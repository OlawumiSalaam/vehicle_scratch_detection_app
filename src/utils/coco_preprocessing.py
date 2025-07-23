import json
import os


def map_all_classes_to_scratch(input_json_path, output_json_path):
    """
    Remap all categories in a COCO annotation JSON to a single category 'scratch' (ID=0).

    Args:
        input_json_path (str): Path to the original COCO annotation file.
        output_json_path (str): Path to save the modified COCO annotation file.
    """
    # Load the original COCO annotations
    with open(input_json_path, 'r') as f:
        data = json.load(f)

    # Set a single category: 'scratch' with ID 0
    data['categories'] = [{'id': 0, 'name': 'scratch'}]

    # Remap all annotation category_ids to 0
    for ann in data['annotations']:
        ann['category_id'] = 0

    # Save the modified annotations
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
    with open(output_json_path, 'w') as f:
        json.dump(data, f)

    print(f"All categories mapped to 'scratch' and saved to: {output_json_path}")


def verify_scratch_mapping(json_path):
    """
    Verify that a COCO annotation JSON contains only the 'scratch' category with ID 0.

    Args:
        json_path (str): Path to the modified COCO annotation file.
    """
    with open(json_path, 'r') as f:
        data = json.load(f)

    print("Categories in JSON:")
    for cat in data['categories']:
        print(f"  ID: {cat['id']}  Name: {cat['name']}")

    category_counts = {}
    for ann in data['annotations']:
        cid = ann['category_id']
        category_counts[cid] = category_counts.get(cid, 0) + 1

    print("\nAnnotation Category ID Counts:")
    for cid, count in category_counts.items():
        print(f"  Class ID {cid}: {count} annotations")

    if list(category_counts.keys()) == [0]:
        print("\nAll annotations successfully mapped to class ID 0 (scratch).")
    else:
        print("\nFound unexpected class IDs:", category_counts.keys())