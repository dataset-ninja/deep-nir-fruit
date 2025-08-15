Dataset **deepNIR Fruit Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvOTk4X2RlZXBOSVIgRnJ1aXQgRGV0ZWN0aW9uL2RlZXBuaXItZnJ1aXQtZGV0ZWN0aW9uLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIjNRc0ZvdjRWVzdQQjBkSEhBYlRMbzhyaXZ3dU9LNE1wRG42NnFQKy9GUkE9In0=?response-content-disposition=attachment%3B%20filename%3D%22deepnir-fruit-detection-DatasetNinja.tar%22)

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