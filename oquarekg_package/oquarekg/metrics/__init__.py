#nombre de los scripts con las metricas y las clases
from .annotationRichnessMetric import AnnotationRichnessMetric
from .basicProvenanceMetric import BasicProvenanceMetric
from .compatibleDatatypeMetric import CompatibleDatatypeMetric
from .deprecatedClassPropMetric import DeprecatedTermsMetric
from .dereferenceabilityMetric import DereferenceabilityMetric
from .descriptionsPerInstanceMetric import DescriptionsPerInstanceMetric
from .differentSerializationFormatsMetric import DifferentSerializationFormatsMetric
from .entitiesNoTypeMetric import EntitiesNoTypeMetric
from .evidenceMetric import EvidenceMetric
from .extensionalConcisenessMetric import ExtensionalConcisenessMetric
from .humanLicenseMetric import HumanReadableLicenseMetric
from .instancesWithNoDescriptionMetric import InstancesWithNoDescriptionMetric
from .instancesWithNoNameMetric import InstancesWithNoNameMetric
from .instancesWithNoSynonymMetric import InstancesWithNoSynonymMetric
from .machineLicenseMetric import MachineLicenseMetric
from .misplacedClassPropMetric import MisplacedClassPropertyMetric
from .misusedDatatypeObjPropMetric import MisusedPropertiesMetric
from .multipleLanguagesMetric import MultipleLanguagesMetric
from .namesPerInstanceMetric import NamesPerInstanceMetric
from .relationsPerNode import RelationsPerNodeMetric
from .reuseTermsMetric import ReuseTermsMetric
from .synonymsPerInstanceMetric import SynonymsPerInstanceMetric
from .traceabilityDataMetric import TraceabilityDataMetric
from .usageUndefinedClassPropMetric import UsageUndefinedTermsMetric
from .usedVocabulariesMetric import UsedVocabulariesMetric
from .validFormatMetric import ValidFormatMetric
from .classesPerInstanceMetric import ClassesPerInstanceMetric
from .instancesWithMultipleTypesMetric import InstancesMultipleTypesMetric


#Lista de las clases para que las llame desde main.py como un modulo

__all__ = [
    "AnnotationRichnessMetric",
    "BasicProvenanceMetric",
    "ClassesPerInstanceMetric",
    "CompatibleDatatypeMetric",
    "DeprecatedTermsMetric",
    "DereferenceabilityMetric",
    "DescriptionsPerInstanceMetric",
    "DifferentSerializationFormatsMetric",
    "EntitiesNoTypeMetric",
    "EvidenceMetric",
    "ExtensionalConcisenessMetric",
    "HumanReadableLicenseMetric",
    "InstancesMultipleTypesMetric",
    "InstancesWithNoDescriptionMetric",
    "InstancesWithNoNameMetric",
    "InstancesWithNoSynonymMetric",
    "MachineLicenseMetric",
    "MisplacedClassPropertyMetric",
    "MisusedPropertiesMetric",
    "MultipleLanguagesMetric",
    "NamesPerInstanceMetric",
    "RelationsPerNodeMetric",
    "ReuseTermsMetric",
    "SynonymsPerInstanceMetric",
    "TraceabilityDataMetric",
    "UsageUndefinedTermsMetric",
    "UsedVocabulariesMetric",
    "ValidFormatMetric",

]
