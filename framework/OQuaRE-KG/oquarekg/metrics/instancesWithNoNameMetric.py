from rdflib import RDF, RDFS, DCTERMS, FOAF, Graph, SKOS, URIRef, DC
from .metric import Metric
from ..predicates import NAME_PREDICATES, TYPE_PREDICATES

class InstancesWithNoNameMetric(Metric):
    def calculate_metric(self, graph: Graph) -> float:
        """
        Calculates the ratio of instances without a name used in a graph.

        Args:
            graph: RDF graph.

        Returns:
            Mean number of instances without a name. Best = 0
        """
    
        instances = set()
        named_instances = set()
        # set of names predicates, add as many as necesary
        # name_predicates = {
        #     RDFS.label,
        #     DCTERMS.title,
        #     DC.title,
        #     FOAF.name,
        #     SKOS.prefLabel,
        #     URIRef("http://purl.obolibrary.org/obo/IAO_0000589"),
        #     URIRef("https://schema.org/name"),
        #     URIRef("http://purl.obolibrary.org/obo/NCIT_P108")
        #     }  

        # Find the instances (rdf:type predicates)
        for subject, predicate, obj in graph:
            if predicate in TYPE_PREDICATES:
                instances.add(subject)
        # Find instances with name
            elif predicate in NAME_PREDICATES:
                named_instances.add(subject)

        # Calculate the ratio of instances without name
        unnamed_count = len(instances - named_instances)
        total_instances = len(instances)

        if unnamed_count > 0:
            without_name = (unnamed_count / total_instances)
        else:
            without_name = 0.0

        return without_name
    
    def get_metric_name(self):
        return 'Instances with no name metric'