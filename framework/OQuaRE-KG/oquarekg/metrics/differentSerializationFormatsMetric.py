from rdflib import Graph, URIRef, DC,DCAT, DCTERMS, VOID
from .metric import Metric
from ..predicates import FORMAT_PREDICATES

class DifferentSerializationFormatsMetric(Metric):
    def calculate_metric(self, graph: Graph) -> set:
        """
        Gets the set of valid graph serialization formats from graph metadata.

        Args:
            graph: RDF graph.

        Returns:
            A set of valid serialization formats, or an empty set if none are found.
        """

        formats = set()

        # Predicate list
        # format_predicates = {
        #     VOID.feature,
        #     DCTERMS.format,
        #     DC.format,
        #     URIRef("https://schema.org/encodingFormat"),
        #     DCAT.mediaType,
        # }

        for subject, predicate, obj in graph:
            if predicate in FORMAT_PREDICATES:
                # Extraer la parte final de la URI o literal
                uri_str = str(obj).strip()

                # If it is an URI, extract the final part
                if uri_str.startswith("http"):
                    if '#' in uri_str:
                        format_name = uri_str.split('#')[-1].lower()
                    else:
                        format_name = uri_str.split('/')[-1].lower()
                else:
                    # If it is a literal (e.x. "text/turtle", "application/ld+json")
                    format_name = uri_str.lower()

                formats.add(format_name)

        return formats

    def get_metric_name(self):
        return 'Different serialisation formats metric'