from rdflib import Graph, URIRef, RDF, RDFS, OWL, Literal
from .metric import Metric
from ..predicates import TYPE_PREDICATES

class UsageUndefinedTermsMetric(Metric):

    def isClass(uri, graph):
        """Checks if a URI is a class."""
        #return (URIRef(uri), RDF.type, OWL.Class) in graph or (URIRef(uri), RDF.type, RDFS.Class) in graph
        return any((URIRef(uri), t, OWL.Class) in graph or (URIRef(uri), t, RDFS.Class) in graph for t in TYPE_PREDICATES)

    def isProperty(uri, graph):
        """Checks if a URI is a property."""
        # return (URIRef(uri), RDF.type, OWL.ObjectProperty) in graph or \
        #     (URIRef(uri), RDF.type, OWL.DatatypeProperty) in graph or \
        #     (URIRef(uri), RDF.type, RDF.Property) in graph
        return any((URIRef(uri), t, OWL.ObjectProperty) in graph or (URIRef(uri), t, OWL.DatatypeProperty) in graph or 
                   (URIRef(uri), t, RDF.Property) in graph for t in TYPE_PREDICATES)

    def calculate_metric(self, graph: Graph) -> float:
        """
        Calculates the metric value for undefined classes and properties in a RDF graph.

        Args:
            graph: RDF graph.

        Returns:
            The metric value representing the ratio of undefined classes and properties. Best = 0
        """


        undefined_classes = set()
        undefined_properties = set()
        total_classes = 0
        total_properties = 0

        for subject, predicate, obj in graph:
            #if predicate == RDF.type and isinstance(obj, URIRef):
            if predicate in TYPE_PREDICATES and isinstance(obj, URIRef):
                if UsageUndefinedTermsMetric.isClass(obj, graph):
                    total_classes += 1
                elif not UsageUndefinedTermsMetric.isClass(obj, graph) and \
                    obj != OWL.ObjectProperty and obj != OWL.DatatypeProperty and obj != OWL.Class: # Do not count OWL types as undefined
                    undefined_classes.add(obj)

            #if isinstance(predicate, URIRef) and predicate != RDF.type: # Exclude rdf:type from property counting
            if isinstance(predicate, URIRef) and predicate not in TYPE_PREDICATES: # Exclude type_predicates from property counting
                total_properties += 1
                if not UsageUndefinedTermsMetric.isProperty(predicate, graph):
                    undefined_properties.add(predicate)

        size_undefined_classes = len(undefined_classes)
        size_undefined_properties = len(undefined_properties)

        if (total_classes + total_properties) > 0:
            undefined_terms = (size_undefined_classes + size_undefined_properties) / (total_classes + total_properties)
        else:
            undefined_terms = 0

        return undefined_terms

    def get_metric_name(self):
        return 'Usage of undefined terms metric'