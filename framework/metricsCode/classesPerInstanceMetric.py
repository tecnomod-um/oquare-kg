from rdflib import Graph, RDF

def classes_per_instance_metric(graph:Graph) -> float:
    """
    Calculates whether an instance has two rdf:type in a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The ratio of types per instance. Best = 1
    """
    
    total_instances = set()  # Subjets that at least have one rdf:type
    total_types = 0          # Total rdf:type (could be more than one)
    for subject, predicate, obj in graph:
        if predicate == RDF.type:
            total_instances.add(subject) 
            total_types += 1

    if total_instances:
        classes_per_instance = total_types / len(total_instances)
    else:
        classes_per_instance = 0

    return classes_per_instance