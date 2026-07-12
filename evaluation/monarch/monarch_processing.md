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




## The queries to obtain the subgraphs

### Graph 1. Gene-condition associations for a disorder or a subtype.

*Query for any disorder*

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
*Query for cardiovascular disorder*

```sparql
PREFIX biolink:  <https://w3id.org/biolink/vocab/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(*) AS ?count)
WHERE {
  ?a rdf:predicate biolink:gene_associated_with_condition ; 
	 rdf:object ?d .
  ?d biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0004995> .
  ?a ?ap ?ao .
} 
```

The output graph has 9,184 triples.

### Graph 2.  Triples that describe has_phenotype associations for a  disease subject  or a subtype

*Query for any disorder*
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

*Query for cardiovascular disorder*

```sparql
PREFIX biolink:  <https://w3id.org/biolink/vocab/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(*) AS ?count)
WHERE {
  ?a rdf:predicate biolink:has_phenotype ; rdf:subject ?d .
  ?d biolink:subclass_of* <http://purl.obolibrary.org/obo/MONDO_0004995>.
  ?a ?ap ?ao .
} 
```
The output graph has 291,185 triples.

# Graph 3. Phenotype associations and gene associations exist in Monarch for type 2 diabetes mellitus and all its ontological subtypes combined?
```sparql
PREFIX biolink:  <https://w3id.org/biolink/vocab/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(*) AS ?count)
WHERE {
VALUES ?DISEASE { <http://purl.obolibrary.org/obo/MONDO_0004995> }
  VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition }
  ?s ?p ?o .
  { ?s biolink:subclass_of* ?DISEASE } UNION { ?o biolink:subclass_of* ?DISEASE}
} 
```
The output graph has 15,689 triples.

# Graph 4. Genes associated with cardiovascular diseases plus has phenotype cardiovascular disease, plus full annotation closure
```sparql
PREFIX biolink:  <https://w3id.org/biolink/vocab/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(*) AS ?count)
WHERE {
VALUES ?DISEASE { <http://purl.obolibrary.org/obo/MONDO_0004995> }
  VALUES ?p { biolink:has_phenotype biolink:gene_associated_with_condition }
  ?s ?p ?o .
  { ?s biolink:subclass_of* ?DISEASE } UNION { ?o biolink:subclass_of* ?DISEASE}
} 
```

## 5. Nested size variants

Generate 3–4 graphs by changing only the `?ROOT` branch (narrow subbranch → cardiovascular → a broader superclass), aiming to match the orders of magnitude of CisReg (~10^4, 10^5, 10^6). For the largest one, add a second branch with UNION if needed. Materialize each variant in its own named graph (`urn:slice:mondo_s`, `_m`, `_l`) and the union as `all`.

```sparql
# Control count
SELECT (COUNT(*) AS ?triples) WHERE { GRAPH <urn:slice:mondo> { ?s ?p ?o } }
```

| CisReg graph | Triples | Monarch graph | Construction (predicate + MONDO breadth) | Target size |
|---|---|---|---|---|
| crm2tfac | 12,933 | mondo_s | gene_associated_with_condition; narrow MONDO branch | ~10^4 |
| crm2phen | 45,794 | mondo_m | has_phenotype (disease→phenotype); medium branch | ~5×10^4 |
| crm2gene | 82,491 | mondo_l | gene_associated_with_condition + has_phenotype; larger branch | ~10^5 |
| crm | 1,483,949 | mondo_xl | both predicates + full annotation closure; broad branch | ~10^6 |
| all | 1,622,550 | mondo_all | union of the Monarch named graphs above | sum of the above |



## 6. OQuaRE-KG configuration for Monarch (CRITICAL)

Add the following to the framework's annotation-property lists, or the baseline will be artificially poor:

- Names: `rdfs:label`, `biolink:symbol`, `biolink:full_name`
- Descriptions: `dcterms:description`
- Synonyms: `biolink:synonym`, `biolink:exact_synonym`, `biolink:related_synonym`, `biolink:narrow_synonym`, `biolink:broad_synonym`

Modeling decision to declare: `biolink:Association` (reification) nodes have no label/description by design and will raise *instances with no name/description*. Consider reporting metrics **with and without** association nodes for a fair comparison with BioGateway.

## 7. Perturbation targets per experiment

| Exp. | Perturbation | Target predicate(s) | Levels |
|---|---|---|---|
| 1 | Remove names | `rdfs:label` (+ `biolink:symbol`, `biolink:full_name`) | 20/50/90 % |
| 2 | Remove descriptions | `dcterms:description` | 20/50/90 % |
| 3 | Add language tags | on `rdfs:label` (plain literals) | 20/50/90 % |
| 4 | Wrong datatypes | `has_count`, `has_total`, `evidence_count`, `has_percentage`, `has_quotient` | 10/30/50/90 % |

Methodological recommendation (from the review): additionally use finer levels (e.g. steps of 5–10 %) to locate the detection threshold at the quality-score level, and repeat each perturbation with several seeds, reporting variance. ALWAYS perturb the exported `.ttl`, never during extraction.

## 8. Baseline QC (before perturbing)

```sparql
# Malformed types within the slice (rdf:type with a literal object)
SELECT (COUNT(*) AS ?bad) WHERE {
  GRAPH <urn:slice:mondo> { ?s rdf:type ?o FILTER(isLiteral(?o)) }
}

# Instances with no label / no description (baseline sanity check)
SELECT (COUNT(DISTINCT ?s) AS ?noLabel) WHERE {
  GRAPH <urn:slice:mondo> { ?s ?p ?o } FILTER NOT EXISTS { GRAPH <urn:slice:mondo> { ?s rdfs:label ?l } }
}

# Language tags on slice labels (expected: 0)
SELECT (COUNT(*) AS ?tagged) WHERE {
  GRAPH <urn:slice:mondo> { ?s rdfs:label ?l FILTER(lang(?l) != "") }
}
```

Also verify: valid RDF, connected subgraph, and quality profiles that are stable across size variants. Report the malformed-type count as an intrinsic Monarch property (evidence that OQuaRE-KG detects real issues).
