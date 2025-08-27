from rdflib import Graph, URIRef, PROV, RDF

def traceability_data_metric(graph):
    """
    Calculates the ratio of resources that have at least one associated PROV predicate.

    Args:
        graph: RDF graph.

    Returns:
        The ratio of instances with associated provenance information. Best = 1
    """
    # Set of specific PROV predicates to consider. Add more if needed 
    prov_predicates = {
        PROV.wasAttributedTo,
        PROV.wasGeneratedBy,
        PROV.used,
        PROV.wasAssociatedWith,
        PROV.actedOnBehalfOf
    }

    instances = set() # store all instances (subjects of rdf:type)
    used_prov_predicates = set() # store URIs involved in PROV triples

    for subject, predicate, obj in graph:
        # Identify unique instances
        if predicate == RDF.type and isinstance(subject, URIRef):
            instances.add(subject)

        # Check if the triple uses a PROV predicate of interest
        prov_triple = False
        if predicate in prov_predicates:
            prov_triple = True

        if prov_triple:
            # If it is subject a PROV triple, add subject and object if they are URIs
            if isinstance(subject, URIRef):
                used_prov_predicates.add(subject)
            if isinstance(obj, URIRef):
                used_prov_predicates.add(obj)

    # Calculate the metric
    total_instances = len(instances)

    if total_instances > 0:
        instances_with_prov = instances.intersection(used_prov_predicates)
        
        prov_metric = len(instances_with_prov) / total_instances
    else:
        prov_metric = 0

    return prov_metric
