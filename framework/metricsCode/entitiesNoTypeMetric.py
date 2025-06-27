from rdflib import URIRef, RDF, Graph, Literal

def entities_no_type_metric(graph):
    """
    Calculates the ratio of entities without an rdf:type declaration
    to the total number of entities in a graph.

    Args:
        graph: RDF graph.

    Returns:
        The ratio of entities without a type. Best = 0
    """

    entities = set()
    entities_with_type = set()

    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef):
            entities.add(subject)

        if predicate == RDF.type and isinstance(subject, URIRef):
            entities_with_type.add(subject)

    total_entities = len(entities)
    entities_without_type = total_entities - len(entities_with_type)

    if total_entities > 0:
        entities_no_type = entities_without_type / total_entities
    else:
        entities_no_type = 0

    return entities_no_type