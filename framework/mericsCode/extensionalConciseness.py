from rdflib import Graph, URIRef

def extensional_conciseness_metric(graph):
    """
    Compute the extensional conciseness metric using a bloom filter approach on a RDF graph.
    
    Args:
        RDF graph
    
    Returns: 
        Extensional conciseness metric value. Best = 0
    """
 
    entities = set()
    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef):
            entities.add(subject)
        if isinstance(obj, URIRef):
            entities.add(obj)

    entities_list = list(entities) # Convert to list to preserve order for consistent hashing
    
    resource_check = set()
    seen_hashes = set()

    for resource in entities_list:
        resourceHash = hash(resource)
        if resourceHash in seen_hashes:
            resource_check.add(resource)
        seen_hashes.add(resourceHash)

    size_resource_check = len(resource_check)
    size_entities = len(entities_list)

    if size_entities > 0:
        conciseness_metric = size_resource_check / size_entities  
    else:
        conciseness_metric = 0

    return conciseness_metric