Dataset **deepNIR Fruit Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/x/3/rz/aXtvOfFS8aQ8BnjFm4j3Y7xKgTRjQed2j4BniB09djw9pjAAIjuPn5LwgcBbYT45S3qRR8cZQpPacvmqVCYKSERs3NCrJlPqDjmpZSrgyVEKgvHmxS5MilIc9Kmx.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='deepNIR Fruit Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://zenodo.org/record/6324489/files/yolov5.zip?download=1).