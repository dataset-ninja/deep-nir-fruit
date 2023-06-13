import glob
import os

import supervisely as sly
from supervisely.io.fs import file_exists, get_file_name, get_file_name_with_ext


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/home/iwatkot/supervisely/ninja-datasets/deepfruit/yolov5"
    # images_folder = "images"
    anns_folder = "labels"
    ann_ext = ".txt"
    batch_size = 30

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        class_name = image_path.split(dataset_path)[1].split("/")[1]
        obj_class = name_to_class[class_name]

        bbox_path = os.path.join(
            image_path.split("images")[0], anns_folder, get_file_name(image_path) + ann_ext
        )

        if file_exists(bbox_path):
            with open(bbox_path) as f:
                content = f.read().split("\n")

                for curr_data in content:
                    if len(curr_data) != 0:
                        curr_data = list(map(float, curr_data.split(" ")))

                        left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                        right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                        top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                        bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                        rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                        label = sly.Label(rectangle, obj_class)
                        labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class_apple = sly.ObjClass("apple", sly.Rectangle)
    obj_class_avocado = sly.ObjClass("avocado", sly.Rectangle)
    obj_class_blueberry = sly.ObjClass("blueberry", sly.Rectangle)
    obj_class_capsicum = sly.ObjClass("capsicum", sly.Rectangle)
    obj_class_cherry = sly.ObjClass("cherry", sly.Rectangle)
    obj_class_mango = sly.ObjClass("mango", sly.Rectangle)
    obj_class_orange = sly.ObjClass("orange", sly.Rectangle)
    obj_class_rockmelon = sly.ObjClass("rockmelon", sly.Rectangle)
    obj_class_strawberry = sly.ObjClass("strawberry", sly.Rectangle)
    obj_class_kiwi = sly.ObjClass("kiwi", sly.Rectangle)
    obj_class_wheat = sly.ObjClass("wheat", sly.Rectangle)

    name_to_class = {
        "apple": obj_class_apple,
        "avocado": obj_class_avocado,
        "blueberry": obj_class_blueberry,
        "capsicum": obj_class_capsicum,
        "cherry": obj_class_cherry,
        "mango": obj_class_mango,
        "orange": obj_class_orange,
        "rockmelon": obj_class_rockmelon,
        "strawberry": obj_class_strawberry,
        "kiwi": obj_class_kiwi,
        "wheat": obj_class_wheat,
    }

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(name_to_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    all_train_images_pathes = glob.glob(dataset_path + "/*/train/*/*.jpg")
    all_valid_images_pathes = glob.glob(dataset_path + "/*/valid/*/*.jpg")
    all_test_images_pathes = glob.glob(dataset_path + "/*/test/*/*.jpg")

    ds_to_pathes = {
        "train": all_train_images_pathes,
        "valid": all_valid_images_pathes,
        "test": all_test_images_pathes,
    }

    for ds_name in list(ds_to_pathes.keys()):
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_pathes = ds_to_pathes[ds_name]
        # anns_path = os.path.join(dataset_path, ds_name, anns_folder)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

        for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
            img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

    return project
