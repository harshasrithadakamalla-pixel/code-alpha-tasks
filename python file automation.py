import os
import shutil

source_folder = r"C:\Users\DELL\OneDrive\Desktop\07"

destination_folder = os.path.join(source_folder, "jpg_files")

if not os.path.exists(source_folder):
    print("Folder not found!")
else:
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    count = 0

    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            shutil.move(source_path, destination_path)

            print(file, "moved successfully.")
            count += 1

    print("\nTask completed!")
    print("Total JPG files moved:", count)