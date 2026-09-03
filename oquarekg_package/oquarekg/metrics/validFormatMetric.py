from rdflib import Graph, URIRef
from .metric import Metric
from ..predicates import FORMAT_PREDICATES

class ValidFormatMetric(Metric):
    def __init__(self, input_format: str):
        self.input_format = input_format

    def calculate_metric(self, graph: Graph) -> bool:
        """
        Verify that RDF formats declared with void:feature are known and valid.
        
        Args:
            graph: RDF graph.
            input_format: graph formats.

        Returns:
            bool: True if valid formats, False otherwise.
        """
        #void_feature_uri = URIRef("http://rdfs.org/ns/void#feature")
        known_formats = {'xml', 'turtle', 'nt', 'n3', 'json-ld', 'trig', 'nquads'}

        declared_formats = set()
        for subject, predicate, obj in graph:
            if predicate in FORMAT_PREDICATES:
                uri_str = str(obj)
                if '#' in uri_str:
                    format_name = uri_str.split('#')[-1].lower()
                else:
                    format_name = uri_str.split('/')[-1].lower()
                declared_formats.add(format_name)



        if declared_formats:
            # Validate declared format
            for fmt in declared_formats:
                if fmt not in known_formats:
                    return False  # Unknown
                try:
                    graph.serialize(format=fmt)
                except Exception:
                    return False  # Non-serialisable
            return True
        else:
            # If there are not declared formats, verify input format
            #if input_format not in known_formats:
            if self.input_format not in known_formats:
                return False
            try:
                #graph.serialize(format=input_format)
                graph.serialize(format=self.input_format)
                return True
            except Exception:
                return False

    def get_metric_name(self):
        return 'Valid format metric'