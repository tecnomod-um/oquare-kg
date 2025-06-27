from rdflib import Graph, URIRef, Literal, RDF, OWL

def isObjectProperty(predicate, graph):
    """Checks if a predicate is an object property."""
    return (predicate, RDF.type, OWL.ObjectProperty) in graph

def isDatatypeProperty(predicate, graph):
    """Checks if a predicate is a datatype property."""
    return (predicate, RDF.type, OWL.DatatypeProperty) in graph

def isLiteral(obj):
    """Checks if an object is a literal."""
    return isinstance(obj, Literal)

def isIndividual(obj, graph):
    """Crude check if an object is an individual."""
    return isinstance(obj, URIRef)

def misused_properties_metric(graph):
    """
    Computes the misused properties metric for a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The misused properties metric value. Best= 0
    """

    misused_properties = 0
    total_triples = len(graph)

    for subject, predicate, obj in graph:

        if not (predicate, RDF.type, None) in graph: # check if predicate is undefined.
            continue

        if isLiteral(obj) and isObjectProperty(predicate, graph): # check if an object property has a literal value
            misused_properties += 1

        if isIndividual(obj, graph) and isDatatypeProperty(predicate, graph): # check if a datatype property has an individual
            misused_properties += 1


    if total_triples > 0:
        misused_metric = misused_properties / total_triples
    else:
        misused_metric = 0

    return misused_metric
