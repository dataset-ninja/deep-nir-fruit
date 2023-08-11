Dataset **deepNIR Fruit Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/K/s/U9/Ww5suakklYmx4pOWlBnyTYTzxBh7btp2anl3UYMoBCEDBSu2nFwJXRTwDH0f9SBasONziPzZ0Ka7G4m64VGxLcw96sLixHDhkuQVd87JuIhP1gg8fF15nZnthQVx.tar)

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