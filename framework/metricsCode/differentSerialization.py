from rdflib import Graph, URIRef

def serialization_formats_metric(graph):
    """
    Gets the set of valid graph serialization formats from graph metadata.

    Args:
        graph: RDF graph.

    Returns:
        A set of valid serialization formats.
    """

    formats = set()
    void_feature_uri = URIRef("http://rdfs.org/ns/void#feature")  # Standard void feature URI

    for subject, predicate, obj in graph:
        if predicate == void_feature_uri:
            formats.add(obj)

    return formats