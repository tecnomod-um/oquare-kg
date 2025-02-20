# The OQuaRE KG framework

## Introduction
Over the past few years, large amounts of data are being produced, distributed across a multitude of knowledge bases and represented in a variety of formats. The Semantic Web aims to represent data in such a way that it can be understood and processed automatically. To achieve this, it relies on technologies such as OWL for knowledge representation through ontologies, RDF for resource description, and SPARQL as a query language. Using ontologies as a schema, data can be semantically represented in the form of knowledge graphs. Scientific data published using these technologies must meet a number of quality requirements, such as the FAIR principles [^2], to enable it to be reused and understood by a machine.
OquareKG is a framework developed based on Oquare, a quality framework for ontologies. The purpose of OquareKG is to provide the basis for the creation of metrics that guarantee the quality of knowledge bases.

## Global overview
OQuare KG is a quality framework for assessing knowledge graphs, based on OQuaRE [^1]. It defines key characteristics and subcharacteristics essential for evaluating knowledge graph quality. Each characteristic is linked to specific subcharacteristics that contribute to the quality assessment process. Additionally, each subcharacteristic is measured using one or more quality metrics.

[^1] Duque-Ramos, A., Fernández-Breis, J.T., Stevens, R., & Aussenac-Gilles, N. (2011). OQuaRE: A SQuaRE-based approach for evaluating the quality of ontologies. Journal of Research and Practice in Information Technology, 43, 159-173.
[^2] Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Bouwman, J. (2016). The FAIR Guiding Principles for scientific data management and stewardship. Scientific data, 3.

The following table shows the characteristics and their associated subcharacteristics:

| **    Characteristics   ** | **    Subcharacteristics   **                                       |
|----------------------------|---------------------------------------------------------------------|
|     Accessibility          |     Availability,   licensing, clustering                           |
|     Representational       |     Interpretability,   interoperability, versatility               |
|     Structural             |     Completeness,   consistency, syntactic validity, redundancy     |
|     Contextual             |     Understandability,   trustworthiness, provenance, timeliness    |

## Details

* [Quality characteristics](characteristics.md)
* [Quality subcharacteristics](subcharacteristics.md)
* [Metrics](metrics.md)