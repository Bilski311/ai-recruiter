import os
import sys
from pathlib import Path


def delete_image_files(root_dir):
    root = Path(root_dir)
    if not root.is_dir():
        print(f"{root_dir} is not a valid directory.")
        return

    image_extensions = {".png", ".jpeg", ".jpg"}

    for current_dir, _, files in os.walk(root):
        for file in files:
            if Path(file).suffix.lower() in image_extensions:
                file_path = os.path.join(current_dir, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except OSError as e:
                    print(f"Error deleting {file_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python delete_image_files.py [directory]")
        sys.exit(1)

    directory = sys.argv[1]
    delete_image_files(directory)
