from rdflib import Graph, URIRef, RDF, RDFS, OWL, Literal

def isClass(uri, graph):
    """Checks if a URI is a class."""
    return (URIRef(uri), RDF.type, OWL.Class) in graph or (URIRef(uri), RDF.type, RDFS.Class) in graph

def isProperty(uri, graph):
    """Checks if a URI is a property."""
    return (URIRef(uri), RDF.type, OWL.ObjectProperty) in graph or \
            (URIRef(uri), RDF.type, OWL.DatatypeProperty) in graph or \
            (URIRef(uri), RDF.type, RDF.Property) in graph

def misplaced_terms_metric(graph):
    """
    Calculates the ratio of class and property correct usage in a RDF Graph.

    Args:
        graph: RDF Graph.

    Returns:
        The misplaced terms metric value. Best = 0
    """

    incorrect_class_usage = set()
    incorrect_property_usage = set()
    total_triples = len(graph)

    for subject, predicate, obj in graph:
        # Ensure subject is a valid URI
        if isinstance(subject, URIRef):
            if isProperty(subject, graph) and not isClass(subject, graph) and \
                obj != OWL.ObjectProperty and obj != OWL.DatatypeProperty: # count them as an error when defining a property
                incorrect_property_usage.add(subject)

        # Ensure predicate is a valid URI
        if isinstance(predicate, URIRef):
            if isClass(predicate, graph) and not isProperty(predicate, graph):
                incorrect_class_usage.add(predicate)

        # Ensure object is a valid URI
        if isinstance(obj, URIRef):
            if isProperty(obj, graph) and not isClass(obj, graph) and \
                obj != OWL.ObjectProperty and obj != OWL.DatatypeProperty: # count it as an error when defining a property
                incorrect_property_usage.add(obj)



    if total_triples > 0:
        misplaced_metric = (len(incorrect_class_usage) + len(incorrect_property_usage)) / total_triples
    else:
        misplaced_metric = 0

    return misplaced_metric