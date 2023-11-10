from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "deepNIR Fruit Detection"
PROJECT_NAME_FULL: Optional[
    str
] = "deepNIR: Dataset for Generating Synthetic near-infrared (NIR) Images and Improved Fruit Detection System Using Deep Learning Techniques"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Agricultural()]
CATEGORY: Category = Category.Agriculture()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection(), CVTask.UnsupervisedLearning()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2022-03-15"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://inkyusa.github.io/deepNIR_dataset/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 377150
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/deep-nir-fruit"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://zenodo.org/record/6324489/files/yolov5.zip?download=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.mdpi.com/1424-8220/22/13/4721"
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {"GitHub":"some_link_to_repo_if_exists","Zenodo": "https://zenodo.org/record/6324489#.YkbEvX9Bzmg", "Kaggle": "https://www.kaggle.com/datasets/enddl22/deepnir-11fruits"}


CITATION_URL: Optional[str] = "https://zenodo.org/record/6324489/export/hx"
AUTHORS: Optional[List[str]] = ["Inkyu Sa", "Jong Yoon Lim", "Ho Seok Ahn"]
AUTHORS_CONTACTS: Optional[List[str]] = ["inkyu.sa@csiro.au", "jy.lim@auckland.ac.nz","hs.ahn@auckland.ac.nz", "b.macdonald@auckland.ac.nz"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "CSIRO Data61, Australia",
    "CARES, University of Auckland, Australia",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://research.csiro.au/robotics/",
    "https://www.auckland.ac.nz/en/engineering/our-research/discover/research-areas-and-facilities/cares.html",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
