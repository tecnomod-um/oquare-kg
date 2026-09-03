from rdflib import SKOS, RDF, Graph, URIRef
from .metric import Metric
from ..predicates import TYPE_PREDICATES, SYNONYM_PREDICATES

class InstancesWithNoSynonymMetric(Metric):
    def calculate_metric(self, graph:Graph) -> float:
        """

        Calculates the ratio of instances without description used in a graph.

        Args:
            graph: RDFlib graph.

        Returns:
            Mean number of instances without synonym. Best = O
        """
        instances = set()
        instances_with_synonym = set()
        # synonym_predicates = {
        #     SKOS.altLabel,
        #     SKOS.hiddenLabel,
        #     URIRef("http://purl.obolibrary.org/obo/hasExactSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasExactSynonym"),
        #     URIRef("http://purl.obolibrary.org/obo/hasRelatedSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasRelatedSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasBroadSynonym"),
        #     URIRef("http://purl.obolibrary.org/obo/hasNarrowSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasNarrowSynonym"),
        #     URIRef("http://purl.obolibrary.org/obo/NCIT_P90"),
        #     URIRef("http://purl.obolibrary.org/obo/IAO_0000118"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_9991119"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_9991118"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_0001847"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_0001886"),
        #     }  # set of synonym predicates, add as many as necesary

        # Find the instances (rdf:type predicates)
        for subject, predicate, obj in graph:
            if predicate in TYPE_PREDICATES:
                instances.add(subject)
        # Find instances with description
            elif predicate in SYNONYM_PREDICATES:
                instances_with_synonym.add(subject)

        # Calculate the ratio of instances without description
        no_synonyms_count = len(instances - instances_with_synonym)
        total_instances = len(instances)

        if no_synonyms_count > 0:
            without_synonyms = no_synonyms_count / total_instances
        else:
            without_synonyms = 0
    
        return without_synonyms
    
    def get_metric_name(self):
        return 'Instances with no synonyms metric'