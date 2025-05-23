from rdflib import Graph, URIRef, OWL, Literal, RDF

def deprecated_terms_metric(graph):
    """
    Computes the deprecated terms in a RDF Graph, if they are members of owl:deprecated.

    Args:
        graph: RDF graph.

    Returns:
        The deprecated terms metric value. Best = 0
    """

    deprecated_terms = 0
    total_terms = 0
    used_terms = set()
    deprecated_set = set()

    # Collect terms that have owl:deprecated Literal(True)
    for subject, predicate, obj in graph:
        if predicate == OWL.deprecated and obj == Literal(True):
            deprecated_set.add(subject)

    # Collect all unique terms (excluding literals)
    for subject, predicate, obj in graph:
        if not isinstance(subject, Literal):
            used_terms.add(subject)
        if not isinstance(predicate, Literal):
            used_terms.add(predicate)
        if not isinstance(obj, Literal):
            used_terms.add(obj)

    # Calculate deprecated terms
    for term in used_terms:
        if term in deprecated_set:
            deprecated_terms += 1

    total_terms = len(used_terms)

    if total_terms > 0:
        deprecated_metric = deprecated_terms / total_terms
    else:
        deprecated_metric = 0

    return deprecated_metric