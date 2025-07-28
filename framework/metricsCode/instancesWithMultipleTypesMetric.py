from rdflib import Graph, RDF

def instances_multiple_types_metric(graph):
    """
    Calculates the instances that has two or more rdf:type in a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The ratio instances instances with several rdf:types. Best = 0
    """
    one_type = set() # Subjects with one rdf:type
    several_types = set() # Subjects with more than one rdf:type

    for subject, predicate, obj in graph:
        if predicate == RDF.type:
            if subject in one_type:
                several_types.add(subject)
            else:
                one_type.add(subject)

    unique_instances = one_type.union(several_types)
    total_instances = len(unique_instances)
    multiple_types = len(several_types)

    if total_instances > 0:
        metric_result = (multiple_types / total_instances)
    else:
        metric_result = 0

    return metric_result