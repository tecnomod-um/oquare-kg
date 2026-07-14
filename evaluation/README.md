# Evaluation of the OQuaRE KG framework

## Introduction 
This section presents the evaluation of knowledge graphs using the OQuaRE-KG framework. The objective of this analysis is to assess the practical performance of the defined metrics and to emphasise the quality aspects of the selected knowledge graphs.

The evaluation demonstrates the applicability of the framework, as well as the strengths and weaknesses of knowledge graphs, providing insights that support their improvement and practical use.

The subsequent sections are dedicated to the description of the use cases and the presentation of the results of their evaluation.

## Use cases
For the purpose of this evaluation, a set of knowledge graphs from different domains was selected. Each graph represents a distinct scenario, thereby enabling the framework to be tested under diverse conditions.

### Biomedical use cases
Biomedical knowledge graphs are a complex and highly structured use case that integrates data on proteins, genes and diseases.

* Gene regulation knowledge graphs

    Knowledge graphs on the gene regulation domain, with a particular focus on enhancers, which are the most widely studied of the cis-regulatory modules. These sequences were modelled using the CisReg schema, which was also used in BioGateway to integrate data from 25 different sources, modelling information from various biological databases about enhancers and their relations with other entities.

    * Cis-Regulatory modules
        * [Data](https://github.com/juan-mulero/cisregEA)
        * [Evaluation](https://github.com/tecnomod-um/oquare-kg/tree/main/evaluation/results/cisreg)

* The Monarch Knowledge Graph

    The Monarch KG, a biomedical knowledge graph that integrates gene, disease, and phenotype information from 33 heterogeneous data sources, which provides a semantically structured representation of biological entities and their relationships, enabling data integration, semantic reasoning, and biomedical discovery across species.

    * [Data](https://github.com/tecnomod-um/oquare-kg/tree/main/evaluation/monarch)

* At least another one


### Non-biomedical use cases
Non-biomedical knowledge graphs refer to information concerning data related to products, sales and user satisfaction.

* E-commerce knowledge graphs
    * [Data](https://github.com/tecnomod-um/EvaluationGraphAlignmentMethods)
