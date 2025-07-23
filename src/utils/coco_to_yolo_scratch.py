
import os
import json
import shutil
from tqdm import tqdm
from collections import defaultdict

def convert_coco_to_yolo_scratch_only(
    json_path,
    output_dir,
    image_source_dir=None,
    image_dir_name="images",
    label_dir_name="labels"
):
    """
    Converts COCO-formatted annotations to YOLO format for scratch-only class (ID 0).

    Args:
        json_path (str): Path to the COCO annotations JSON file.
        output_dir (str): Base directory where YOLO labels and images will be saved.
        image_source_dir (str, optional): Path to the source images with split subfolders (e.g., /train, /val).
        image_dir_name (str): Name of the subfolder to store images in output_dir.
        label_dir_name (str): Name of the subfolder to store YOLO labels in output_dir.
    """
    with open(json_path, 'r') as f:
        data = json.load(f)

    images = {img['id']: img for img in data['images']}
    annotations = data['annotations']

    split = "train" if "train" in os.path.basename(json_path) else "val"

    label_split_dir = os.path.join(output_dir, label_dir_name, split)
    image_split_dir = os.path.join(output_dir, image_dir_name, split)
    os.makedirs(label_split_dir, exist_ok=True)
    os.makedirs(image_split_dir, exist_ok=True)

    label_data = defaultdict(list)
    invalid_count = 0

    for ann in tqdm(annotations, desc=f"Converting {split} annotations"):
        image_id = ann["image_id"]
        category_id = ann["category_id"]

        if category_id != 0:
            invalid_count += 1
            continue

        image_info = images[image_id]
        width, height = image_info["width"], image_info["height"]
        bbox = ann["bbox"]

        x_center = (bbox[0] + bbox[2] / 2) / width
        y_center = (bbox[1] + bbox[3] / 2) / height
        w_norm = bbox[2] / width
        h_norm = bbox[3] / height
        yolo_line = f"0 {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}"

        label_data[image_info["file_name"]].append(yolo_line)

    for image_filename, yolo_lines in label_data.items():
        label_filename = os.path.splitext(image_filename)[0] + ".txt"
        label_path = os.path.join(label_split_dir, label_filename)

        with open(label_path, "w") as f:
            f.write("\n".join(yolo_lines) + "\n")

        if image_source_dir:
            src_image_path = os.path.join(image_source_dir, split, image_filename)
            dst_image_path = os.path.join(image_split_dir, image_filename)
            if os.path.exists(src_image_path):
                shutil.copy2(src_image_path, dst_image_path)
            else:
                print(f"Image file not found: {src_image_path}")

    print(f"\nConversion complete for {split} split.")
    print(f"YOLO labels saved in: {label_split_dir}")
    if image_source_dir:
        print(f"Images copied to: {image_split_dir}")
    print(f"Skipped annotations with non-zero category_id: {invalid_count}")
