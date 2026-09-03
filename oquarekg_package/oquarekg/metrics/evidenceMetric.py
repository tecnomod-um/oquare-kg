from rdflib import Graph, RDF, RDFS, DCTERMS, URIRef, OWL, Literal
from rdflib.namespace import Namespace
from .metric import Metric
from ..predicates import EVIDENCE_PREDICATES, TYPE_PREDICATES

class EvidenceMetric(Metric):


    def calculate_metric(self, graph:Graph) -> float:
        """
        Calculates the ratio of triples with evidence predicates, in relation to the total number of triples
        defining instances in the graph.

        Args:
            graph: A RDFlib Graph.

        Returns:
            The ratio of triples with valid evidence predicates. Best = 1.
        """
        total_instances = 0
        triples_with_evidence_predicate = 0

        # Set of common evidence related predicates.
        # Add any other specific predicates that indicate evidence.
        # evidence_predicates = {
        #     URIRef("http://geneontology.org/lego/evidence"),
        #     URIRef("http://geneontology.org/lego/evidence-with"),
        #     DCTERMS.source,
        #     DCTERMS.references,
        #     RDFS.isDefinedBy,
        #     OWL.sameAs,
        #     URIRef("http://purl.org/dc/elements/1.1/source"),
        #     URIRef("http://schema.org/evidenceLevel"),
        #     URIRef("http://schema.org/evidenceOrigin"),
        
        # }

        for subject, predicate, obj in graph:
            # Count declarations of instances
            if predicate in TYPE_PREDICATES and isinstance(subject, URIRef):
                total_instances += 1


            # Contamos si el predicado pertenece al set de evidencia
            if predicate in EVIDENCE_PREDICATES:
                triples_with_evidence_predicate += 1
                
        if total_instances > 0:
            evidence_metric = triples_with_evidence_predicate / total_instances
        else:
            evidence_metric = 0

        return evidence_metric


    def get_metric_name(self):
        return 'Evidence metric'
