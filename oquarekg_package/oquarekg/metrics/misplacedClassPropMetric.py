from rdflib import Graph, URIRef, RDFS, OWL, Literal, RDF
from .metric import Metric
from ..predicates import TYPE_PREDICATES


class MisplacedClassPropertyMetric(Metric):

    def isClass(uri, graph):
        """Checks if a URI is a class."""
        return any(
            (URIRef(uri), t, OWL.Class) in graph or
            (URIRef(uri), t, RDFS.Class) in graph
            for t in TYPE_PREDICATES
        )

    def isProperty(uri, graph):
        """Checks if a URI is a property."""
        return any(
            (URIRef(uri), t, OWL.ObjectProperty) in graph or
            (URIRef(uri), t, OWL.DatatypeProperty) in graph or
            (URIRef(uri), t, RDF.Property) in graph
            for t in TYPE_PREDICATES
        )

    def calculate_metric(self, graph: Graph) -> float:

        incorrect_class_usage = set()
        incorrect_property_usage = set()
        total_triples = len(graph)

        for subject, predicate, obj in graph:

            if isinstance(subject, URIRef):
                if (
                    MisplacedClassPropertyMetric.isProperty(subject, graph)
                    and not MisplacedClassPropertyMetric.isClass(subject, graph)
                    and obj != OWL.ObjectProperty
                    and obj != OWL.DatatypeProperty
                ):
                    incorrect_property_usage.add(subject)

            if isinstance(predicate, URIRef):
                if (
                    MisplacedClassPropertyMetric.isClass(predicate, graph)
                    and not MisplacedClassPropertyMetric.isProperty(predicate, graph)
                ):
                    incorrect_class_usage.add(predicate)

            if isinstance(obj, URIRef):
                if (
                    MisplacedClassPropertyMetric.isProperty(obj, graph)
                    and not MisplacedClassPropertyMetric.isClass(obj, graph)
                    and obj != OWL.ObjectProperty
                    and obj != OWL.DatatypeProperty
                ):
                    incorrect_property_usage.add(obj)

        if total_triples > 0:
            misplaced_metric = (len(incorrect_class_usage) + len(incorrect_property_usage)) / total_triples
        else:
            misplaced_metric = 0

        return misplaced_metric

    def get_metric_name(self):
        return 'Misplaced class property metric'