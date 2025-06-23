from rdflib import Graph, RDF, Literal, URIRef

def annotation_richness_metric(graph):
    """
    Calculates the annotation richness metric for a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The metric value representing the ratio of annotation properties to total instances. Best = 1
    """

    # Counters for annotation properties and total instances.
    total_annotation_properties = 0
    total_instances = 0

    # Count the number of annotation properties.
    annotation_properties = set()
    for subject, predicate, obj in graph:
        if isinstance(predicate, URIRef) and predicate != RDF.type:
            annotation_properties.add(predicate)
    total_annotation_properties = len(annotation_properties)

    # Count the number of total instances.
    instance_subjects = set()
    for subject, predicate, obj in graph:
        if predicate == RDF.type and isinstance(subject, URIRef):
            instance_subjects.add(subject)
    total_instances = len(instance_subjects)

    # Calculate the metric.
    if total_instances > 0:
        annotation_richness = total_annotation_properties / total_instances
    else:
        annotation_richness = 0

    return annotation_richness
