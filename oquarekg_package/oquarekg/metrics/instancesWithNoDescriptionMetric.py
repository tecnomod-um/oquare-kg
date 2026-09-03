from rdflib import Graph, RDF, RDFS, DCTERMS, URIRef, SKOS, DC
from .metric import Metric
from ..predicates import DESCRIPTION_PREDICATES, TYPE_PREDICATES

class InstancesWithNoDescriptionMetric(Metric):
    def calculate_metric(self, graph: Graph) -> float:
        """
        Calculates the ratio of instances without description used in a graph.

        Args:
            graph: RDFlib graph.

        Returns:
            Ratio of instances without description. Best = 0
        """
        instances = set()
        described_instances = set()
        
        # description_predicates = {
        #     URIRef ("http://purl.obolibrary.org/obo/IAO_0000115"),
        #     SKOS.definition,
        #     DCTERMS.description,
        #     DC.description,
        #     RDFS.comment,
        #     URIRef("http://schema.org/description"),
        #     URIRef("http://purl.obolibrary.org/obo/NCIT_P97")
        # }

        for subject, predicate, obj in graph:
            if isinstance(subject, URIRef):
                if predicate in TYPE_PREDICATES:
                    instances.add(subject)
                elif predicate in DESCRIPTION_PREDICATES:
                    described_instances.add(subject)

        undescribed_count = len(instances - described_instances)
        total_instances = len(instances)

        if total_instances > 0:
            without_description = undescribed_count / total_instances
        else:
            without_description = 0

        return without_description
    
    def get_metric_name(self):
        return 'Instances with no description metric'