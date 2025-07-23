from pathlib import Path

def count_images_and_labels(base_path):
    """
    Count the number of image and label files in the train and val splits
    of a YOLO-formatted dataset.

    Args:
        base_path (str or Path): Path to the root dataset folder containing 'images' and 'labels' subdirectories.

    Prints:
        Counts of images and labels for both train and val sets.
    """
    image_train = list(Path(base_path, "images/train").glob("*.[jp][pn]g"))
    image_val = list(Path(base_path, "images/val").glob("*.[jp][pn]g"))
    label_train = list(Path(base_path, "labels/train").glob("*.txt"))
    label_val = list(Path(base_path, "labels/val").glob("*.txt"))

    print("\nDataset Summary")
    print(f" Image Count:")
    print(f"  ├─ Train images: {len(image_train)}")
    print(f"  └─ Val images:   {len(image_val)}")
    print(f"\n Label Count:")
    print(f"  ├─ Train labels: {len(label_train)}")
    print(f"  └─ Val labels:   {len(label_val)}\n")
