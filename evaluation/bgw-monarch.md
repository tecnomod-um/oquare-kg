# Evaluation of the OQuaRE KG framework in biomedical use cases

Biomedical knowledge graphs are a complex and highly structured use case that integrates data on proteins, genes and diseases.

## The knowledge graphs

* Gene regulation knowledge graphs

    Knowledge graphs on the gene regulation domain, with a particular focus on enhancers, which are the most widely studied of the cis-regulatory modules. These sequences were modelled using the CisReg schema, which was also used in BioGateway to integrate data from 25 different sources, modelling information from various biological databases about enhancers and their relations with other entities.

    * Cis-Regulatory modules
        * [Data](https://github.com/juan-mulero/cisregEA)
        * [Evaluation](https://github.com/tecnomod-um/oquare-kg/tree/main/evaluation/results/cisreg)

* The Monarch Knowledge Graph

    The Monarch KG, a biomedical knowledge graph that integrates gene, disease, and phenotype information from 33 heterogeneous data sources, which provides a semantically structured representation of biological entities and their relationships, enabling data integration, semantic reasoning, and biomedical discovery across species.

    * [Data](https://github.com/tecnomod-um/oquare-kg/tree/main/evaluation/monarch)



## Comparability of the knwoledge graphs

The next table describes the size in triples of the two sets of graphs included in this evaluation.

| Graph    | Triples    | | Graph    | Triples    | 
|--------------|--------------|
| crm2tfac    | 12,933      | |http://mymonarchinitiative.org/slice/assoc     | 20,934       | 
| crm2phen     | 45,794       | |http://mymonarchinitiative.org/slice/pheno     | 58,457       | 
| crm2gene     | 282,491      | |http://mymonarchinitiative.org/slice/gene-pheno-nervous     | 222,575      | 
| crm    | 1,483,949     | |http://mymonarchinitiative.org/slice/gene-pheno-human     | 604,602      | 
|all    |1,622,550      | |http://mymonarchinitiative.org/slice/complete     | 659,726      | 


The validation compares two families of RDF graphs — the CisReg/BioGateway set
(crm2tfac, crm2phen, crm2gene, crm, all) and the Monarch set
(assoc, pheno, gene-pheno-nervous, gene-pheno-human, complete). The two families are
comparable along every dimension that matters for an OQuaRE-KG evaluation, and
this comparability is engineered into the extraction rather than assumed.

* Same representation, same metric applicability. Both families are RDF/OWL-native
knowledge graphs. OQuaRE-KG therefore applies to the Monarch set with exactly the
same operational definitions used for BioGateway — no translation, re-serialisation
or schema mapping intervenes that could introduce a confound. Any difference in the
resulting scores is attributable to the graphs, not to the measurement pipeline.

* Same construction principle: relation-type slices. Each CisReg graph is a
relation-type slice of a CRM-centred domain (CRM→transcription factor, CRM→phenotype,
CRM→gene). Each Monarch graph is a relation-type slice of a disease-centred domain
(disease→phenotype via has_phenotype, gene→disease via
gene_associated_with_condition). In both families the semantics of the slice is
carried by the predicate, producing clean, interpretable cuts rather than arbitrary
node or triple samples. The extraction logic is the same operation applied to a
different source.

* Same set topology: nested size variants plus a union. Both families comprise
small and medium relation-type slices, a large core graph, and a union graph
(all / mondo_all) formed as the disjunction of the named graphs. The internal
relationships are identical: the smaller graphs are nested within the larger, and
the union is their aggregate. A comparison of one family's profile against the other
therefore compares like structural roles (small↔small, core↔core, union↔union), not
mismatched objects.

* Matched orders of magnitude. The MONDO disorders were chosen so that each Monarch
graph reproduces the triple-count magnitude of its CisReg counterpart. The
correspondence is by role and order of magnitude, tuned by widening or narrowing the
MONDO disorder, rather than by exact biological equivalence. Crucially, at the point
where both families are most sensitive to the aggregation step — the union relative
to the large core — the ratio is almost identical: the Monarch union exceeds its core
by 9.1% (659,726 vs 604,602 triples), against 9.3% for CisReg
(1,622,550 vs 1,483,949). The union operation behaves the same way in both families,
which is direct quantitative evidence that the two sets are structurally analogous.

* Coherent domains and self-consistent baselines. Both families are coherent domain
subgraphs — a regulatory domain in one case, a disease subdomain in the other —
connected and biologically meaningful rather than random cuts. Both are also
self-consistent baselines: annotation closure guarantees that every node retains its
types, names, descriptions and provenance, so no metric is inflated by extraction
artifacts such as orphaned literals or missing type declarations. The only variation
in quality across the experiments comes from the controlled perturbations, which are
applied identically to both families and on verified targets.

* Matched baseline conditions for the perturbations. Where a perturbation depends on
a baseline state, that state coincides across families. For example, labels in both
the CisReg and the Monarch graphs are plain literals with zero language tags, so the
language-tag experiment starts from an identical baseline of 0 in both cases
and measures the same positive enrichment. Like-for-like starting conditions make the
before/after deltas directly comparable.


Nevertheless, the two families are not identical, and the remaining differences are deliberate and accounted for rather than hidden:

* Monarch stores every relation twice — as a direct edge and as a reified
biolink:Association node carrying provenance, evidence and qualifiers — which
activates the Trustworthiness and Provenance dimensions that were flat in BioGateway.
Rather than suppressing this, metrics are reported both with and without association
nodes, so Monarch results can be read against BioGateway on a like-for-like basis
while still exercising the additional dimensions this second graph was chosen to test.

* The largest Monarch graph is capped at ~6×10⁵ triples (a broad but sub-maximal MONDO
root) rather than the full 10⁶ of crm. This compresses the top of the size ladder,
but it preserves the union-to-core ratio noted above, and the invariance of
ratio/density metrics across the ladder is itself one of the properties under test —
so the compression is informative rather than disqualifying.

* The Monarch slice, exactly like the CisReg ones, are nested rather than
mutually independent. This is appropriate to the study's logic: cross-family
independence (Monarch vs BioGateway, two consortia, two modelling approaches) is what
underwrites the generalisation claim, whereas within-family nesting is precisely what
tests robustness of the metrics to graph size. The two kinds of comparison answer two
different questions, and neither relies on the slices being independent of one another.