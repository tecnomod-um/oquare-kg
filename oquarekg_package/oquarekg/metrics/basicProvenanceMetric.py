from rdflib import Graph, URIRef, DCTERMS, Literal
from .metric import Metric
from ..predicates import BASIC_PROV_PREDICATES

class BasicProvenanceMetric(Metric):
    def calculate_metric(self, graph: Graph) -> float:
        """
        Calculates the percentage of provenance and authoring predicates used in a RDF graph.

        Args:
            graph: RDF graph.

        Returns:
            The ratio of predicates used in the graph. Best = 1
        """

        # basic_prov_predicates = {
        #     DCTERMS.creator,
        #     DCTERMS.publisher,
        #     URIRef("http://purl.org/pav/providedBy")
        # }
        
        # basic provenance predicates used in the graph
        used_prov_predicates = set()

        for subject, predicate, obj in graph:
            if predicate in BASIC_PROV_PREDICATES:
                used_prov_predicates.add(predicate)

        if len(used_prov_predicates) > 0:
            basic_prov_metric = (len(used_prov_predicates) / len(BASIC_PROV_PREDICATES))
        else:
            basic_prov_metric = 0.0

        return basic_prov_metric

  
    def get_metric_name(self):
        return 'Basic provenance metric'