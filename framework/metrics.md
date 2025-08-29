# The OQuaRE KG quality metrics

A subcharacteristic comprises at least one or more quality metrics which are, in turn, grouped into characteristics.


## Structural
### Formalisation

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
|  Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric.| The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata.| [Metric code](./metricsCode/usedVocabulariesMetric.py)|

**Formula**

- Indication of used vocabularies
$$
\mathrm{Metric}(G) =
\frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}
$$


### Structural accuracy

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Usage of deprecated classes or properties [^1] | This metric checks whether deprecated terms are used in a graph. More specifically, all used classes and properties are checked if they are members of owl:DeprecatedClass or owl:DeprecatedProperty respectively.  | The result is a score from 0 to 1, where a value of 0 indicates that there are no deprecated terms in the graph.|[Metric code](./metricsCode/deprecatedClassPropMetric.py)|
| Misused OWL datatype or object properties [^1] | This quality indicator assesses a graph’s statements for the correct usage of the predicate in terms the owl:DatatypeProperty and owl:ObjectProperty axioms. Therefore, this metric detects “erroneous” triples where a data value (literal) object is attached to an owl:ObjectProperty, and an entity (individual) to an owl:DatatypeProperty.  | The result is a score from 0 to 1, where a value of 0 indicates that there are no misused properties in the graph.| [Metric code](./metricsCode/misusedDatatypeObjPropMetric.py)|
| Misplaced classes or properties [^1]           | The metric assesses the graph’s statements to check the correct usage of classes and properties. More specifically, this quality indicator checks if the assessed graph has defined classes placed in the triple’s predicate and defined properties in the object position. | The result is a score from 0 to 1, where a value of 0 indicates that there are no misplaced terms in the graph.| [Metric code](./metricsCode/misplacedClassPropMetric.py)|

**Formulas**

- Usage of deprecated classes or properties
$$
\mathrm{Metric}(G) =
\frac{|DepClasses(G)| + |DepProperties(G)|}{|Classes(G)| + |Properties(G)|}
$$
- Misused OWL datatype or object properties
$$
\mathrm{Metric}(G) =
\frac{|MisusedDP(G)| + |MisusedOP(G)|}{|G|}
$$
- Misplaced classes or properties
$$
\mathrm{Metric}(G) =
\frac{|MisplacedClasses(G)| + |MisplacedProperties(G)|}{|G|}
$$



### Consistency

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Misused OWL datatype or object properties [^1] | This quality indicator assesses a graph’s statements for the correct usage of the predicate in terms the owl:DatatypeProperty and owl:ObjectProperty axioms. Therefore, this metric detects “erroneous” triples where a data value (literal) object is attached to an owl:ObjectProperty, and an entity (individual) to an owl:DatatypeProperty.| The result is a score from 0 to 1, where a value of 0 indicates that there are no misused properties in the graph.| [Metric code](./metricsCode/misusedDatatypeObjPropMetric.py)|
| Misplaced classes or properties [^1]           | The metric assesses the graph’s statements to check the correct usage of classes and properties. More specifically, this quality indicator checks if the assessed graph has defined classes placed in the triple’s predicate and defined properties in the object position.| The result is a score from 0 to 1, where a value of 0 indicates that there are no misplaced terms in the graph.   | [Metric code](./metricsCode/misplacedClassPropMetric.py)|
| Compatible datatype [^1] | This quality indicator assesses the lexical form of the data values against the data type attached with the literal itself.| The result is a score from 0 to 1, where a value of 1 indicates that the datatype of a literal is compatible with its lexical form, whereas 0 indicates that none are.| [Metric code](./metricsCode/compatibleDatatypeMetric.py)|
| Classes per instance metric | Mean number of classes per instance. This metric measure whether an instance has two rdf:type. |The range of the value of this metric is the set of real positive numbers. Values lower than 1 mean that there are instances without any rdf:type in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple rdf:types. | [Metric code](./metricsCode/classesPerInstanceMetric.py)|
| Instances with multiple types metric | The ratio of instances of more than one type. This metric measure whether an instance has more than one rdf:type. |The result is a score from 0 to 1, where a value of 0 indicates that there are no instances that have more than one rdf:type in the graph.| [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|
| Usage of undefined classes and properties [^1] | This metric measures if there are entities in the graph which are not described with ontology terms. | The result is a score from 0 to 1, where a value of 0 indicates that there are no undefined terms in the graph.| [Metric code](./metricsCode/usageUndefinedClassPropMetric.py)|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph.| The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph. | [Metric code](./metricsCode/entitiesNoTypeMetric.py)|

**Formulas**
- Misused OWL datatype or object properties
$$
\mathrm{Metric}(G) =
\frac{|MisusedDP(G)| + |MisusedOP(G)|}{|G|}
$$
- Misplaced classes or properties
$$
\mathrm{Metric}(G) =
\frac{|MisplacedClasses(G)| + |MisplacedProperties(G)|}{|G|}
$$
- Compatible datatype
$$
\mathrm{Metric}(G) = \frac{|ValidLiterals(G)|}{|Literals(G)|}
$$
- Classes per instance metric
$$
\mathrm{Metric}(G) =
\frac{\sum_{i \in Ind(G)} |Classes(i)|}{|Ind(G)|}
$$

- Instances with multiple types metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid |Classes(i)| > 1 \}|}{|Ind(G)|}
$$

- Usage of undefined classes and properties
$$
\mathrm{Metric}(G) =
\frac{|UndefClasses(G)| + |UndefProperties(G)|}{|Classes(G)| + |Properties(G)|}
$$

- Entities with no type metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Classes(i) = \varnothing \}|}{|Ind(G)|}
$$

### Syntactic validity

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Compatible datatype [^1] | This quality indicator assesses the lexical form of the data values against the data type attached with the literal itself. | The result is a score from 0 to 1, where a value of 1 indicates that the datatype of a literal is compatible with its lexical form, whereas 0 indicates that none are. | [Metric code](./metricsCode/compatibleDatatypeMetric.py)|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata. | The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationFormatsMetric.py)|
| Valid format metric[^1] | This metric identifies whether the declared serialisation formats are valid and conform to recognised RDF syntax specifications.| The result is True if the formats are valid, and False otherwise.|[Metric code](./metricsCode/validFormatMetric.py)|

**Formulas**
- Compatible datatype
$$
\mathrm{Metric}(G) = \frac{|ValidLiterals(G)|}{|Literals(G)|}
$$
- Different serialisation formats
$$
\mathrm{Metric}(G) = \{\, f \in ValidFormats \;\mid\; f \text{ is declared in the metadata of } G \,\}
$$
- Valid format metric
$$
\mathrm{Metric}(G) =
\begin{cases}
1, & \text{if } format(G) \in ValidFormats, \\[6pt]
0, & \text{otherwise}.
\end{cases}
$$

### Redundancy  

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Extensional conciseness [^1] | The extensional conciseness metric checks for redundant resources in the assessed graph and thus measures the number of unique instances found in the graph.| The result is a score from 0 to 1, where a value of 0 indicates that the instances found in the graph are uniques.| [Metric code](./metricsCode/extensionalConcisenessMetric.py)|
 
**Formulas**
- Extensional conciseness
$$
\mathrm{Metric}(G) =
\frac{|UniqueInstances(G)|}{|Ind(G)|}
$$

### Interpretability

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph. | [Metric code](./metricsCode/entitiesNoTypeMetric.py)|
| Re-use of existing terms [^1]                | This metric assesses if a graph re-uses relevant terms in a particular domain. In particular, this metric checks if a property or a class (in case the predicate is rdf:type) used in a triple refers to a term in another vocabulary.| The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are.| [Metric code](./metricsCode/reuseTermsMetric.py)|
| Usage of undefined classes and properties [^1] | This metric measures if there are entities in the graph which are not described with ontology terms.| The result is a score from 0 to 1, where a value of 0 indicates that there are no undefined terms in the graph.| [Metric code](./metricsCode/usageUndefinedClassPropMetric.py)|
| Classes per instance metric | Mean number of classes per instance. This metric measure whether an instance has two rdf:type. | The range of the value of this metric is the set of real positive numbers. Values lower than 1 mean that there are instances without any rdf:type in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple rdf:types. | | [Metric code](./metricsCode/classesPerInstanceMetric.py)|
| Instances with multiple types metric | The ratio of instances of more than one type. This metric measure whether an instance has more than one rdf:type.|  The result is a score from 0 to 1, where a value of 0 indicates that there are no instances that have more than one rdf:type in the graph.| [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|

**Formulas**
- Entities with no type metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Classes(i) = \varnothing \}|}{|Ind(G)|}
$$

- Re-use of existing terms
$$
\mathrm{Metric}(G) =
\frac{|ReusedClasses(G)| + |ReusedProperties(G)|}
     {|Classes(G)| + |Properties(G)|}
$$

- Usage of undefined classes and properties
$$
\mathrm{Metric}(G) =
\frac{|UndefClasses(G)| + |UndefProperties(G)|}{|Classes(G)| + |Properties(G)|}
$$

- Classes per instance metric
$$
\mathrm{Metric}(G) =
\frac{\sum_{i \in Ind(G)} |Classes(i)|}{|Ind(G)|}
$$
- Instances with multiple types metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid |Classes(i)| > 1 \}|}{|Ind(G)|}
$$

## Functional adequacy

### Inference

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
|Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. | The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata. | [Metric code](./metricsCode/usedVocabulariesMetric.py)|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph.| [Metric code](./metricsCode/entitiesNoTypeMetric.py)|
| Usage of undefined classes and properties [^1] | This metric measures if there are entities in the graph which are not described with ontology terms. | The result is a score from 0 to 1, where a value of 0 indicates that there are no undefined terms in the graph.| [Metric code](./metricsCode/usageUndefinedClassPropMetric.py)|
| Classes per instance metric | Mean number of classes per instance. This metric measure whether an instance has two rdf:type. | The range of the value of this metric is the set of real positive numbers. Values lower than 1 mean that there are instances without any rdf:type in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple rdf:types. | [Metric code](./metricsCode/classesPerInstanceMetric.py)|
| Instances with multiple types metric | The ratio of instances of more than one type. This metric measure whether an instance has more than one rdf:type. | The result is a score from 0 to 1, where a value of 0 indicates that there are no instances that have more than one rdf:type in the graph.| [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|

**Formulas**
- Indication of used vocabularies
$$
\mathrm{Metric}(G) =
\frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}
$$

- Entities with no type metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Classes(i) = \varnothing \}|}{|Ind(G)|}
$$

- Usage of undefined classes and properties
$$
\mathrm{Metric}(G) =
\frac{|UndefClasses(G)| + |UndefProperties(G)|}{|Classes(G)| + |Properties(G)|}
$$

- Classes per instance metric
$$
\mathrm{Metric}(G) =
\frac{\sum_{i \in Ind(G)} |Classes(i)|}{|Ind(G)|}
$$

- Instances with multiple types metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid |Classes(i)| > 1 \}|}{|Ind(G)|}
$$

### Understandability

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Instances with no description metric [^3]  | The ratio of instances lacking a description in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no instances without description in the graph.| [Metric code](./metricsCode/instancesWithNoDescriptionMetric.py)|
| Instances with no name metric [^3]  | The ratio of instances lacking a name in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no instances without a name in the graph.    | [Metric code](./metricsCode/instancesWithNoNameMetric.py)|                    
| Instances with no synonym metric [^3]  | The ratio of instances lacking a synonym in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no instances without synonym in the graph.  |[Metric code](./metricsCode/instancesWithNoSynonymMetric.py)|
| Descriptions per instance metric [^3]  | This metric accounts for the number of descriptions associated with instances, which can also be provided by using different annotation properties used by the community to include descriptions (rdfs:comment, skos:definition, dcterms:description, etc.). This metric is calculated as the total number of descriptions associated with graph instances divided by the total number of instances in the graph. | The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, every instance has at least one description.  | [Metric code](./metricsCode/descriptionsPerInstanceMetric.py)|
| Names per instance metric [^3]   | This metric accounts for the number of names associated with instances, and uses the list of annotation properties used by the community for names (rdfs:label, skos:prefLabel, foaf:name, etc.). Then, this metric is calculated as the number of names associated with graph instances divided by the total number of instances in the graph.| The range of the value of this metric is the set of real positive numbers. Values lower than one mean that there are instances without any name in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple names; possibly caused by the inclusion of multilingual names or by some design decision.| [Metric code](./metricsCode/namesPerInstanceMetric.py)|
| Synonyms per instance metric [^3]  | This metric accounts for the number of synonyms associated with instances, which can also be provided by using different annotation properties used by the community to include synonyms (oboInOwl:hasExactSynonym, skos:altLabel, iao:0000118, etc.). This metric is calculated as the number of synonyms associated with instances divided by the total number of instances in the graph. | The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, every instance has at least one synonym.  | [Metric code](./metricsCode/synonymsPerInstanceMetric.py)|
| Annotation richness metric [^4]   | Mean number of annotation properties per instances. |The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates, on average, that each instance is characterized by multiple properties. | [Metric code](./metricsCode/annotationRichnessMetric.py)| |
| Indication of used vocabularies [^1]  | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. | The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata.  | [Metric code](./metricsCode/usedVocabulariesMetric.py)|

**Formulas**
- Instances with no description metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Descriptions(i) = \varnothing \}|}{|Ind(G)|}
$$
- Instances with no name metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Names(i) = \varnothing \}|}{|Ind(G)|}
$$
- Instances with no synonym metric
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Synonyms(i) = \varnothing \}|}{|Ind(G)|}
$$
- Descriptions per instance metric
$$
\mathrm{Metric}(G)\;=\;\frac{\sum_{i\in Ind(G)}\mathrm{Decriptions}(i)}{|Ind(G)|}
$$
- Names per instance metric
$$
\mathrm{Metric}(G)\;=\;\frac{\sum_{i\in Ind(G)}\mathrm{Names}(i)}{|Ind(G)|}
$$
- Synonyms per instance metric
$$
\mathrm{Metric}(G)\;=\;\frac{\sum_{i\in Ind(G)}\mathrm{Synonyms}(i)}{|Ind(G)|}
$$

- Annotation richness metric
$$
\mathrm{Metric}(G)\;=\;\frac{\sum_{i\in Ind(G)}\mathrm{AP}(i)}{|Ind(G)|}
$$
- Indication of used vocabularies
$$
\mathrm{Metric}(G) =
\frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}
$$

### Trustworthiness

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Evidence metric | This metric verifies whether graph’s assertions have terms for capturing evidence. | The result is a score from 0 to 1, where a value of 1 indicates that all triples have evidence, whereas 0 indicates that none are.  | [Metric code](./metricsCode/evidenceMetric.py)|
| Evidence codes metric | This metric verifies whether graph’s assertions have terms for capturing evidence.| The result is a score from 0 to 1, where a value of 1 indicates that, on average, every triple has at least one evidence URI, whereas 0 indicates that none are. |[Metric code](./metricsCode/evidenceCodesMetric.py)|
| Traceability of the data [^1]   | This metric checks whether each resource has provenance information related to the origin of data.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.  |[Metric code](./metricsCode/traceabilityMetric.py)|

**Formulas**
- Evidence metric
$$
\mathrm{Metric}(G)\;=\;\frac{\sum_{i\in Ind(G)}\mathrm{Evidence}(i)}{|Ind(G)|}
$$
- Evidence codes metric
$$
\mathrm{Metric}(G)\;=\;\frac{\sum_{i\in Ind(G)}\mathrm{EvidenceCodes}(i)}{|Ind(G)|}
$$

- Traceability of the data
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Provenance(i) \neq \varnothing \}|}{|Ind(G)|}
$$

### Provenance
 
| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.  | [Metric code](./metricsCode/basicProvenanceMetric.py)|
| Traceability of the data [^1]  | This metric checks whether each resource has provenance information related to the origin of data.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information. | [Metric code](./metricsCode/traceabilityMetric.py)|

**Formulas**
- Provision of basic provenance information 
$$
\mathrm{Metric_{ProvBasic}}(G) =
\frac{|ProvProps(G)|}{|BasicProvProps|}
$$
- Traceability of the data
$$
\mathrm{Metric}(G) =
\frac{|\{ i \in Ind(G) \mid Provenance(i) \neq \varnothing \}|}{|Ind(G)|}
$$


### Clustering  

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph. | [Metric code](./metricsCode/entitiesNoTypeMetric.py)|
| Relations per node metric | Average number of relations per graph node. | The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, that each node has multiple relations. | [Metric code](./metricsCode/relationsPerNodeMetric.py)|
| Synonyms per instance metric [^3]   | This metric accounts for the number of synonyms associated with instances, which can also be provided by using different annotation properties used by the community to include synonyms (oboInOwl:hasExactSynonym, skos:altLabel, iao:0000118, etc.). This metric is calculated as the number of synonyms associated with instances divided by the total number of instances in the graph. | The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, every instance has at least one synonym.  | [Metric code](./metricsCode/synonymsPerInstanceMetric.py)|
| Usage of undefined classes and properties [^1] | This metric measures if there are entities in the graph which are not described with ontology terms. | The result is a score from 0 to 1, where a value of 0 indicates that there are no undefined terms in the graph.| [Metric code](./metricsCode/usageUndefinedClassPropMetric.py)|
| Classes per instance metric | Mean number of classes per instance. This metric measure whether an instance has two rdf:type. | The range of the value of this metric is the set of real positive numbers. Values lower than 1 mean that there are instances without any rdf:type in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple rdf:types. | [Metric code](./metricsCode/classesPerInstanceMetric.py)|
| Instances with multiple types metric | The ratio of instances of more than one type. This metric measure whether an instance has more than one rdf:type. | The result is a score from 0 to 1, where a value of 0 indicates that there are no instances that have more than one rdf:type in the graph.| [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|



## Compatibility
### Interoperability


| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Re-use of existing terms [^1]   | This metric   assesses if a graph re-uses relevant terms in a particular domain. In   particular, this metric checks if a property or a class (in case the   predicate is rdf:type) used in a triple refers to a term in another vocabulary.| The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are. | [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|
|  Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. |The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata.| [Metric code](./metricsCode/usedVocabulariesMetric.py)|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata.| The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationMetric.py)|



## Transferability
### Versatility

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata.|  The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationMetric.py)|
| Usage of multiple languages [^1]     | This metric checks the number of languages a graph supports.| The result is a score from 0 to 1, where a value of 1 indicates that all the labels have language tags, whereas 0 indicates that none are.   | [Metric code](./metricsCode/multipleLanguagesMetric.py)|


## Operability
### Licensing

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Machine-readable license [^1] | The aim of this metric is to check if a dataset has a valid machine-readable license.| The result is True if a valid machine-readable license is found, False otherwise.  | [Metric code](./metricsCode/machineLicenseMetric.py)|
| Human-readable license [^1]   | Verifies whether a human-readable text, stating the licensing model attributed to the resource, has been provided as part of the graph. |The result is True if a valid human-readable license description is found, False otherwise.  | [Metric code](./metricsCode/humanLicenseMetric.py)|


## Reliability
### Accessibility

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Dereferenceability of the URI [^1]    | The aim of this metric is to check the number of valid dereferenceable URIs used in a graph.| The result is a score from 0 to 1, where a value of 1 indicates that all the URIs are dereferenceables, whereas 0 indicates that none are.  | [Metric code](./metricsCode/dereferenceabilityMetric.py)|
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.   | [Metric code](./metricsCode/basicProvenanceMetric.py)|
| Traceability of the data [^1]   | This metric checks whether each resource has provenance information related to the origin of data. |The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.  | [Metric code](./metricsCode/traceabilityDataMetric.py)|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata. | The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationFormatsMetric.py)|


## Maintainability
### Reusability


| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Re-use of existing terms [^1]  | This metric   assesses if a graph re-uses relevant terms in a particular domain. In   particular, this metric checks if a property or a class (in case the   predicate is rdf:type) used in a triple refers to a term in another   vocabulary.| The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are.| [Metric code](./metricsCode/reuseTermsMetric.py)|
| Machine-readable license [^1] | The aim of this metric is to check if a dataset has a valid machine-readable license.| The result is True if a valid machine-readable license is found, False otherwise.   | [Metric code](./metricsCode/machineLicenseMetric.py)|
| Human-readable license [^1]   | Verifies whether a human-readable text, stating the licensing model attributed to the resource, has been provided as part of the graph.| The result is True if a valid human-readable license description is found, False otherwise.   | [Metric code](./metricsCode/humanLicenseMetric.py)|
| Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric.| The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata. | [Metric code](./metricsCode/usedVocabulariesMetric.py)|
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset. | The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.  | [Metric code](./metricsCode/basicProvenanceMetric.py)|
| Traceability of the data [^1]  | This metric checks whether each resource has provenance information related to the origin of data. |The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.  | [Metric code](./metricsCode/traceabilityDataMetric.py)|






[^1]: Modified from: Debattista, J., Lange, C., Auer, S., & Cortis, D. (2018). Evaluating the quality of the LOD cloud: An empirical investigation. Semantic Web, 9(6), 859-901. https://doi.org/10.3233/SW-180306
[^2]: Zaveri, A., Rula, A., Maurino, A., Pietrobon, R., Lehmann, J., & Auer, S. (2016). Quality assessment for Linked Data: A Survey. Semantic Web, 7(1), 63-93.https://doi.org/10.3233/SW-150175
[^3]: Modified from: Abad-Navarro, F., Martínez-Costa, C., & Fernández-Breis, J. T. (2023). HURON: A Quantitative Framework for Assessing Human Readability in Ontologies. IEEE Access, 11, 101833-101851. IEEE Access. https://doi.org/10.1109/ACCESS.2023.3316512
[^4]: Modified from: Duque-Ramos, A., Fernández-Breis, J. T., Stevens, R., & Aussenac-Gilles, N. (2011). OQuaRE: A SQuaRE-based Approach for Evaluating the Quality of Ontologies. Journal of Research and Practice in Information Technology, 43(2).

