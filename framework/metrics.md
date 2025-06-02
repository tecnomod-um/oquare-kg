# The OQuaRE KG quality metrics

A subcharacteristic comprises at least one or more quality metrics which are, in turn, grouped into characteristics.


## Structural
### Formalisation

| **Metric**               | **Definition**                                                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|
|  Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric.  |


### Consistency

| **Metric**                                     | **Definition**                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Usage of deprecated classes or properties [^1] | This metric checks whether deprecated terms are used in a graph. More specifically, all used classes and properties are checked if they are members of owl:DeprecatedClass or owl:DeprecatedProperty respectively.                                                                                                                               |
| Misused OWL datatype or object properties [^1] | This quality indicator assesses a graph’s statements for the correct usage of the predicate in terms the owl:DatatypeProperty and owl:ObjectProperty axioms. Therefore, this metric detects “erroneous” triples where a data value (literal) object is attached to an owl:ObjectProperty, and an entity (individual) to an owl:DatatypeProperty. |
| Misplaced classes or properties [^1]           | The metric assesses the graph’s statements to check the correct usage of classes and properties. More specifically, this quality indicator checks if the assessed graph has defined classes placed in the triple’s predicate and defined properties in the object position.                                                                      |

### Syntactic validity

| **Metric**               | **Definition**                                                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Compatible datatype [^1] | This quality indicator assesses the lexical form of the data values against the data type attached with the literal itself. |

### Redundancy  

| **Metric**                   | **Definition**                                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Extensional conciseness [^1] | The extensional conciseness metric checks for redundant resources in the assessed graph and thus measures the number of unique instances found in the graph. |
 

### Interpretability

| Metric                                       | Definition                                                                                                                                                                                                                             |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Re-use of existing terms [^1]                | This metric assesses if a graph re-uses relevant terms in a particular domain. In particular, this metric checks if a property or a class (in case the predicate is rdf:type) used in a triple refers to a term in another vocabulary. |



### Timeliness

| **Metric**                                                  | **Definition**                                                                                                                                                                          |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Freshness of datasets based on currency and volatility [^2] | Detecting freshness of graphs based on currency and volatility. Currency is the age of the data when delivered to the user and volatility is the length of time the data remains valid. |
| Freshness of datasets based on their data source [^2]       | Detecting freshness of datasets based on their data source by measuring the distance between the last modified time of the data source and last modified time of the dataset            |



## Functional adequacy

### Inference

| **Metric**               | **Definition**                                                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|
|Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric.  |

### Understandability

| **Metric**                                 | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instances with no description metric [^3]      | The Percentage of instances lacking a description in the graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Instances with no name metric [^3]             | The Percentage of instances lacking a name in the graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Instances with no synonym metric [^3]           | The Percentage of instances lacking a synonym in the graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Descriptions per instance metric [^3]           | This metric accounts for the number of descriptions associated with instances, which can also be provided by using different annotation properties used by the community to include descriptions (rdfs:comment, skos:definition, dcterms:description, etc.). This metric is calculated as the total number of descriptions associated with graph instances divided by the total number of instances in the graph. The range of the value of this metric is the set of real positive numbers.                                                                                                                                                                                                |
| Names per instance metric [^3]                 | This metric accounts for the number of names associated with instances, and uses the list of annotation properties used by the community for names (rdfs:label, skos:prefLabel, foaf:name, etc.). Then, this metric is calculated as the number of names associated with graph instances divided by the total number of classes in the graph. The range of the value of this metric is the set of real positive numbers. Values lower than one mean that there are instances without any name in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple names; possibly caused by the inclusion of multilingual names or by some design decision. |
| Synonyms per instance metric [^3]               | This metric accounts for the number of synonyms associated with instances, which can also be provided by using different annotation properties used by the community to include synonyms (oboInOwl:hasExactSynonym, skos:altLabel, iao:0000118, etc.). This metric is calculated as the number of synonyms associated with instances divided by the total number of instances in the graph. The range of the value of this metric is the set of real positive numbers.                                                                                                                                                                                                                      |
| Annotation richness metric [^4]                 | Mean number of annotation properties per instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Human readable labelling and comments [^1] | The aim of this metric is to calculate graph’s completeness in terms of human readable labels and descriptions. The metric measures the percentage of local entities that have a label or a description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Indication of used vocabularies [^1]       | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric.                                                                                                                                                                                                                                                                                                                                                       |


### Trustworthiness

| **Metric**                                             | **Definition**                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Evidence metric | This metric verifies whether graph’s assertions have terms for capturing evidence.  |
| Traceability of the data [^1]                          | This metric checks whether each resource has provenance information related to the origin of data.                                                                                                                                                                                            |


### Provenance
 
| **Metric**                                     | **Definition**                                                                                                                                                                                                                                                              |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset.                                                                                                                                                                                     |
| Traceability of the data [^1]                  | This metric checks whether each resource has provenance information related to the origin of data.                                                                                                                                                                          |

### Clustering  

| **Metric**                                   | **Definition**                                                                                                                                                                                |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links to external linked data providers [^1] | Well-interlinked data enables better analysis and understanding of the data. The aim of this metric is to identify the total number of external RDF links used within the   assessed dataset. |



## Compatibility
### Interoperability

| **Metric**                                   | **Definition**                                                                                                                                                                                                                                 |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Re-use of existing terms [^1]                | This metric   assesses if a graph re-uses relevant terms in a particular domain. In   particular, this metric checks if a property or a class (in case the   predicate is rdf:type) used in a triple refers to a term in another   vocabulary. |




## Transferability
### Versatility

| **Metric**                           | **Definition**                                                                                |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata.|
| Usage of multiple languages [^1]     | This metric checks the number of languages a graph supports.                                  |


## Operability
### Licensing

| **Metric**                    | **Definition**                                                                                                                                   |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Machine-readable license [^1] | The aim of this metric is to check if a dataset has a valid machine-readable license.                                                            |
| Human-readable license [^1]   | Verifies whether a human-readable text, stating the licensing model attributed to the resource, has been provided as part of the graph.          |


## Reliability
### Availability

| **Metric**                            | **Definition**                                                                                                             |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Dereferenceability of the URI [^1]    | The aim of this metric is to check the number of valid   dereferenceable URIs used in a graph.                             |






[^1]: Modified from: Debattista, J., Lange, C., Auer, S., & Cortis, D. (2018). Evaluating the quality of the LOD cloud: An empirical investigation. Semantic Web, 9(6), 859-901. https://doi.org/10.3233/SW-180306
[^2]: Zaveri, A., Rula, A., Maurino, A., Pietrobon, R., Lehmann, J., & Auer, S. (2016). Quality assessment for Linked Data: A Survey. Semantic Web, 7(1), 63-93.https://doi.org/10.3233/SW-150175
[^3]: Modified from: Abad-Navarro, F., Martínez-Costa, C., & Fernández-Breis, J. T. (2023). HURON: A Quantitative Framework for Assessing Human Readability in Ontologies. IEEE Access, 11, 101833-101851. IEEE Access. https://doi.org/10.1109/ACCESS.2023.3316512
[^4]: Modified from: Duque-Ramos, A., Fernández-Breis, J. T., Stevens, R., & Aussenac-Gilles, N. (2011). OQuaRE: A SQuaRE-based Approach for Evaluating the Quality of Ontologies. Journal of Research and Practice in Information Technology, 43(2).

