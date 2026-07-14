# Description of the processing of the Monarch KG 


## The Monarch KG

Monarch was selected because it is RDF/OWL-native (so OQuaRE-KG metrics apply directly), independently produced by another consortium, and rich in provenance, evidence and licensing metadata.

- Monarch release loaded in GraphDB: `__version/date__`
- Extraction date: `2026-07-03`
- MONDO branch(es) used as seed: `__IRI(s)__`


## Preliminary analysis

The Monarch graph was profiled with SPARQL. The following findings are the most relevant, as they determine what can be measured and perturbed and how the framework must be configured:
* Reified associations plus direct edges. Every relation is stored twice — as a direct triple and as a biolink:Association node (~15.2M) that carries provenance, evidence and qualifiers.
* Names. rdfs:label (1.44M), plus biolink:symbol (585K) and biolink:full_name (585K) for genes. Labels are plain literals with zero language tags, so Exp.3 (adding tags) is meaningful and starts from a baseline of 0, as in BioGateway.
* Descriptions. dcterms:description (540K); there is no rdfs:comment.
* Synonyms. biolink:synonym (1.53M) plus exact / related / narrow / broad synonym variants.
* Numeric typed literals (ammunition for Exp.4). has_count / has_total (190K, integers), evidence_count (15.2M, integer), has_percentage / has_quotient (190K, float) — targets for controlled datatype corruption.
* Provenance as literals. primary_knowledge_source (15.2M), aggregator_knowledge_source (20.4M) and provided_by (16.7M) activate the Trustworthiness and Provenance dimensions, which were flat in BioGateway.
* Confirmed typing defect. rdf:type with a literal object appears 87,885 times (e.g. "genotype", "strain", "SO:0001589|SO:0001627"): a concrete structural-accuracy count for the baseline QC — to be reported, not perturbed.

The full graph (>15M associations) is too large to run the full perturbation matrix repeatedly (four experiment types × multiple levels × several random seeds) within reasonable time and storage. A well-chosen slice preserves the properties we need to measure while making the experiment tractable and reproducible. Size is a means, not an end: the slice must remain a valid, representative KG.

### Profiling queries

In order to carry out this initial analysis and profiling of the queries, we executed the following queries

#### Predicates by frequency
```sparql
SELECT ?p (COUNT(*) AS ?n) WHERE { ?s ?p ?o } GROUP BY ?p ORDER BY DESC(?n)
```

#### rdf:type distribution
```sparql
SELECT ?type (COUNT(*) AS ?n) WHERE { ?s a ?type } GROUP BY ?type ORDER BY DESC(?n)
```

#### Predicates with a literal object
```sparql
SELECT ?p (COUNT(*) AS ?n) WHERE { ?s ?p ?o FILTER(isLiteral(?o)) } GROUP BY ?p ORDER BY DESC(?n)
```
#### Labels with a language tag (expected result: 0)

```sparql
PREFIX rdfs:     <http://www.w3.org/2000/01/rdf-schema#>
SELECT (COUNT(*) AS ?tagged) WHERE { ?s rdfs:label ?l FILTER(lang(?l) != "") }
```

## Design of the subgraphs for the experiments
The goal is to produce several graphs of increasing size (~10^4, 10^5, 10^6 triples) which could be assimilated with the graphs generated for the CisReg case. Matching the orders of magnitude of the CisReg family makes the two cases directly comparable. It also adds a validation dimension for free: ratio/density metrics should be invariant to graph size, so stable profiles across variants provide extra evidence of the framework’s soundness, while any size-dependence would be an informative finding.

### Criterion 1. Entity-centric extraction with annotation closure

Select a set of core entities/edges and then pull in the complete set of triples that describe those entities, rather than sampling triples at random. The uniform random sampling of nodes without their context would orphan literals, break type declarations and delete labels/descriptions. That would artificially inflate exactly the metrics we later perturb (instances with no name/type/description), confounding the experiment. 

The only variation in quality must come from the controlled perturbations, so the baseline slice has to be a faithful, self-consistent KG. "Closure" means: after choosing the core, we add every triple that types, names, describes or provides provenance for the involved nodes.

### Criterion 2. Thematic slice by disease branch 

Seed the slice from a disease branch (a MONDO class and all its descendants via subclass_of*), then collect the associated phenotypes and genes. A coherent biological subdomain yields a connected, meaningful subgraph — mirroring the nature of the CisReg graphs, which are themselves coherent domain slices. Seeding by an ontology branch also gives a clean, reproducible size lever: a narrow class produces a small graph, a broad class a large one, without resorting to random cuts that would damage connectivity.

### Criterion 3. Slicing by relation type (rdf:predicate)
Define the core edges by association predicate (disease–phenotype via has_phenotype; gene–disease via gene_associated_with_condition). The relation type already encodes the semantics of the slice, so we obtain a clean, interpretable cut without needing to enumerate node-category IRIs. It also parallels the BioGateway design, where each graph (crm2gene, crm2phen, crm2tfac) is a relation-type slice — maximising comparability between the two cases.

### Criterion 4. Independent slices
Using disjoint disease branches reproduces the CisReg structure - several distinct slices plus a genuine union - and lets size be tuned by branch breadth. The roots are chosen so that none is an ancestor or descendant of another, so the graphs do not overlap and the union carries no double counting, exactly as CisReg’s "all" is the union of its slices. Each graph is rebuilt independently (re-running the full annotation closure per branch) rather than assembled from smaller ones, which guarantees every graph is self-consistent. As a bonus, comparing across sizes tests whether ratio/density metrics stay stable, which they should; any size-dependence would itself be an informative finding.Using disjoint disease branches reproduces the CisReg structure - several distinct slices plus a genuine union — and lets size be tuned by branch breadth. The roots are chosen so that none is an ancestor or descendant of another, so the graphs do not overlap and the union carries no double counting, exactly as CisReg’s "all" is the union of its slices. Each graph is rebuilt independently (re-running the full annotation closure per branch) rather than assembled from smaller ones, which guarantees every graph is self-consistent. As a bonus, comparing across sizes tests whether ratio/density metrics stay stable, which they should; any size-dependence would itself be an informative finding.


## The queries to obtain the subgraphs

### Graph 1. Gene-condition associations by disorder or a subtype.


```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX biolink:  <https://w3id.org/biolink/vocab/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(*) AS ?count) ?dis ?dis_label
WHERE {
  ?a rdf:predicate biolink:gene_associated_with_condition ; 
	 rdf:object ?d .
  ?d biolink:subclass_of*  ?dis.
   ?dis biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0000001>.
  ?dis rdfs:label ?dis_label .
  ?a ?ap ?ao .
} 
GROUP BY  ?dis ?dis_label
```

[Results of query graph associations](data/query1-associations.xlsx)


### Graph 2.  Triples that describe has_phenotype associations by disorder  or a subtype

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX biolink:  <https://w3id.org/biolink/vocab/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(*) AS ?count) ?dis ?dis_label
WHERE {
  ?a rdf:predicate biolink:has_phenotype ; rdf:subject ?d .
  ?d biolink:subclass_of*  ?dis.
  ?dis biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0000001>.
  ?dis rdfs:label ?dis_label .
  ?a ?ap ?ao .
} 
GROUP BY  ?dis ?dis_label
```
[Results of query graph phenotypes associations](data/query2-phenotypes.xlsx)

### Graph 3. Phenotype associations and gene associations exist in Monarch by disorder and all its ontological subtypes combined?

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX biolink:  <https://w3id.org/biolink/vocab/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(*) AS ?count) ?dis ?dis_label
WHERE {

  VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition }
  ?s ?p ?o .
  { ?s biolink:subclass_of* ?dis } UNION { ?o biolink:subclass_of* ?dis}
  ?dis biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0000001>.
  ?dis rdfs:label ?dis_label .
} 
GROUP BY  ?dis ?dis_label
```
[Results of query graph phenotypes + genes associations](data/query3-genespluspheno.xlsx)

#### Disorder selection

At this point, we selected the disorder for the slicing of the graph. For this purpose we selected the diseases to achieve graphs of the following size. One branch (disorder) is used only for one graph

* Graph 1: approx 10K: http://purl.obolibrary.org/obo/MONDO_0004995	(cardiovascular disorder): 9,184 triples
* Graph 2: approx 40K-50K: http://purl.obolibrary.org/obo/MONDO_0019751 (autoinflammatory syndrome): 45,940 triples
* Graph 3: approx 80K-100K: http://purl.obolibrary.org/obo/MONDO_0005071 (nervous system disorder); 82,737 triples




### Graph 1 Creation

generation: gene_associated_with_condition, disease in the OBJECT slot
```sparql

INSERT { GRAPH <http://mymonarchinitiative.org/slice/assoc> { ?a ?ap ?ao } }
WHERE {
  ?a rdf:predicate biolink:gene_associated_with_condition ; rdf:object ?d .
  ?d biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0004995> .
  ?a ?ap ?ao .
} ;

```
closure (reified: nodes via rdf:subject/rdf:object)
```sparql

INSERT { GRAPH <http://mymonarchinitiative.org/slice/assoc> { ?n ?np ?no } }
WHERE {
  GRAPH <http://mymonarchinitiative.org/slice/assoc> { ?a ?sp ?n . VALUES ?sp { rdf:subject rdf:object } }
  ?n ?np ?no .
  FILTER(?np IN (rdf:type, biolink:category, rdfs:label, dcterms:description,
    biolink:synonym, biolink:exact_synonym, biolink:related_synonym,
    biolink:narrow_synonym, biolink:broad_synonym, biolink:xref,
    biolink:symbol, biolink:full_name, biolink:in_taxon, biolink:in_taxon_label,
    biolink:deprecated))
} ;

```

### Graph 2 Creation

```sparql
# generation: has_phenotype, disease in the SUBJECT slot
INSERT { GRAPH <http://mymonarchinitiative.org/slice/pheno> { ?a ?ap ?ao } }
WHERE {
  ?a rdf:predicate biolink:has_phenotype ; rdf:subject ?d .
  ?d biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0019751> .
  ?a ?ap ?ao .
} ;
```
# closure (reified)
```sparql
INSERT { GRAPH <http://mymonarchinitiative.org/slice/pheno> { ?n ?np ?no } }
WHERE {
  GRAPH <http://mymonarchinitiative.org/slice/pheno> { ?a ?sp ?n . VALUES ?sp { rdf:subject rdf:object } }
  ?n ?np ?no .
  FILTER(?np IN (rdf:type, biolink:category, rdfs:label, dcterms:description,
    biolink:synonym, biolink:exact_synonym, biolink:related_synonym,
    biolink:narrow_synonym, biolink:broad_synonym, biolink:xref,
    biolink:symbol, biolink:full_name, biolink:in_taxon, biolink:in_taxon_label,
    biolink:deprecated))
} ;


### Graph 3 Creation


generation: both predicates, direct edges, disease as subject OR object
```sparql
INSERT { GRAPH <http://mymonarchinitiative.org/slice/gene-pheno> { ?s ?p ?o } }
WHERE {
  VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition }
  ?s ?p ?o .
  { ?s biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0005071> }
  UNION
  { ?o biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0005071> }
} ;
```

closure (direct: nodes via subject/object of the edges)
```sparql
INSERT { GRAPH <http://mymonarchinitiative.org/slice/gene-pheno> { ?n ?np ?no } }
WHERE {
  GRAPH <http://mymonarchinitiative.org/slice/gene-pheno> {
    { ?n ?p ?o . VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition } }
    UNION
    { ?s ?p ?n . VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition } }
  }
  ?n ?np ?no .
  FILTER(?np IN (rdf:type, biolink:category, rdfs:label, dcterms:description,
    biolink:synonym, biolink:exact_synonym, biolink:related_synonym,
    biolink:narrow_synonym, biolink:broad_synonym, biolink:xref,
    biolink:symbol, biolink:full_name, biolink:in_taxon, biolink:in_taxon_label,
    biolink:deprecated))
} ;
```

### Graph 4. Annotation closure for the three graphs


# generation: both predicates, direct edges, broad root (human disease)
```sparql
INSERT { GRAPH <http://mymonarchinitiative.org/slice/mondo_xl> { ?s ?p ?o } }
WHERE {
  VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition }
  ?s ?p ?o .
  { ?s biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0700096> }
  UNION
  { ?o biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0700096> }
} ;
```
# closure (direct)
```sparql
INSERT { GRAPH <http://mymonarchinitiative.org/slice/mondo_xl> { ?n ?np ?no } }
WHERE {
  GRAPH <http://mymonarchinitiative.org/slice/mondo_xl> {
    { ?n ?p ?o . VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition } }
    UNION
    { ?s ?p ?n . VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition } }
  }
  ?n ?np ?no .
  FILTER(?np IN (rdf:type, biolink:category, rdfs:label, dcterms:description,
    biolink:synonym, biolink:exact_synonym, biolink:related_synonym,
    biolink:narrow_synonym, biolink:broad_synonym, biolink:xref,
    biolink:symbol, biolink:full_name, biolink:in_taxon, biolink:in_taxon_label,
    biolink:deprecated))
} ;
```