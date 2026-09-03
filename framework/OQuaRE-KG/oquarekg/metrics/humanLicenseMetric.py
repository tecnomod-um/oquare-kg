from rdflib import Graph, URIRef, Namespace, Literal, DCTERMS, RDFS
from .metric import Metric
from ..predicates import LICENSE_PREDICATES

class HumanReadableLicenseMetric(Metric):

    def calculate_metric(self, graph:Graph) -> bool:
        """
        Validates human-readable license descriptions in a graph.

        Args:
            graph: RDF graph.

        Returns:
            True if a valid human-readable license description is found, False otherwise. Best = true
        """
    
        # license_predicates = [
        #     DCTERMS.license,
        #     RDFS.comment,
        #     DCTERMS.description,
        #     RDFS.label,
        #     URIRef("https://schema.org/license"),
        # ]

        for predicate in LICENSE_PREDICATES:
            for subject, predicate, obj in graph.triples((None, predicate, None)):
                if isinstance(obj, URIRef):
                    return True  # Found a URI that likely links to a license
                if isinstance(obj, Literal) and "license" in obj.lower():
                    return True  # Found a text mentioning license

        return False

    def get_metric_name(self):
        return 'Human readable license metric'