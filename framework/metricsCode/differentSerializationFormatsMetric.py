from rdflib import Graph, URIRef

def serialization_formats_metric(graph):
    """
    Gets the set of valid graph serialization formats from graph metadata.

    Args:
        graph: RDF graph.

    Returns:
        A set of valid serialization formats, or None if none are found.
    """

    formats = set()
    void_feature_uri = URIRef("http://rdfs.org/ns/void#feature")

    for subject, predicate, obj in graph:
        if predicate == void_feature_uri:
            # Extraer la parte final de la URI
            formats.add(str(obj).split("/")[-1])

    return formats