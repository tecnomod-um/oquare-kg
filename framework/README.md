# The OQuaRE KG framework

## Introduction
Over the past few years, large amounts of data are being produced, distributed across a multitude of knowledge bases and represented in a variety of formats. The Semantic Web aims to represent data in such a way that it can be understood and processed automatically. To achieve this, it relies on technologies such as OWL for knowledge representation through ontologies, RDF for resource description, and SPARQL as a query language. Using ontologies as a schema, data can be semantically represented in the form of knowledge graphs. Scientific data published using these technologies must meet a number of quality requirements, such as the FAIR principles [^2], to enable it to be reused and understood by a machine.
OQuaRE-KG is a framework based on OQuaRE, a quality framework for ontologies. The purpose of OQuaRE KG is to provide the basis for the creation of metrics that guarantee the quality of knowledge bases.

## Global overview
OQuaRE-KG is a quality framework for assessing knowledge graphs, based on OQuaRE [^1]. It defines key characteristics and subcharacteristics essential for evaluating knowledge graph quality. Each characteristic is linked to specific subcharacteristics that contribute to the quality assessment process. Additionally, each subcharacteristic is measured using one or more quality metrics.

[^1]: Duque-Ramos, A., Fernández-Breis, J.T., Stevens, R., & Aussenac-Gilles, N. (2011). OQuaRE: A SQuaRE-based approach for evaluating the quality of ontologies. Journal of Research and Practice in Information Technology, 43, 159-173.
[^2]: Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Bouwman, J. (2016). The FAIR Guiding Principles for scientific data management and stewardship. Scientific data, 3.

The following table shows the characteristics and their associated subcharacteristics:

| **Characteristics** | **Subcharacteristics**                                      |
|---------------------|-------------------------------------------------------------|
|Structural           |Formalisation, structural accuracy, consistency, syntactic validity, redundancy, interpretability |
|Functional adequacy  |Inference, understandability, trustworthiness, provenance, clustering |
|Compatibility        |Interoperability                     |
|Transferability      |Versatility                          |
|Operability          |Licensing                            |
|Reliability          |Accessibility                        |
|Maintainability      |Reusability                          |


The following diagram shows the characteristics and their associated subcharacteristics:

![The following diagram shows the characteristics and their associated subcharacteristics:](https://github.com/tecnomod-um/oquare-kg/blob/main/framework/images/OquareKG.png)


An example of quality assessment in a knowledge graph with oquare:

![An example of quality assessment in a knowledge graph with oquare:](https://github.com/tecnomod-um/oquare-kg/blob/main/framework/images/ExampleOquareKG.png)


## Static Scaling

OQuaRE-KG scales the values of the metrics into quality scores in the range [1,5]. Metrics can be classify into three groups based on their range of values:

* Binary value: scaled to 1 or 5.

    | Metric score |    1    |     5    |
    |--------------|---------|----------|
    | Metric value |  false  |   true   |

* Values in the range [0,1] are scaled [1,5] by intervals of 20%.

    - If high values of the metric indicate high quality, then those high values are mapped to the higher scores in the range [1,5].

    | Metric score | 1       | 2          | 3          | 4          | 5        |
    |--------------|---------|------------|------------|------------|----------|
    | Metric value | [0-20]% | (20-40]%   | (40-60]%   | (60-80]%   | >80%     |

    - Otherwise, the high values are mapped onto the lower scores.

    | Metric score | 1       | 2          | 3          | 4          | 5        |
    |--------------|---------|------------|------------|------------|----------|
    | Metric value |   >80%  |  (60-80]%  | (40-60]%   |  (20-40]%  | [0-20]%  |

* Values in other ranges are scaled into [0,1] and then the previous scaling to [1,5] is applied.


Once the quality scores of the metrics have been calculated, the quality scores of the subcharacteristics and characteristics are obtained by averaging the scores of their corresponding associated metrics and subcharacteristics, respectively.


## Details

* [Quality characteristics](characteristics.md)
* [Quality subcharacteristics](subcharacteristics.md)
* [Metrics](metrics.md)
