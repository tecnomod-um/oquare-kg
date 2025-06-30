from rdflib import Graph, RDF, Literal, URIRef,RDFS, OWL

def annotation_richness_metric(graph):
    """
    Calculates the annotation richness metric for a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The metric value representing the ratio of annotation properties to total instances. Best = 1
    """

    total_annotations = set()
    total_instances = set()  

    # Define a default set of annotation predicates. As many as needed
    annotation_properties = {
        RDFS.label,
        RDFS.comment,
        RDFS.seeAlso,
        RDFS.isDefinedBy,
        OWL.versionInfo,
        URIRef("http://purl.org/dc/terms/description"),
        URIRef("http://purl.org/dc/terms/title"),
        URIRef("http://purl.org/dc/elements/1.1/description"),
        URIRef("http://purl.org/dc/elements/1.1/title")
    }

    for subject, predicate, obj in graph:
        # Check if the predicate is an annotation predicate
        if predicate in annotation_properties and isinstance(subject, URIRef):
            total_annotations.add((subject))

        # Count instances only if they have an rdf:type
        if predicate == RDF.type and isinstance(subject, URIRef):
            total_instances.add(subject)

    num_total_annotations = len(total_annotations)
    num_total_instances = len(total_instances)

    if num_total_instances > 0:
        descriptions_metric = num_total_annotations / num_total_instances
    else:
        descriptions_metric = 0

    return descriptions_metric