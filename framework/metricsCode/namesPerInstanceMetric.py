from rdflib import Graph, RDF, RDFS, URIRef, Literal, DCTERMS, DC

def names_per_instance_metric(graph):
    """
    Calculates the names per instance metric for a RDF graph.

    Args:
        graph: The RDF graph.

    Returns:
        The names per instance metric. Best >= 1
    """

    total_names = 0
    instances = set()

    # Define name properties. Add as many as needed
    name_properties = {
        RDFS.label,
        URIRef("http://schema.org/name"),
        DC.title,
        DCTERMS.title
    }

    # Count names and instances in a single pass
    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef):
            if predicate in name_properties:
                total_names += 1
            elif predicate == RDF.type:
                instances.add(subject)

    total_instances = len(instances)

    if total_instances > 0:
        names_metric = total_names / total_instances
    else:
        names_metric = 0

    return names_metric