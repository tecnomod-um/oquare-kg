# OQuaRE-KG

OQuaRE-KG is a quality evaluation framework for assessing knowledge graphs based on OQuaRE.

## Installation

```bash
pip install git+https://github.com/tecnomod-um/oquare-kg.git#subdirectory=oquarekg_package
```

# Usage

## Complete workflow

```Python
from oquarekg import run_oquarekg

run_oquarekg(

    graph_file="graph.ttl",

    domain_uri="http://example.org"

)
```

## Evaluation only

```Python
from oquarekg import evaluate

evaluate(

    graph_file="graph.ttl",

    domain_uri="http://example.org"

)
```

## Scoring only

```Python
from oquarekg import scoring
scoring(
    input_dir="results",
    output_dir="results"
)
```
