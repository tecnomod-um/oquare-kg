from rdflib import Graph, URIRef, Namespace, Literal, DCTERMS, RDFS


def human_readable_license_metric(graph):
    """
    Validates human-readable license descriptions in a graph.

    Args:
        graph: RDF graph.

    Returns:
        True if a valid human-readable license description is found, False otherwise. Best = true
    """
   
    license_predicates = [
        DCTERMS.license,
        RDFS.comment,
        URIRef("http://www.w3.org/1999/xhtml/vocab#license"),
        URIRef("http://creativecommons.org/ns#license"),
    ]

    for predicate in license_predicates:
        for subject, predicate, obj in graph.triples((None, predicate, None)):
            if isinstance(obj, URIRef):
                return True  # Found a URI that likely links to a license
            if isinstance(obj, Literal) and "license" in obj.lower():
                return True  # Found a text mentioning license

    return False
