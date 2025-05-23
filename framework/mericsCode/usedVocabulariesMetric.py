from rdflib import Graph, URIRef, Namespace, RDF, OWL, RDFS

# Vocabularies to exclude from the analysis. Add more vocabularies to exclude as needed
excluded_vocabularies = {
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#",  # RDF Vocabulary
    "http://www.w3.org/2000/01/rdf-schema#",       # RDFS Vocabulary
    "http://www.w3.org/2002/07/owl#",              # OWL Vocabulary
    "http://rdfs.org/ns/void#",                    # VOID Vocabulary
}

def extract_namespace(uri):
    """
    Extract the base namespace from a URI.
    
    If the URI contains '#', it returns everything before the last '#'.
    If the URI contains '/', it returns everything before the last '/'.
    """
    uri_str = str(uri)
    if '#' in uri_str:
        return uri_str.rsplit('#', 1)[0] + '#'
    else:
        return uri_str.rsplit('/', 1)[0] + '/'

def used_vocabularies_metric(graph):
    """
    This function calculates the reuse score based on the ontologies used in the RDF graph, excluding specific vocabularies.
    The declared ontologies using `void:vocabulary` (or any other method of declaring vocabularies).
    
    Args:
        graph: RDF graph.
    
    Returns:
        The reuse score of the external ontologies. Best = 1
    """
    
    # Declare the VOID namespace
    VOID = Namespace("http://rdfs.org/ns/void#")

    # Initialize a set to store declared ontologies
    declared_ontologies = set()

    # Extract ontologies declared with `void:vocabulary` from the graph
    for subject, predicate, obj in graph.triples((None, VOID.vocabulary, None)):
        if isinstance(obj, URIRef):
            declared_ontologies.add(str(obj))

    # Initialize a set to store used ontologies
    used_ontologies = set()

    # Iterate over the triples in the graph to extract used ontologies
    for subject, predicate, obj in graph:
        if isinstance(predicate, URIRef):
            ns = extract_namespace(predicate)
            if ns not in excluded_vocabularies:
                used_ontologies.add(ns)

        # If the predicate is rdf:type, check the object
        if predicate == RDF.type and isinstance(obj, URIRef):
            ns = extract_namespace(obj)
            if ns not in excluded_vocabularies:
                used_ontologies.add(ns)

    # Calculate the intersection of declared ontologies and used ontologies (reused ones)
    reused = declared_ontologies.intersection(used_ontologies)
    
    # Return the ratio of reused ontologies to used ontologies
    if len(used_ontologies) > 0:
        reused_vacabularies_metric = len(reused) / len(used_ontologies) 
    else:
        reused_vacabularies_metric = 0

    return reused_vacabularies_metric
