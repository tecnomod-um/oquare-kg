# List of predicates used in OQuaRE-KG metrics (and other configurable parameters)


from rdflib import PROV, Namespace, URIRef, Graph, RDF, RDFS, URIRef, Literal, DCTERMS, DC, FOAF, SKOS, OWL, DCAT, VOID, DCAT


TYPE_PREDICATES = {
    RDF.type,
    URIRef("https://w3id.org/biolink/vocab/category"),
    URIRef("https://w3id.org/biolink/vocab/type")
}

EVIDENCE_PREDICATES = {
    URIRef("http://geneontology.org/lego/evidence"),
    URIRef("http://geneontology.org/lego/evidence-with"),
    DCTERMS.source,
    DCTERMS.references,
    RDFS.isDefinedBy,
    OWL.sameAs,
    DC.source,
    URIRef("http://schema.org/evidenceLevel"),
    URIRef("http://schema.org/evidenceOrigin"),
}

FORMAT_PREDICATES = {
    VOID.feature,
    DCTERMS.format,
    DC.format,
    URIRef("https://schema.org/encodingFormat"),
    DCAT.mediaType,
}

#  Same predicates for names per instance and instances with no names metrics
NAME_PREDICATES = {
    RDFS.label,
    DCTERMS.title,
    DC.title,
    FOAF.name,
    SKOS.prefLabel,
    URIRef("http://purl.obolibrary.org/obo/IAO_0000589"),
    URIRef("https://schema.org/name"),
    URIRef("http://purl.obolibrary.org/obo/NCIT_P108"),
    URIRef("https://w3id.org/biolink/vocab/symbol"),
    URIRef("https://w3id.org/biolink/vocab/full_name")
}

# License predicates for human license predicates and machine license predicates
LICENSE_PREDICATES = {
    DCTERMS.license,
    RDFS.comment,
    DCTERMS.description,
    RDFS.label,
    URIRef("https://schema.org/license"),
}

# This are not predicates but valid machine-readable licenses
MACHINE_LICENSES = {
        URIRef("http://creativecommons.org/licenses/by/4.0/"),
        URIRef("http://creativecommons.org/licenses/by-sa/4.0/"),
        URIRef("http://creativecommons.org/licenses/by-nc/4.0/"),
        # Add other valid machine-readable licenses here
    }

BASIC_PROV_PREDICATES = {
    DCTERMS.creator,
    DCTERMS.publisher,
    URIRef("http://purl.org/pav/providedBy")
}


#  Same predicates for description per instance and instances with no descriptions metrics
DESCRIPTION_PREDICATES = {
    URIRef ("http://purl.obolibrary.org/obo/IAO_0000115"),
    SKOS.definition,
    DCTERMS.description,
    DC.description,
    RDFS.comment,
    URIRef("http://schema.org/description"),
    URIRef("http://purl.obolibrary.org/obo/NCIT_P97")
}

#  Same predicates for synonym per instance and instances with no synonyms metrics
SYNONYM_PREDICATES = {
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
    URIRef("https://w3id.org/biolink/vocab/synonym"),
    URIRef("https://w3id.org/biolink/vocab/exact_synonym"),
    URIRef("https://w3id.org/biolink/vocab/related_synonym"),
    URIRef("https://w3id.org/biolink/vocab/broad_synonym"),
    URIRef("https://w3id.org/biolink/vocab/narrow_synonym")
    }  # set of synonym predicates, add as many as necesary


# Annotation properties
ANNOTATION_PREDICATES = (NAME_PREDICATES | DESCRIPTION_PREDICATES | SYNONYM_PREDICATES)

# Language tags predicates (ADD DESCRIPTIONS TOO??)
LANGUAGE_TAG_PREDICATES = (NAME_PREDICATES | SYNONYM_PREDICATES)

VOCABULARY_PREDICATES = {
    VOID.vocabulary
    }

#Used in used vocabularies metric and reuse terms metric
# Vocabularies to exclude from the analysis. Add more vocabularies to exclude as needed
STANDARD_VOCABULARIES = {
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#",  # RDF Vocabulary
    "http://www.w3.org/2000/01/rdf-schema#",       # RDFS Vocabulary
    "http://www.w3.org/2002/07/owl#",              # OWL Vocabulary
    #"http://rdfs.org/ns/void#",                    # VOID Vocabulary
    #"https://w3id.org/biolink/vocab/",          # Biolink Vocabulary
}

FORMAT_PREDICATES = {
    VOID.feature,
    DCTERMS.format,
    DC.format,
    URIRef("https://schema.org/encodingFormat"),
    DCAT.mediaType,
}

TRACEABILITY_PREDICATES = {
    PROV.wasAttributedTo,
    PROV.wasGeneratedBy,
    PROV.used,
    PROV.wasAssociatedWith,
    PROV.actedOnBehalfOf,
    URIRef("https://w3id.org/biolink/vocab/primary_knowledge_source"),
    URIRef("https://w3id.org/biolink/vocab/aggregator_knowledge_source"),
    URIRef("https://w3id.org/biolink/vocab/provided_by"),
    URIRef("https://w3id.org/biolink/vocab/xref"),
}