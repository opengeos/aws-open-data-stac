# aws-open-data-stac

## Introduction

The [AWS Open Data](https://registry.opendata.aws/) program hosts a lot of publicly available geospatial datasets. Some of these datasets are available as [SpatioTemporal Asset Catalog (STAC)](https://stacspec.org/) endpoints. This repo compiles the list of all AWS Open geospatial datasets with a STAC endpoint as a CSV file and as a JSON file, making it easier to find and use them programmatically. The list is updated daily.

A complete list of AWS open datasets as individual YAML files is available [here](https://github.com/awslabs/open-data-registry).

## Usage

This repo provides the list of AWS open geospatial datasets with a STAC endpoint in two formats:

- Tab separated values (TSV) file: [aws_stac_catalogs.tsv](https://github.com/giswqs/aws-open-data-stac/blob/master/aws_stac_catalogs.tsv)
- JSON file: [aws_stac_catalogs.json](https://github.com/giswqs/aws-open-data-stac/blob/master/aws_stac_catalogs.json)

The TSV file can be easily read into a Pandas DataFrame using the following code:

```python
import pandas as pd

url = 'https://github.com/giswqs/aws-open-data-stac/raw/master/aws_stac_catalogs.tsv'
df = pd.read_csv(url, sep='\t')
df.head()
```

## Related Projects

- A list of open datasets on AWS: [aws-open-data ](https://github.com/giswqs/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/giswqs/aws-open-data-geo)
