from rdflib import Graph, URIRef
import requests
from .metric import Metric

class DereferenceabilityMetric(Metric):
    def calculate_metric(self, graph:Graph) -> float:
        """
        Calculates the ratio of dereferenceable URIs in a RDF graph.

        Args:
            graph: RDF graph

        Returns:
            The ratio of dereferenceable URIs in the graph. Best = 1
            Returns 0 if no URIs are found in the graph.
        """
        uris = set()
        for s, p, o in graph:
            if isinstance(s, URIRef):
                uris.add(str(s))
            if isinstance(p, URIRef):
                uris.add(str(p))
            if isinstance(o, URIRef):
                uris.add(str(o))


        total_uris = len(uris)
        if total_uris == 0:
            return 0.0


        dereferenceable_uris_count = 0
        timeout = 1  # Timeout in seconds for the HTTP request

        for uri in uris:
            try:
                response = requests.head(uri, timeout=timeout)  # Use HEAD for a lighter request
                response.raise_for_status()  # Raise an exception for bad HTTP status codes (4xx or 5xx)
                dereferenceable_uris_count += 1
            except requests.exceptions.RequestException:
                pass  # Ignore dereferencing errors


        if total_uris > 0:
            dereferenceable_ratio = dereferenceable_uris_count / total_uris
        else:
            dereferenceable_ratio = 0

        return dereferenceable_ratio
    
    def get_metric_name(self):
        return 'Dereferenceable uris metric'