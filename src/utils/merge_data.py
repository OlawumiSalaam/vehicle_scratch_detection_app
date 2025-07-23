
import os
import shutil
from pathlib import Path

def merge_scratch_and_no_damage(
    scratch_image_dir, scratch_label_dir,
    nodamage_image_dir, nodamage_label_dir,
    output_root
):
    for split in ['train', 'val']:
        images_out = Path(output_root) / "images" / split
        labels_out = Path(output_root) / "labels" / split
        images_out.mkdir(parents=True, exist_ok=True)
        labels_out.mkdir(parents=True, exist_ok=True)

        print(f"Copying scratch data for {split}...")
        scratch_img_path = Path(scratch_image_dir) / split
        scratch_lbl_path = Path(scratch_label_dir) / split

        for img_file in scratch_img_path.glob("*.jpg"):
            shutil.copy(img_file, images_out / img_file.name)
        for lbl_file in scratch_lbl_path.glob("*.txt"):
            shutil.copy(lbl_file, labels_out / lbl_file.name)

        print(f"Adding no_damage data for {split}...")
        nodmg_img_path = Path(nodamage_image_dir) / split
        nodmg_lbl_path = Path(nodamage_label_dir) / split

        for img_file in nodmg_img_path.glob("*.jpg"):
            shutil.copy(img_file, images_out / img_file.name)

        for img_file in nodmg_img_path.glob("*.jpg"):
            lbl_name = img_file.with_suffix(".txt").name
            lbl_file = nodmg_lbl_path / lbl_name

            if lbl_file.exists():
                shutil.copy(lbl_file, labels_out / lbl_name)
            else:
                (labels_out / lbl_name).write_text("")

        print(f"Merged {split} set completed.\n")