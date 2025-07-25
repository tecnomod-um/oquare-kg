from rdflib import Graph, Literal, URIRef

def relations_per_node_metric(graph: Graph) -> float:
    """
    Calculates the ratio of relations per node in an RDF graph.

    Args:
        graph (Graph): An RDF graph from rdflib.

    Returns:
        float: Average number of properties per node. Best > 1
    """
    relations_per_node = {}

    for subject, predicate, obj in graph:
        if subject not in relations_per_node:
            relations_per_node[subject] = set()
        relations_per_node[subject].add(predicate)

    total_nodes = len(relations_per_node)

    total_relations = sum(len(predicates) for predicates in relations_per_node.values())
    if total_nodes > 0:
        average_relations = total_relations / total_nodes
    else:
        average_relations = 0

    return average_relations