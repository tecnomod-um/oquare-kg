# The OQuaRE KG quality metrics

A subcharacteristic comprises at least one or more quality metrics which are, in turn, grouped into characteristics.


## Structural
### Formalisation

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
|  Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric.| The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata.| [Metric code](./metricsCode/usedVocabulariesMetric.py)|

### Formula

**Indication of used vocabularies**

$$\mathrm{Metric}(G) = \frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}$$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $Vocabularies(G)$: the set of distinct external vocabularies (namespaces) from which the classes and properties in the graph are reused.


### Structural accuracy

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Usage of deprecated classes or properties [^1] | This metric checks whether deprecated terms are used in a graph. More specifically, all used classes and properties are checked if they are members of owl:DeprecatedClass or owl:DeprecatedProperty respectively.  | The result is a score from 0 to 1, where a value of 0 indicates that there are no deprecated terms in the graph.|[Metric code](./metricsCode/deprecatedClassPropMetric.py)|
| Misused OWL datatype or object properties [^1] | This quality indicator assesses a graph’s statements for the correct usage of the predicate in terms the owl:DatatypeProperty and owl:ObjectProperty axioms. Therefore, this metric detects “erroneous” triples where a data value (literal) object is attached to an owl:ObjectProperty, and an entity (individual) to an owl:DatatypeProperty.  | The result is a score from 0 to 1, where a value of 0 indicates that there are no misused properties in the graph.| [Metric code](./metricsCode/misusedDatatypeObjPropMetric.py)|
| Misplaced classes or properties [^1]           | The metric assesses the graph’s statements to check the correct usage of classes and properties. More specifically, this quality indicator checks if the assessed graph has defined classes placed in the triple’s predicate and defined properties in the object position. | The result is a score from 0 to 1, where a value of 0 indicates that there are no misplaced terms in the graph.| [Metric code](./metricsCode/misplacedClassPropMetric.py)|

### Formulas

**Usage of deprecated classes or properties**

$$ \mathrm{Metric}(G) = \frac{|DepClasses(G)| + |DepProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $DepClasses(G)$: the subset of $Classes(G)$ that are explicitly deprecated according to their ontology or vocabulary definition.
- $DepProperties(G)$: the subset of $Properties(G)$ that are explicitly deprecated according to their ontology or vocabulary definition.

**Misused OWL datatype or object properties**

$$ \mathrm{Metric}(G) = \frac{|MisusedDP(G)| + |MisusedOP(G)|}{|G|} $$

where:
- $∣G∣$: the total number of triples in $G$.
- $MisusedDP(G)$: the subset of triples in which a datatype property is misused, e.g., linked to an individual instead of a literal.
- $MisusedOP(G)$: the subset of triples in which an object property is misused, e.g., pointing to a literal instead of an individual.

**Misplaced classes or properties**

$$ \mathrm{Metric}(G) = \frac{|MisplacedClasses(G)| + |MisplacedPropertie (G)|}{|G|} $$

where:
- $∣G∣$: the total number of triples in $G$.
- $MisplacedClasses(G)$: the subset of triples in which a class is used incorrectly, e.g., appearing in the position of a predicate where it does not belong.
- $MisplacedProperties(G)$: the subset of triples in which a property is misused, treated as a class instead of as a predicate.



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

### Formulas

**Misused OWL datatype or object properties**

$$ \mathrm{Metric}(G) = \frac{|MisusedDP(G)| + |MisusedOP(G)|}{|G|} $$

where:
- $∣G∣$: the total number of triples in $G$.
- $MisusedDP(G)$: the subset of triples in which a datatype property is misused, e.g., linked to an individual instead of a literal.
- $MisusedOP(G)$: the subset of triples in which an object property is misused, e.g., pointing to a literal instead of an individual.

**Misplaced classes or properties**

$$ \mathrm{Metric}(G) = \frac{|MisplacedClasses(G)| + |MisplacedPropertie (G)|}{|G|} $$

where:
- $∣G∣$: the total number of triples in $G$.
- $MisplacedClasses(G)$: the subset of triples in which a class is used incorrectly, e.g., appearing in the position of a predicate where it does not belong.
- $MisplacedProperties(G)$: the subset of triples in which a property is misused, treated as a class instead of as a predicate.

**Compatible datatype**

$$ \mathrm{Metric}(G) = \frac{|ValidLiterals(G)|}{|Literals(G)|} $$

where:
- $Literals(G)$: the set of all literal values used in the graph $G$.
- $ValidLiterals(G)$: the subset of $Literals(G)$ that are well-formed and valid.

**Classes per instance metric**

$$\mathrm{Metric}(G) = \frac{\sum_{i \in Ind(G)} |Classes(i)|}{|Ind(G)|}$$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $∣Classes(i)∣$: the number of classes associated with instance $i$.
- The numerator $∑i∈Ind(G)∣Classes(i)∣$ counts the total number of class assignments across all instances.


**Instances with multiple types metric**

$$\mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid |Classes(i)| > 1 \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- The condition $∣Classes(i)∣>1$ means that the instance $i$ is assigned to more than one class.

**Usage of undefined classes and properties**

$$\mathrm{Metric}(G) = \frac{|UndefClasses(G)| + |UndefProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $UndefClasses(G)$: the subset of $Classes(G)$ that are undefined, i.e., classes used in the graph but not formally defined in any accessible vocabulary or ontology.
- $UndefProperties(G)$: the subset of $Properties(G)$ that are undefined, i.e., properties used in the graph but not formally defined in any accessible vocabulary or ontology.

**Entities with no type metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Classes(i) = \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- ${i∈Ind(G)∣Classes(i)=∅}$: the subset of instances that have no associated class.

### Syntactic validity

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Compatible datatype [^1] | This quality indicator assesses the lexical form of the data values against the data type attached with the literal itself. | The result is a score from 0 to 1, where a value of 1 indicates that the datatype of a literal is compatible with its lexical form, whereas 0 indicates that none are. | [Metric code](./metricsCode/compatibleDatatypeMetric.py)|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata. | The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationFormatsMetric.py)|
| Valid format metric[^1] | This metric identifies whether the declared serialisation formats are valid and conform to recognised RDF syntax specifications.| The result is True if the formats are valid, and False otherwise.|[Metric code](./metricsCode/validFormatMetric.py)|

### Formulas

**Compatible datatype**

$$ \mathrm{Metric}(G) = \frac{|ValidLiterals(G)|}{|Literals(G)|} $$

where:
- $Literals(G)$: the set of all literal values used in the graph $G$.
- $ValidLiterals(G)$: the subset of $Literals(G)$ that are well-formed and valid.

**Different serialisation formats**

$$ \mathrm{Metric}(G) = \{\, f \in ValidFormats \;\mid\; f \text{ is declared in the metadata of } G \,\} $$

where:
- $f$: a serialization format.
- $ValidFormats$: set of accepted RDF serialisations (e.g. Turtle, RDF/XML, JSON-LD, N-Triples, N-Quads, TriG).

**Valid format metric**

$$
\mathrm{Metric}(G) =
\begin{cases}
1, & \text{if } format(G) \in ValidFormats, \\ \\
0, & \text{otherwise}.
\end{cases}
$$

where:
- $format(G)$: function that returns the format in which graph $G$ is serialised (e.g. Turtle, RDF/XML, JSON-LD).
- $ValidFormats$: set of accepted RDF serialisations (e.g. Turtle, RDF/XML, JSON-LD, N-Triples, N-Quads, TriG).

### Redundancy  

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Extensional conciseness [^1] | The extensional conciseness metric checks for redundant resources in the assessed graph and thus measures the number of unique instances found in the graph.| The result is a score from 0 to 1, where a value of 0 indicates that the instances found in the graph are uniques.| [Metric code](./metricsCode/extensionalConcisenessMetric.py)|
 
### Formula

**Extensional conciseness**

$$ \mathrm{Metric}(G) = \frac{|UniqueInstances(G)|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $UniqueInstances(G)$: the subset of instances in $G$ that are not duplicates, i.e., they have distinct descriptions and are not semantically equivalent to other instances.

### Interpretability

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph. | [Metric code](./metricsCode/entitiesNoTypeMetric.py)|
| Re-use of existing terms [^1]                | This metric assesses if a graph re-uses relevant terms in a particular domain. In particular, this metric checks if a property or a class (in case the predicate is rdf:type) used in a triple refers to a term in another vocabulary.| The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are.| [Metric code](./metricsCode/reuseTermsMetric.py)|
| Usage of undefined classes and properties [^1] | This metric measures if there are entities in the graph which are not described with ontology terms.| The result is a score from 0 to 1, where a value of 0 indicates that there are no undefined terms in the graph.| [Metric code](./metricsCode/usageUndefinedClassPropMetric.py)|
| Classes per instance metric | Mean number of classes per instance. This metric measure whether an instance has two rdf:type. | The range of the value of this metric is the set of real positive numbers. Values lower than 1 mean that there are instances without any rdf:type in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple rdf:types. | | [Metric code](./metricsCode/classesPerInstanceMetric.py)|
| Instances with multiple types metric | The ratio of instances of more than one type. This metric measure whether an instance has more than one rdf:type.|  The result is a score from 0 to 1, where a value of 0 indicates that there are no instances that have more than one rdf:type in the graph.| [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|

### Formulas

**Entities with no type metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Classes(i) = \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- ${i∈Ind(G)∣Classes(i)=∅}$: the subset of instances that have no associated class.

**Re-use of existing terms**

$$ \mathrm{Metric}(G) = \frac{|ReusedClasses(G)| + |ReusedProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: set of all classes used in $G$.
- $Properties(G)$: set of all properties used in $G$.
- $ReusedClasses(G)⊆Classes(G)$: subset of classes that are not defined within the graph, but imported from external vocabularies.
- $ReusedProperties(G)⊆Properties(G)$: subset of properties that are not defined within the graph, but imported from external vocabularies.

**Usage of undefined classes and properties**

$$ \mathrm{Metric}(G) = \frac{|UndefClasses(G)| + |UndefProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $UndefClasses(G)$: the subset of $Classes(G)$ that are undefined, i.e., classes used in the graph but not formally defined in any accessible vocabulary or ontology.
- $UndefProperties(G)$: the subset of $Properties(G)$ that are undefined, i.e., properties used in the graph but not formally defined in any accessible vocabulary or ontology.

**Classes per instance metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i \in Ind(G)} |Classes(i)|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $∣Classes(i)∣$: the number of classes associated with instance $i$.
- The numerator $∑i∈Ind(G)∣Classes(i)∣$ counts the total number of class assignments across all instances.

**Instances with multiple types metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid |Classes(i)| > 1 \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- The condition $∣Classes(i)∣>1$ means that the instance $i$ is assigned to more than one class.

## Functional adequacy

### Inference

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
|Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. | The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata. | [Metric code](./metricsCode/usedVocabulariesMetric.py)|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph.| [Metric code](./metricsCode/entitiesNoTypeMetric.py)|
| Usage of undefined classes and properties [^1] | This metric measures if there are entities in the graph which are not described with ontology terms. | The result is a score from 0 to 1, where a value of 0 indicates that there are no undefined terms in the graph.| [Metric code](./metricsCode/usageUndefinedClassPropMetric.py)|
| Classes per instance metric | Mean number of classes per instance. This metric measure whether an instance has two rdf:type. | The range of the value of this metric is the set of real positive numbers. Values lower than 1 mean that there are instances without any rdf:type in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple rdf:types. | [Metric code](./metricsCode/classesPerInstanceMetric.py)|
| Instances with multiple types metric | The ratio of instances of more than one type. This metric measure whether an instance has more than one rdf:type. | The result is a score from 0 to 1, where a value of 0 indicates that there are no instances that have more than one rdf:type in the graph.| [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|

### Formulas

**Indication of used vocabularies**

$$\mathrm{Metric}(G) = \frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}$$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $Vocabularies(G)$: the set of distinct external vocabularies (namespaces) from which the classes and properties in the graph are reused.

**Entities with no type metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Classes(i) = \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- ${i∈Ind(G)∣Classes(i)=∅}$: the subset of instances that have no associated class.

**Usage of undefined classes and properties**

$$ \mathrm{Metric}(G) = \frac{|UndefClasses(G)| + |UndefProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $UndefClasses(G)$: the subset of $Classes(G)$ that are undefined, i.e., classes used in the graph but not formally defined in any accessible vocabulary or ontology.
- $UndefProperties(G)$: the subset of $Properties(G)$ that are undefined, i.e., properties used in the graph but not formally defined in any accessible vocabulary or ontology.

**Classes per instance metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i \in Ind(G)} |Classes(i)|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $∣Classes(i)∣$: the number of classes associated with instance $i$.
- The numerator $∑i∈Ind(G)∣Classes(i)∣$ counts the total number of class assignments across all instances.

**Instances with multiple types metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid |Classes(i)| > 1 \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- The condition $∣Classes(i)∣>1$ means that the instance $i$ is assigned to more than one class.

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

### Formulas

**Instances with no description metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Descriptions(i) = \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Descriptions(i)$: the set of description annotations associated with instance $i$.
- ${i∈Ind(G)∣Descriptions(i)=∅}$: the subset of instances that have no description annotation.

**Instances with no name metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Names(i) = \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Names(i)$: the set of description names associated with instance $i$.
- ${i∈Ind(G)∣Names(i)=∅}$: the subset of instances that have no name annotation.

**Instances with no synonym metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Synonyms(i) = \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Synonyms(i)$: the set of synonym annotations associated with instance $i$.
- ${i∈Ind(G)∣Synonyms(i)=∅}$: the subset of instances that have no synonym annotation.

**Descriptions per instance metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i\in Ind(G)}\mathrm{Decriptions}(i)}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Descriptions(i)$: the number of description annotations (e.g., using description annotation properties) associated with instance $i$.
- The numerator $∑i∈Ind(G)Descriptions(i)$ is the total number of descriptions defined for all instances.

**Names per instance metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i\in Ind(G)}\mathrm{Names}(i)}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Names(i)$: the number of name annotations (e.g., using name annotation properties) associated with instance $i$.
- The numerator $∑i∈Ind(G)Names(i)$ is the total number of names defined for all instances.

**Synonyms per instance metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i\in Ind(G)}\mathrm{Synonyms}(i)}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Synonyms(i)$: the number of synonym annotations (e.g., using synonym annotation properties) associated with instance $i$.
- The numerator $∑i∈Ind(G)Synonyms(i)$ is the total number of synonyms defined for all instances.

**Annotation richness metric**

$$
\mathrm{Metric}(G) = \frac{\sum_{i\in Ind(G)}\mathrm{AP}(i)}{|Ind(G)|}
$$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $AP(i)$: the number of annotation properties (e.g., labels, comments, descriptions, synonyms, etc.) associated with instance $i$.
- The numerator $∑i∈Ind(G)AP(i)$ is the total number of annotation property assertions across all instances.

**Indication of used vocabularies**

$$\mathrm{Metric}(G) = \frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}$$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $Vocabularies(G)$: the set of distinct external vocabularies (namespaces) from which the classes and properties in the graph are reused.

### Trustworthiness

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Evidence metric | This metric verifies whether graph’s assertions have terms for capturing evidence. | The result is a score from 0 to 1, where a value of 1 indicates that all triples have evidence, whereas 0 indicates that none are.  | [Metric code](./metricsCode/evidenceMetric.py)|
| Evidence codes metric | This metric verifies whether graph’s assertions have terms for capturing evidence.| The result is a score from 0 to 1, where a value of 1 indicates that, on average, every triple has at least one evidence URI, whereas 0 indicates that none are. |[Metric code](./metricsCode/evidenceCodesMetric.py)|
| Traceability of the data [^1]   | This metric checks whether each resource has provenance information related to the origin of data.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.  |[Metric code](./metricsCode/traceabilityMetric.py)|

### Formulas
**Evidence metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i\in Ind(G)}\mathrm{Evidence}(i)}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $EvidenceCodes(i)$: the number of evidence codes associated with instance $i$.
- The numerator $∑i∈Ind(G)Evidence(i)$ is the total number of evidence provided across all instances.

**Evidence codes metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i\in Ind(G)}\mathrm{EvidenceCodes}(i)}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $EvidenceCodes(i)$: the number of evidence codes associated with instance $i$.
- The numerator $∑i∈Ind(G)EvidenceCodes(i)$ is the total number of evidence codes provided across all instances.

**Traceability of the data**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Provenance(i) \neq \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: set of instances (individual resources) in graph $G$.
- $Provenance(i)$: set of provenance properties associated with instance $i$.

### Provenance
 
| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.  | [Metric code](./metricsCode/basicProvenanceMetric.py)|
| Traceability of the data [^1]  | This metric checks whether each resource has provenance information related to the origin of data.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information. | [Metric code](./metricsCode/traceabilityMetric.py)|

### Formulas

**Provision of basic provenance information**

$$ \mathrm{Metric}(G) = \frac{|ProvProps(G)|}{|BasicProvProps|} $$

where:
- $BasicProvProps$: set of provenance properties considered basic or minimally required.
- $ProvProps(G)⊆BasicProvProps$: subset of those properties that actually appear in graph $G$.

**Traceability of the data**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Provenance(i) \neq \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: set of instances (individual resources) in graph $G$.
- $Provenance(i)$: set of provenance properties associated with instance $i$.


### Clustering  

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Entities with no type metric | The ratio of nodes lacking rdf:type in the graph. | The result is a score from 0 to 1, where a value of 0 indicates that there are no entities without a type in the graph. | [Metric code](./metricsCode/entitiesNoTypeMetric.py)|
| Relations per node metric | Average number of relations per graph node. | The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, that each node has multiple relations. | [Metric code](./metricsCode/relationsPerNodeMetric.py)|
| Synonyms per instance metric [^3]   | This metric accounts for the number of synonyms associated with instances, which can also be provided by using different annotation properties used by the community to include synonyms (oboInOwl:hasExactSynonym, skos:altLabel, iao:0000118, etc.). This metric is calculated as the number of synonyms associated with instances divided by the total number of instances in the graph. | The range of the value of this metric is the set of real positive numbers, where a value of 1 or greater indicates that, on average, every instance has at least one synonym.  | [Metric code](./metricsCode/synonymsPerInstanceMetric.py)|
| Usage of undefined classes and properties [^1] | This metric measures if there are entities in the graph which are not described with ontology terms. | The result is a score from 0 to 1, where a value of 0 indicates that there are no undefined terms in the graph.| [Metric code](./metricsCode/usageUndefinedClassPropMetric.py)|
| Classes per instance metric | Mean number of classes per instance. This metric measure whether an instance has two rdf:type. | The range of the value of this metric is the set of real positive numbers. Values lower than 1 mean that there are instances without any rdf:type in the graph. Contrariwise, a value greater than 1 indicates that there are instances with multiple rdf:types. | [Metric code](./metricsCode/classesPerInstanceMetric.py)|
| Instances with multiple types metric | The ratio of instances of more than one type. This metric measure whether an instance has more than one rdf:type. | The result is a score from 0 to 1, where a value of 0 indicates that there are no instances that have more than one rdf:type in the graph.| [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|

### Formulas
**Entities with no type metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Classes(i) = \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- ${i∈Ind(G)∣Classes(i)=∅}$: the subset of instances that have no associated class.

**Relations per node metric**

$$ \mathrm{Metric}(G) = \frac{|P(G)|}{|N(G)|} $$

where:
- $N(G)$: set of nodes in the graph
- $P(G)$: set of relations (edges) in the graph, i.e., the total number of RDF properties connecting nodes.

**Synonyms per instance metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i\in Ind(G)}\mathrm{Synonyms}(i)}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph $G$.
- $Synonyms(i)$: the number of synonym annotations (e.g., using synonym annotation properties) associated with instance $i$.
- The numerator $∑i∈Ind(G)Synonyms(i)$ is the total number of synonyms defined for all instances.

**Usage of undefined classes and properties**

$$ \mathrm{Metric}(G) = \frac{|UndefClasses(G)| + |UndefProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $UndefClasses(G)$: the subset of $Classes(G)$ that are undefined, i.e., classes used in the graph but not formally defined in any accessible vocabulary or ontology.
- $UndefProperties(G)$: the subset of $Properties(G)$ that are undefined, i.e., properties used in the graph but not formally defined in any accessible vocabulary or ontology.

**Classes per instance metric**

$$ \mathrm{Metric}(G) = \frac{\sum_{i \in Ind(G)} |Classes(i)|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $∣Classes(i)∣$: the number of classes associated with instance $i$.
- The numerator $∑i∈Ind(G)∣Classes(i)∣$ counts the total number of class assignments across all instances.

**Instances with multiple types metric**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid |Classes(i)| > 1 \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: the set of all instances (individuals) in the graph.
- $Classes(i)$: the set of classes to which instance $i$ belongs.
- The condition $∣Classes(i)∣>1$ means that the instance $i$ is assigned to more than one class.



## Compatibility
### Interoperability


| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Re-use of existing terms [^1]   | This metric   assesses if a graph re-uses relevant terms in a particular domain. In   particular, this metric checks if a property or a class (in case the   predicate is rdf:type) used in a triple refers to a term in another vocabulary.| The result is a score from 0 to 1, where a value of 1 indicates that all terms in the graph are reused, whereas 0 indicates that none are. | [Metric code](./metricsCode/instancesWithMultipleTypesMetric.py)|
|  Indication of used vocabularies [^1] | This metric verifies whether the vocabularies used in the graphs, either in the predicate position or in the object position if the predicate is rdf:type, are included in the graph metadata particularly using the recommended void:vocabulary predicate. The vocabularies of RDF, RDFS, and OWL are not considered in this metric. |The result is a score from 0 to 1, where a value of 1 denotes that all vocabularies used are declared, whereas 0 indicates absence of this metadata.| [Metric code](./metricsCode/usedVocabulariesMetric.py)|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata.| The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationMetric.py)|

### Formulas
**Re-use of existing terms**

$$ \mathrm{Metric}(G) = \frac{|ReusedClasses(G)| + |ReusedProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: set of all classes used in $G$.
- $Properties(G)$: set of all properties used in $G$.
- $ReusedClasses(G)⊆Classes(G)$: subset of classes that are not defined within the graph, but imported from external vocabularies.
- $ReusedProperties(G)⊆Properties(G)$: subset of properties that are not defined within the graph, but imported from external vocabularies.

**Indication of used vocabularies**

$$\mathrm{Metric}(G) = \frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}$$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $Vocabularies(G)$: the set of distinct external vocabularies (namespaces) from which the classes and properties in the graph are reused.

**Different serialisation formats**

$$ \mathrm{Metric}(G) = \{\, f \in ValidFormats \;\mid\; f \text{ is declared in the metadata of } G \,\} $$

where:
- $ValidFormats$: set of accepted RDF serialisations (e.g. Turtle, RDF/XML, JSON-LD, N-Triples, N-Quads, TriG).

## Transferability
### Versatility

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata.|  The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationMetric.py)|
| Usage of multiple languages [^1]     | This metric checks the number of languages a graph supports.| The result is a score from 0 to 1, where a value of 1 indicates that all the labels have language tags, whereas 0 indicates that none are.   | [Metric code](./metricsCode/multipleLanguagesMetric.py)|

### Formulas

**Different serialisation formats**

$$ \mathrm{Metric}(G) = \{\, f \in ValidFormats \;\mid\; f \text{ is declared in the metadata of } G \,\} $$

where:
- $ValidFormats$: set of accepted RDF serialisations (e.g. Turtle, RDF/XML, JSON-LD, N-Triples, N-Quads, TriG).

**Usage of multiple languages**

$$
\mathrm{Metric}(G) = \frac{|\{ lit \in AP(G) \mid hasLangTag(lit) \}|}{|AP(G)|}
$$


where:
- $AP(G)$: set of literals associated with annotation properties.

- $hasLangTag(lit)$: predicate indicating whether the literal has an associated language tag.

## Operability
### Licensing

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Machine-readable license [^1] | The aim of this metric is to check if a dataset has a valid machine-readable license.| The result is True if a valid machine-readable license is found, False otherwise.  | [Metric code](./metricsCode/machineLicenseMetric.py)|
| Human-readable license [^1]   | Verifies whether a human-readable text, stating the licensing model attributed to the resource, has been provided as part of the graph. |The result is True if a valid human-readable license description is found, False otherwise.  | [Metric code](./metricsCode/humanLicenseMetric.py)|

### Formulas
**Machine-readable license**

$$ \mathrm{Metric}(G) =
\begin{cases}
1, & \text{if } mLicense(G) \text{ is True}, \\ \\
0, & \text{if } mLicense(G) \text{ is False}.
\end{cases}
$$

where:
- $mLicense(G)$: function that returns if a machine readable license is declared in the graph $G$.

**Human-readable license**

$$
\mathrm{Metric}(G) =
\begin{cases}
1, & \text{if } hLicense(G) \text{ is True}, \\ \\
0, & \text{if } hLicense(G) \text{ is False}.
\end{cases}
$$

where:
- $hLicense(G)$: function that returns if a human readable license is declared in the graph $G$.

## Reliability
### Accessibility

| **Metric**               | **Definition**           | **Score**              | **Code** |
|--------------------------|--------------------------|------------------------|----------|
| Dereferenceability of the URI [^1]    | The aim of this metric is to check the number of valid dereferenceable URIs used in a graph.| The result is a score from 0 to 1, where a value of 1 indicates that all the URIs are dereferenceables, whereas 0 indicates that none are.  | [Metric code](./metricsCode/dereferenceabilityMetric.py)|
| Provision of basic provenance information [^1] | This metric search for triples with the predicates dc:creator or dc:publisher in the dataset having a type void:Dataset or dcat:Dataset.| The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this metadata.   | [Metric code](./metricsCode/basicProvenanceMetric.py)|
| Traceability of the data [^1]   | This metric checks whether each resource has provenance information related to the origin of data. |The result is a score from 0 to 1, where a value of 1 denotes full compliance, whereas 0 indicates absence of this information.  | [Metric code](./metricsCode/traceabilityDataMetric.py)|
| Different serialisation formats [^1] | This metric checks whether a graph has multiple serialisation formats defined in its metadata. | The result is a set of valid serialization formats, or an empty set if none are found.| [Metric code](./metricsCode/differentSerializationFormatsMetric.py)|

### Formulas
**Dereferenceability of the URI**

$$ \mathrm{Metric}(G) = \frac{|\{ u \in URI(G) \mid dereferenceable(u) \}|}{|URI(G)|} $$

where:
- $URI(G)$: set of all URIs used in graph $G$.
- $dereferenceable(u)$: predicate that is true if URI 
u returns a valid response (e.g., HTTP code 200 and RDF/HTML content) when attempting to resolve it.

**Traceability of the data**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Provenance(i) \neq \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: set of instances (individual resources) in graph $G$.
- $Provenance(i)$: set of provenance properties associated with instance $i$.

**Different serialisation formats**

$$ \mathrm{Metric}(G) = \{\, f \in ValidFormats \;\mid\; f \text{ is declared in the metadata of } G \,\} $$

where:
- $ValidFormats$: set of accepted RDF serialisations (e.g. Turtle, RDF/XML, JSON-LD, N-Triples, N-Quads, TriG).

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

### Formulas
**Re-use of existing terms**

$$ \mathrm{Metric}(G) = \frac{|ReusedClasses(G)| + |ReusedProperties(G)|}{|Classes(G)| + |Properties(G)|} $$

where:
- $Classes(G)$: set of all classes used in $G$.
- $Properties(G)$: set of all properties used in $G$.
- $ReusedClasses(G)⊆Classes(G)$: subset of classes that are not defined within the graph, but imported from external vocabularies.
- $ReusedProperties(G)⊆Properties(G)$: subset of properties that are not defined within the graph, but imported from external vocabularies.

**Machine-readable license**

$$
\mathrm{Metric}(G) =
\begin{cases}
1, & \text{if } mLicense(G) \text{ is True}, \\ \\
0, & \text{if } mLicense(G) \text{ is False}.
\end{cases}
$$

where:
- $mLicense(G)$: function that returns if a machine readable license is declared in the graph $G$.

**Human-readable license**

$$
\mathrm{Metric}(G) =
\begin{cases}
1, & \text{if } hLicense(G) \text{ is True}, \\ \\
0, & \text{if } hLicense(G) \text{ is False}.
\end{cases}
$$

where:
- $hLicense(G)$: function that returns if a human readable license is declared in the graph $G$.

**Indication of used vocabularies**

$$\mathrm{Metric}(G) = \frac{|Vocabularies(G)|}{|Classes(G)| + |Properties(G)|}$$

where:
- $Classes(G)$: the set of all classes used in the graph $G$.
- $Properties(G)$: the set of all properties used in the graph $G$.
- $Vocabularies(G)$: the set of distinct external vocabularies (namespaces) from which the classes and properties in the graph are reused.

**Provision of basic provenance information**

$$ \mathrm{Metric}(G) = \frac{|ProvProps(G)|}{|BasicProvProps|} $$

where:
- $BasicProvProps$: set of provenance properties considered basic or minimally required.
- $ProvProps(G)⊆BasicProvProps$: subset of those properties that actually appear in graph $G$.

**Traceability of the data**

$$ \mathrm{Metric}(G) = \frac{|\{ i \in Ind(G) \mid Provenance(i) \neq \varnothing \}|}{|Ind(G)|} $$

where:
- $Ind(G)$: set of instances (individual resources) in graph $G$.
- $Provenance(i)$: set of provenance properties associated with instance $i$.




[^1]: Modified from: Debattista, J., Lange, C., Auer, S., & Cortis, D. (2018). Evaluating the quality of the LOD cloud: An empirical investigation. Semantic Web, 9(6), 859-901. https://doi.org/10.3233/SW-180306
[^2]: Zaveri, A., Rula, A., Maurino, A., Pietrobon, R., Lehmann, J., & Auer, S. (2016). Quality assessment for Linked Data: A Survey. Semantic Web, 7(1), 63-93.https://doi.org/10.3233/SW-150175
[^3]: Modified from: Abad-Navarro, F., Martínez-Costa, C., & Fernández-Breis, J. T. (2023). HURON: A Quantitative Framework for Assessing Human Readability in Ontologies. IEEE Access, 11, 101833-101851. IEEE Access. https://doi.org/10.1109/ACCESS.2023.3316512
[^4]: Modified from: Duque-Ramos, A., Fernández-Breis, J. T., Stevens, R., & Aussenac-Gilles, N. (2011). OQuaRE: A SQuaRE-based Approach for Evaluating the Quality of Ontologies. Journal of Research and Practice in Information Technology, 43(2).

