from rdflib import Graph, URIRef, RDF, RDFS, OWL, Literal

def isClass(uri, graph):
    """Checks if a URI is a class."""
    return (URIRef(uri), RDF.type, OWL.Class) in graph or (URIRef(uri), RDF.type, RDFS.Class) in graph

def isProperty(uri, graph):
    """Checks if a URI is a property."""
    return (URIRef(uri), RDF.type, OWL.ObjectProperty) in graph or \
           (URIRef(uri), RDF.type, OWL.DatatypeProperty) in graph or \
           (URIRef(uri), RDF.type, RDF.Property) in graph

def undefined_terms_metric(graph):
    """
    Calculates the metric value for undefined classes and properties in a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The metric value representing the ratio of undefined classes and properties. Best = 0
    """


    undefined_classes = set()
    undefined_properties = set()
    total_classes = 0
    total_properties = 0

    for subject, predicate, obj in graph:
        if predicate == RDF.type and isinstance(obj, URIRef):
            if isClass(obj, graph):
                total_classes += 1
            elif not isClass(obj, graph) and \
                obj != OWL.ObjectProperty and obj != OWL.DatatypeProperty and obj != OWL.Class: # Do not count OWL types as undefined
                undefined_classes.add(obj)

        if isinstance(predicate, URIRef) and predicate != RDF.type: # Exclude rdf:type from property counting
            total_properties += 1
            if not isProperty(predicate, graph):
                undefined_properties.add(predicate)

    size_undefined_classes = len(undefined_classes)
    size_undefined_properties = len(undefined_properties)

    if (total_classes + total_properties) > 0:
        undefined_terms = (size_undefined_classes + size_undefined_properties) / (total_classes + total_properties)
    else:
        undefined_terms = 0

    return undefined_terms
