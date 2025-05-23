from rdflib import URIRef, RDF, Graph, Literal

def entities_no_type_metric(graph):
    """
    Calculates the ratio of total entities to rdf:type declarations in a graph.

    Args:
        graph: RDF graph.

    Returns:
        The metric calculates the ratio of total entities to rdf:type declarations. Best = 0
    """

    total_types = 0
    total_entities = 0

    entities = set()

    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef): # checks if the subject is a URIRef to identify entities in an RDF graph
            entities.add(subject)

        if predicate == RDF.type:
            total_types += 1

    total_entities = len(entities)

    if total_types > 0:
        entities_no_type = total_entities / total_types
    else:
        entities_no_type = 0

    return entities_no_type