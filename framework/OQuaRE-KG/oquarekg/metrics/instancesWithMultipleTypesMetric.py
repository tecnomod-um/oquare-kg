from rdflib import Graph, RDF
from .metric import Metric
from ..predicates import TYPE_PREDICATES
class InstancesMultipleTypesMetric(Metric):
    def calculate_metric(self, graph: Graph) -> float:
        """
        Calculates the instances that has two or more rdf:type in a RDF graph.

        Args:
            graph: RDF graph.

        Returns:
            The ratio instances instances with several rdf:types. Best = 0
        """
        one_type = set() # Subjects with one rdf:type
        several_types = set() # Subjects with more than one rdf:type

        for subject, predicate, obj in graph:
            if predicate in TYPE_PREDICATES:
                if subject in one_type:
                    several_types.add(subject)
                else:
                    one_type.add(subject)

        unique_instances = one_type.union(several_types)
        total_instances = len(unique_instances)
        multiple_types = len(several_types)

        if total_instances > 0:
            metric_result = (multiple_types / total_instances)
        else:
            metric_result = 0

        return metric_result
    
    def get_metric_name(self):
        return 'Instances with multiple types metric'