import os
import sys

def replace_in_file(file_path, old_str, new_str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = content.replace(old_str, new_str)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Updated content in: {file_path}")
    except Exception as e:
        print(f"Could not process file {file_path}: {e}")

def replace_in_path(current_path, old_str, new_str):
    for root, dirs, files in os.walk(current_path, topdown=False):
        for dir_name in dirs:
            new_dir_name = dir_name.replace(old_str, new_str)
            old_dir_path = os.path.join(root, dir_name)
            new_dir_path = os.path.join(root, new_dir_name)

            if new_dir_name != dir_name:
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed folder: {old_dir_path} -> {new_dir_path}")

        for file_name in files:
            new_file_name = file_name.replace(old_str, new_str)
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)

            if new_file_name != file_name:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed file: {old_file_path} -> {new_file_path}")

            replace_in_file(new_file_path, old_str, new_str)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <new_string>")
        sys.exit(1)

    new_string = sys.argv[1]

    old_string = "__APP_NAME__"
    current_directory = os.getcwd()

    replace_in_path(current_directory, old_string, new_string)

    print("Replacement completed.")
