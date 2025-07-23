import json
import matplotlib.pyplot as plt
from collections import Counter

def explore_coco_dataset(json_path, set_name="Dataset"):
    """
    Visualizes and summarizes a COCO-format dataset (train, test, or val).
    
    Args:
        json_path (str): Path to the COCO annotations JSON file.
        set_name (str): A label to describe the dataset (e.g., 'Train', 'Test').
    """
    with open(json_path, "r") as f:
        coco_data = json.load(f)

    # Basic dataset info
    print(f"📁 {set_name} Dataset Info")
    print("Categories:", [c['name'] for c in coco_data['categories']])
    print("Number of images:", len(coco_data['images']))
    print("Number of annotations:", len(coco_data['annotations']))

    # Sample annotations
    print(f"\n📝 Sample Annotations ({set_name} Set):")
    for ann in coco_data['annotations'][:5]:
        print(f"  ID: {ann['id']}, Image ID: {ann['image_id']}, Category ID: {ann['category_id']}, BBox: {ann['bbox']}")

    # Category distribution
    category_counts = Counter([ann['category_id'] for ann in coco_data['annotations']])
    id_to_name = {cat['id']: cat['name'] for cat in coco_data['categories']}
    category_names = [id_to_name[cid] for cid in category_counts.keys()]
    frequencies = list(category_counts.values())

    # Plot category distribution
    plt.figure(figsize=(8, 5))
    plt.bar(category_names, frequencies, color="skyblue", edgecolor="black")
    plt.title(f"{set_name} Set: Category Distribution")
    plt.xlabel("Category")
    plt.ylabel("Number of Annotations")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Bounding box size distribution
    widths = [ann['bbox'][2] for ann in coco_data['annotations']]
    heights = [ann['bbox'][3] for ann in coco_data['annotations']]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(widths, bins=30, color="mediumseagreen", edgecolor="black")
    plt.title(f"{set_name} Set: BBox Widths")
    plt.xlabel("Width")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.hist(heights, bins=30, color="tomato", edgecolor="black")
    plt.title(f"{set_name} Set: BBox Heights")
    plt.xlabel("Height")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()
