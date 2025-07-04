from rdflib import Graph, RDF, URIRef,SKOS

def synonyms_per_instance_metric(graph):
    """
    Calculates the synonyms per instance metric for an RDF graph.

    Args:
        graph: RDF graph.
        
    Returns:
        The synonyms per instance metric. Best >= 1
    """

    total_synonyms = 0
    instances = set()

    # Define a default set of synonym properties
    synonym_properties = {
            SKOS.altLabel,
            SKOS.hiddenLabel,
            URIRef("http://purl.obolibrary.org/obo/hasExactSynonym"),
            URIRef("http://www.geneontology.org/formats/oboInOWL#hasExactSynonym"),
            URIRef("http://purl.obolibrary.org/obo/hasRelatedSynonym"),
            URIRef("http://www.geneontology.org/formats/oboInOWL#hasRelatedSynonym"),
            URIRef("http://www.geneontology.org/formats/oboInOWL#hasBroadSynonym"),
            URIRef("http://purl.obolibrary.org/obo/hasNarrowSynonym"),
            URIRef("http://www.geneontology.org/formats/oboInOWL#hasNarrowSynonym"),
            URIRef("http://purl.obolibrary.org/obo/NCIT_P90"),
            URIRef("http://purl.obolibrary.org/obo/IAO_0000118"),
            URIRef("http://purl.obolibrary.org/obo/OBI_9991119"),
            URIRef("http://purl.obolibrary.org/obo/OBI_9991118"),
            URIRef("http://purl.obolibrary.org/obo/OBI_0001847"),
            URIRef("http://purl.obolibrary.org/obo/OBI_0001886"),
        # Add other common synonym properties here
    }

    # Count synonyms
    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef) and predicate in synonym_properties:
            total_synonyms += 1
        elif predicate == RDF.type and isinstance(subject, URIRef):    # Count instances
            instances.add(subject)

    total_instances = len(instances)

    # Calculate metric
    if total_instances > 0:
        synonyms_metric = total_synonyms / total_instances
    else:
        synonyms_metric = 0

    return synonyms_metric