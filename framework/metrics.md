# The OQuaRE KG quality metrics

A subcharacteristic comprises at least one or more quality metrics which are, in turn, grouped into characteristics.


## Structural
### Formalisation

| **Metric**               | **Definition**                                                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|
|  Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata. |

### Structural accuracy

| **Metric**                                     |   **Definition**                    |
|------------------------------------------------|-------------------------|
| Usage of deprecated classes or properties [^1] | This metric checks whether deprecated terms are used in a graph. More specifically, all used classes and properties are checked if they are members of owl:DeprecatedClass or owl:DeprecatedProperty respectively. The result is a score from 0 to 1, where a value of 0 indicates that there are no deprecated terms in the graph.     |
| Misused OWL datatype or object properties [^1] | This quality indicator assesses a graph’s statements for the correct usage of the predicate in terms the owl:DatatypeProperty and owl:ObjectProperty axioms. Therefore, this metric detects “erroneous” triples where a data value (literal) object is attached to an owl:ObjectProperty, and an entity (individual) to an owl:DatatypeProperty. |
| Misplaced classes or properties [^1]           | The metric assesses the graph’s statements to check the correct usage of classes and properties. More specifically, this quality indicator checks if the assessed graph has defined classes placed in the triple’s predicate and defined properties in the object position. The result is a score from 0 to 1, where a value of 0 indicates that there are no misplaced terms in the graph.
                                                                     |


### Consistency

| **Metric**                                     | **Definition**                    
|------------------------------------------------|---------------------------------------------|
| Misused OWL datatype or object properties [^1] | This quality indicator assesses a graph’s statements for the correct usage of the predicate in terms the owl:DatatypeProperty and owl:ObjectProperty axioms. Therefore, this metric detects “erroneous” triples where a data value (literal) object is attached to an owl:ObjectProperty, and an entity (individual) to an owl:DatatypeProperty. |
| Misplaced classes or properties [^1]           | The metric assesses the graph’s statements to check the correct usage of classes and properties. More specifically, this quality indicator checks if the assessed graph has defined classes placed in the triple’s predicate and defined properties in the object position. The result is a score from 0 to 1, where a value of 0 indicates that there are no misplaced terms in the graph.                                                                      |
| Compatible datatype [^1] | This quality indicator assesses the lexical form of the data values against the data type attached with the literal itself. The result is a score from 0 to 1, where a value of 1 indicates that the datatype of a literal is compatible with its lexical form, whereas 0 indicates that none are.|


### Syntactic validity

| **Metric**               | **Definition**                                                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Compatible datatype [^1] | This quality indicator assesses the lexical form of the data values against the data type attached with the literal itself. The result is a score from 0 to 1, where a value of 1 indicates that the datatype of a literal is compatible with its lexical form, whereas 0 indicates that none are. |
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata. The result is a set of valid serialization formats, or an empty set if none are found.|
| Valid format metric[^1] | This metric identifies whether the declared serialisation formats are valid and conform to recognised RDF syntax specifications. The result is True if valid formats, False otherwise.|

### Redundancy  

| **Metric**                   | **Definition**                                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Extensional conciseness [^1] | The extensional conciseness metric checks for redundant resources in the assessed graph and thus measures the number of unique instances found in the graph. The result is a score from 0 to 1, where a value of 0 indicates that the instances found in the graph are uniques.
 |
 

### Interpretability

| Metric                                       | Definition                                                                                                                                                                                                                             |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph. |
| Re-use of existing terms [^1]                | This metric assesses if a graph re-uses relevant terms in a particular domain. In particular, this metric checks if a property or a class (in case the predicate is rdf:type) used in a triple refers to a term in another vocabulary. The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are.|



## Functional adequacy

### Inference

| **Metric**               | **Definition**                                                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|
|Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata. |
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. |

### Understandability

| **Metric**                                 | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instances with no description metric [^3]      | The ratio of instances lacking a description in the graph. The result is a score from 0 to 1, where a value of 0 indicates that there are no instances without description in the graph.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Instances with no name metric [^3]             | The ratio of instances lacking a name in the graph. The result is a score from 0 to 1, where a value of 0 indicates that there are no instances without a name in the graph.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Instances with no synonym metric [^3]           | The ratio of instances lacking a synonym in the graph. The result is a score from 0 to 1, where a value of 0 indicates that there are no instances without synonym in the graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Descriptions per instance metric [^3]           | This metric accounts for the number of descriptions associated with instances, which can also be provided by using different annotation properties used by the community to include descriptions (rdfs:comment, skos:definition, dcterms:description, etc.). This metric is calculated as the total number of descriptions associated with graph instances divided by the total number of instances in the graph. The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, every instance has at least one description.                                                                                                                                                                                               |
| Names per instance metric [^3]                 | This metric accounts for the number of names associated with instances, and uses the list of annotation properties used by the community for names (rdfs:label, skos:prefLabel, foaf:name, etc.). Then, this metric is calculated as the number of names associated with graph instances divided by the total number of classes in the graph. The range of the value of this metric is the set of real positive numbers. Values lower than one mean that there are instances without any name in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple names; possibly caused by the inclusion of multilingual names or by some design decision.|
| Synonyms per instance metric [^3]               | This metric accounts for the number of synonyms associated with instances, which can also be provided by using different annotation properties used by the community to include synonyms (oboInOwl:hasExactSynonym, skos:altLabel, iao:0000118, etc.). This metric is calculated as the number of synonyms associated with instances divided by the total number of instances in the graph. The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, every instance has at least one synonym.  |
| Annotation richness metric [^4]                 | Mean number of annotation properties per instances. The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates, on average, that each instance is characterized by multiple properties.              |
| Human readable labelling and comments [^1] | The aim of this metric is to calculate graph’s completeness in terms of human readable labels and descriptions. The metric measures the percentage of local entities that have a label or a description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Indication of used vocabularies [^1]       | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata.                                                                                                                                                                                                                                                                                                                                                       |


### Trustworthiness

| **Metric**                                             | **Definition**                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Evidence metric | This metric verifies whether graph’s assertions have terms for capturing evidence. The result is a score from 0 to 1, where a value of 1 indicates that all triples have evidence, whereas 0 indicates that none are.  |
| Evidence codes metric | This metric verifies whether graph’s assertions have terms for capturing evidence. The result is a score from 0 to 1, where a value of 1 indicates that, on average, every triple has at least one evidence URI, whereas 0 indicates that none are. |
| Traceability of the data [^1]                          | This metric checks whether each resource has provenance information related to the origin of data. The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.    |


### Provenance
 
| **Metric**                                     | **Definition**                                                                                                                                                                                                                                                              |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset. The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.                                                                                                                                                                                     |
| Traceability of the data [^1]                  | This metric checks whether each resource has provenance information related to the origin of data. The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.                                                                                                                                                                         |

### Clustering  

| **Metric**                                   | **Definition**                                                                                                                                                                                |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph. |
| Relations per node metric | Average number of relations per graph node. The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, that each node has multiple relations. |
| Synonyms per instance metric [^3]               | This metric accounts for the number of synonyms associated with instances, which can also be provided by using different annotation properties used by the community to include synonyms (oboInOwl:hasExactSynonym, skos:altLabel, iao:0000118, etc.). This metric is calculated as the number of synonyms associated with instances divided by the total number of instances in the graph. The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, every instance has at least one synonym.  |



## Compatibility
### Interoperability

| **Metric**                                   | **Definition**                                                                                                                                                                                                                                 |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Re-use of existing terms [^1]                | This metric   assesses if a graph re-uses relevant terms in a particular domain. In   particular, this metric checks if a property or a class (in case the   predicate is rdf:type) used in a triple refers to a term in another vocabulary. The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are. |
|  Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata.|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata. The result is a set of valid serialization formats, or an empty set if none are found.|




## Transferability
### Versatility

| **Metric**                           | **Definition**                                                                                |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata.  The result is a set of valid serialization formats, or an empty set if none are found.|
| Usage of multiple languages [^1]     | This metric checks the number of languages a graph supports. The result is a score from 0 to 1, where a value of 1 indicates that all the labels have language tags, whereas 0 indicates that none are.                                 |


## Operability
### Licensing

| **Metric**                    | **Definition**                                                                                                                                   |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Machine-readable license [^1] | The aim of this metric is to check if a dataset has a valid machine-readable license. The result is True if a valid machine-readable license is found, False otherwise.                                                             |
| Human-readable license [^1]   | Verifies whether a human-readable text, stating the licensing model attributed to the resource, has been provided as part of the graph. The result is True if a valid human-readable license description is found, False otherwise.         |


## Reliability
### Accessibility

| **Metric**                            | **Definition**                                                                                                             |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Dereferenceability of the URI [^1]    | The aim of this metric is to check the number of valid dereferenceable URIs used in a graph. The result is a score from 0 to 1, where a value of 1 indicates that all the URIs are dereferenceables, whereas 0 indicates that none are.                            |
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset. The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.                                                                                                                                                       |
| Traceability of the data [^1]                  | This metric checks whether each resource has provenance information related to the origin of data. The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.                                                                                                                                                               |
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata.  The result is a set of valid serialization formats, or an empty set if none are found.|


## Maintainability
### Reusability

| **Metric**                    | **Definition**                                                                                                                                   |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Re-use of existing terms [^1]                | This metric   assesses if a graph re-uses relevant terms in a particular domain. In   particular, this metric checks if a property or a class (in case the   predicate is rdf:type) used in a triple refers to a term in another   vocabulary. The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are.|
| Machine-readable license [^1] | The aim of this metric is to check if a dataset has a valid machine-readable license. The result is True if a valid machine-readable license is found, False otherwise.                                                            |
| Human-readable license [^1]   | Verifies whether a human-readable text, stating the licensing model attributed to the resource, has been provided as part of the graph. The result is True if a valid human-readable license description is found, False otherwise.         |
| Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata. |
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset. The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.                                                                                                                                                       |
| Traceability of the data [^1]                  | This metric checks whether each resource has provenance information related to the origin of data. The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.                                                                                                                                                               |






[^1]: Modified from: Debattista, J., Lange, C., Auer, S., & Cortis, D. (2018). Evaluating the quality of the LOD cloud: An empirical investigation. Semantic Web, 9(6), 859-901. https://doi.org/10.3233/SW-180306
[^2]: Zaveri, A., Rula, A., Maurino, A., Pietrobon, R., Lehmann, J., & Auer, S. (2016). Quality assessment for Linked Data: A Survey. Semantic Web, 7(1), 63-93.https://doi.org/10.3233/SW-150175
[^3]: Modified from: Abad-Navarro, F., Martínez-Costa, C., & Fernández-Breis, J. T. (2023). HURON: A Quantitative Framework for Assessing Human Readability in Ontologies. IEEE Access, 11, 101833-101851. IEEE Access. https://doi.org/10.1109/ACCESS.2023.3316512
[^4]: Modified from: Duque-Ramos, A., Fernández-Breis, J. T., Stevens, R., & Aussenac-Gilles, N. (2011). OQuaRE: A SQuaRE-based Approach for Evaluating the Quality of Ontologies. Journal of Research and Practice in Information Technology, 43(2).

