from rdflib import Graph, URIRef, RDF

def reuse_terms_metric(graph, domain):
    """
    Calculates external terms (classes and properties) in a RDF Graph.

    Args:
        graph: RDF graph.
        domain: A string representing the namespace of the domain.

    Returns:
        The ratio of external terms. Best = 1
    """

    reused_classes = set()
    reused_properties = set()
    all_classes = set()
    all_properties = set()

    # Iterate over each triple in the graph
    for subject, predicate, obj in graph:
        all_properties.add(predicate)

        # If predicate is rdf:type, then the object represents a class
        if predicate == RDF.type:
            all_classes.add(obj)

    # Check for external terms
    for subject, predicate, obj in graph:
        if isinstance(obj, URIRef) and not str(obj).startswith(domain):
            if predicate == RDF.type:
                reused_classes.add(obj)
            else:
                reused_properties.add(predicate)

    # Calculate the ratio of reused terms
    total_reused_terms = len(reused_classes) + len(reused_properties)
    total_terms = len(all_classes) + len(all_properties)


    if total_terms > 0:
        reused_terms = (total_reused_terms / total_terms)
    else:
        reused_terms = 0

    return reused_terms