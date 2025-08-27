from rdflib import Graph, Literal, URIRef, Namespace

def serialization_formats_metric(graph):
    """
    Gets the set of valid graph serialization formats from graph metadata.

    Args:
        graph: RDF graph.

    Returns:
        A set of valid serialization formats, or an empty set if none are found.
    """

    formats = set()
    void_feature_uri = URIRef("http://rdfs.org/ns/void#feature")

    for subject, predicate, obj in graph:
        if predicate == void_feature_uri:
            # Extract the final part of the URI
            uri_str = str(obj)
            if '#' in uri_str:
                format_name = uri_str.split('#')[-1].lower()
            else:
                format_name = uri_str.split('/')[-1].lower()
            formats.add(format_name)

    return formats
