from rdflib import DC, DCTERMS, FOAF, SKOS, Graph, RDF, Literal, URIRef,RDFS, OWL
from .metric import Metric
from ..predicates import ANNOTATION_PREDICATES, TYPE_PREDICATES

class AnnotationRichnessMetric(Metric):
    def calculate_metric(self, graph: Graph) -> float:
        """
        Calculates the annotation richness metric for a RDF graph.

        Args:
            graph: RDF graph.

        Returns:
            The metric value representing the ratio of annotation properties to total instances. Best > 1
        """

        total_annotations = 0
        total_instances = set()  

        # Define a default set of annotation predicates. As many as needed
        # annotation_properties = {
        #     RDFS.label,
        #     RDFS.comment,
        #     RDFS.seeAlso,
        #     RDFS.isDefinedBy,
        #     OWL.versionInfo,
        #     DCTERMS.title,
        #     DC.title,
        #     FOAF.name,
        #     SKOS.prefLabel,
        #     URIRef("http://purl.obolibrary.org/obo/IAO_0000589"),
        #     URIRef("https://schema.org/name"),
        #     URIRef("http://purl.obolibrary.org/obo/NCIT_P108"),
        #     SKOS.altLabel,
        #     SKOS.hiddenLabel,
        #     URIRef("http://purl.obolibrary.org/obo/hasExactSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasExactSynonym"),
        #     URIRef("http://purl.obolibrary.org/obo/hasRelatedSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasRelatedSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasBroadSynonym"),
        #     URIRef("http://purl.obolibrary.org/obo/hasNarrowSynonym"),
        #     URIRef("http://www.geneontology.org/formats/oboInOWL#hasNarrowSynonym"),
        #     URIRef("http://purl.obolibrary.org/obo/NCIT_P90"),
        #     URIRef("http://purl.obolibrary.org/obo/IAO_0000118"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_9991119"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_9991118"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_0001847"),
        #     URIRef("http://purl.obolibrary.org/obo/OBI_0001886"),
        #     URIRef ("http://purl.obolibrary.org/obo/IAO_0000115"),
        #     SKOS.definition,
        #     DCTERMS.description,
        #     DC.description,
        #     URIRef("http://schema.org/description"),
        #     URIRef("http://purl.obolibrary.org/obo/NCIT_P97"),
        # }

        for subject, predicate, obj in graph:
            # Check if the predicate is an annotation predicate
            if predicate in ANNOTATION_PREDICATES and isinstance(subject, URIRef):
                total_annotations += 1

            # Count instances only if they have an rdf:type
            if predicate in TYPE_PREDICATES and isinstance(subject, URIRef):
                total_instances.add(subject)

        num_total_instances = len(total_instances)

        if num_total_instances > 0:
            annotations_metric = total_annotations / num_total_instances
        else:
            annotations_metric = 0

        return annotations_metric

   
    def get_metric_name(self):
        return 'Annotation richness metric'