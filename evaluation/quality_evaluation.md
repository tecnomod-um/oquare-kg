# Quality evaluation scale

## Static Scaling

OQuaRE-KG scales the raw values of the metrics into normalised quality scores in the range [1,5] (Likert scale), with 1 being the lowest quality score, and 5 the highest quality score.

Metrics can be classified into three groups based on their range of values:

* Binary value: scaled to 1 or 5.

    | Metric score |    1    |     5    |
    |--------------|---------|----------|
    | Metric value |  false  |   true   |

* Values in the range [0,1] are scaled [1,5] by intervals of 20%.

    - If high values of the metric indicate high quality, then those high values are mapped to the higher scores in the range [1,5].

    | Metric score | 1       | 2          | 3          | 4          | 5        |
    |--------------|---------|------------|------------|------------|----------|
    | Metric value | [0-20]% | (20-40]%   | (40-60]%   | (60-80]%   | >80%     |

    - Otherwise, the high values are mapped onto the lower scores.

    | Metric score | 1       | 2          | 3          | 4          | 5        |
    |--------------|---------|------------|------------|------------|----------|
    | Metric value |   >80%  |  (60-80]%  | (40-60]%   |  (20-40]%  | [0-20]%  |

* Values in other ranges are scaled into [0,1] and then the previous scaling to [1,5] is applied.


Once the quality scores of the metrics have been calculated, the quality scores of the subcharacteristics and characteristics are obtained by averaging the scores of their corresponding associated metrics and subcharacteristics, respectively.