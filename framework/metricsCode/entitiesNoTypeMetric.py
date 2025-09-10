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

    all_subjects = set()
    classes = set()
    entities_with_type = set()

    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef):
            all_subjects.add(subject)
        if predicate == RDF.type:
            if isinstance(subject, URIRef):
                entities_with_type.add(subject)
            if isinstance(obj, URIRef):
                classes.add(obj)

    instances = all_subjects - classes
    total_instances = len(instances)

    instances_with_type = instances.intersection(entities_with_type)
    instances_without_type = total_instances - len(instances_with_type)

    if total_instances > 0:
        entities_no_type = instances_without_type / total_instances
    else:
        entities_no_type = 0

    return entities_no_type