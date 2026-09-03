from rdflib import Graph, URIRef, RDF
from .metric import Metric
from ..predicates import TYPE_PREDICATES, STANDARD_VOCABULARIES

class ReuseTermsMetric(Metric):
    def __init__(self, domain: str):
        self.domain = domain

    def is_standard_vocab(self, term: str) -> bool:
        """Comprueba si un término pertenece a vocabularios estándar."""
        return any(term.startswith(vocab) for vocab in STANDARD_VOCABULARIES)

    def calculate_metric(self, graph: Graph) -> float:

        reused_classes = set()
        reused_properties = set()
        all_classes = set()
        all_properties = set()

        for subject, predicate, obj in graph:

            # All properties count
            if isinstance(predicate, URIRef):
                all_properties.add(predicate)

                # External properties, exclude standard vocabularies
                #if not str(predicate).startswith(self.domain):
                if not str(predicate).startswith(self.domain) and not self.is_standard_vocab(str(predicate)):   
                    reused_properties.add(predicate)


            # Classes (rdf:type)
            if predicate in TYPE_PREDICATES and isinstance(obj, URIRef):
                all_classes.add(obj)

                # External classes
                #if not str(obj).startswith(self.domain):
                if not str(obj).startswith(self.domain) and not self.is_standard_vocab(str(obj)):
                    reused_classes.add(obj)

        total_terms = len(all_classes) + len(all_properties)
        total_reused_terms = len(reused_classes) + len(reused_properties)

        
        if total_terms > 0:
            reused_terms = (total_reused_terms / total_terms)
        else:
            reused_terms = 0.0

        return reused_terms

    def get_metric_name(self):
        return 'Reuse terms metric'

# from rdflib import Graph, URIRef, RDF
# from metrics.metric import Metric
# from predicates import TYPE_PREDICATES

# class ReuseTermsMetric(Metric):
#     def __init__(self, domain: str):
#         self.domain = domain

#     def calculate_metric(self, graph: Graph) -> float:
#         """
#         Calculates external terms (classes and properties) in a RDF Graph.

#         Args:
#             graph: RDF graph.
#             domain: A string representing the namespace of the domain.

#         Returns:
#             The ratio of external terms. Best = 1
#         """

#         reused_classes = set()
#         reused_properties = set()
#         all_classes = set()
#         all_properties = set()

#         # Iterate over each triple in the graph
#         for subject, predicate, obj in graph:
#             all_properties.add(predicate)

#             # If predicate is rdf:type, then the object represents a class
#             if predicate in TYPE_PREDICATES:
#                 all_classes.add(obj)

#         # Check for external terms
#         for subject, predicate, obj in graph:
#             if isinstance(obj, URIRef) and not str(obj).startswith(self.domain):
#                 if predicate in TYPE_PREDICATES:
#                     reused_classes.add(obj)
#                 else:
#                     reused_properties.add(predicate)

#         # Calculate the ratio of reused terms
#         total_reused_terms = len(reused_classes) + len(reused_properties)
#         total_terms = len(all_classes) + len(all_properties)


#         if total_terms > 0:
#             reused_terms = (total_reused_terms / total_terms)
#         else:
#             reused_terms = 0

#         return reused_terms
    
#     def get_metric_name(self):
#         return 'Reuse terms metric'