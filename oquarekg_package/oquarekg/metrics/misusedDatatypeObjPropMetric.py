from rdflib import Graph, URIRef, Literal, OWL
from .metric import Metric
from ..predicates import TYPE_PREDICATES


class MisusedPropertiesMetric(Metric):

    def isObjectProperty(predicate, graph):
        return any((predicate, t, OWL.ObjectProperty) in graph for t in TYPE_PREDICATES) # check similar predicates to rdf:type in TYPE_PREDICATES

    def isDatatypeProperty(predicate, graph):
        return any((predicate, t, OWL.DatatypeProperty) in graph for t in TYPE_PREDICATES) # check similar predicates to rdf:type in TYPE_PREDICATES

    def isLiteral(obj):
        return isinstance(obj, Literal)

    def isIndividual(obj, graph):
        return isinstance(obj, URIRef)

    def calculate_metric(self, graph: Graph) -> float:

        misused_properties = 0
        total_triples = len(graph)

        for subject, predicate, obj in graph:

            if not any((predicate, t, None) in graph for t in TYPE_PREDICATES): # check similar predicates to rdf:type in TYPE_PREDICATES
                continue

            if MisusedPropertiesMetric.isLiteral(obj) and MisusedPropertiesMetric.isObjectProperty(predicate, graph):
                misused_properties += 1

            if MisusedPropertiesMetric.isIndividual(obj, graph) and MisusedPropertiesMetric.isDatatypeProperty(predicate, graph):
                misused_properties += 1

        if total_triples > 0:
            misused_metric = misused_properties / total_triples
        else:
            misused_metric = 0

        return misused_metric

    def get_metric_name(self):
        return 'Misused properties metric'