import os

def verify_yolo_labels(labels_root):
    splits = ['train', 'val']
    issues = []

    for split in splits:
        label_dir = os.path.join(labels_root, split)
        print(f"\nVerifying {split} labels in: {label_dir}")
        count = 0

        for fname in os.listdir(label_dir):
            if not fname.endswith(".txt"):
                continue

            path = os.path.join(label_dir, fname)
            with open(path, "r") as f:
                lines = f.readlines()

            if not lines:
                issues.append((fname, "Empty file"))
                continue

            for line in lines:
                parts = line.strip().split()
                if len(parts) != 5:
                    issues.append((fname, f"Invalid YOLO format: {line.strip()}"))
                    continue

                try:
                    cls_id = int(parts[0])
                    if cls_id != 0:
                        issues.append((fname, f"Invalid class ID: {cls_id}"))
                except ValueError:
                    issues.append((fname, f"Non-integer class ID: {parts[0]}"))

            count += 1

        print(f"Checked {count} label files in '{split}'")

    if issues:
        print(f"\n Found {len(issues)} issues:")
        for fname, reason in issues[:10]:
            print(f" - {fname}: {reason}")
    else:
        print("\nAll labels are correctly formatted and valid.")
