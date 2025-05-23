import os
import json
import time

# Path to the root directory of your project
root_dir = 'languages'

# Folder where metadata is stored
metadata_dir = 'metadata'

def extract_metadata(file_path, language, data_structure_type):
    """
    Extracts metadata from the given file path and generates a JSON structure.
    """
    # Use the file name as the name of the structure
    file_name = os.path.basename(file_path)
    name = file_name.replace('.py', '').replace('.cpp', '').replace('.java', '').replace('.js', '').replace('.go', '')

    # Description (you can adjust this part based on your naming or comments in the code)
    description = f"{name} implementation using basic data structures in {language}."

    # Get file creation and modification dates
    created_time = os.path.getctime(file_path)
    modified_time = os.path.getmtime(file_path)

    # Return a metadata dictionary
    return {
        "name": name.replace("_", " ").title(),
        "language": language,
        "path": file_path,
        "type": data_structure_type,
        "category": name.split("_")[0],  # Assuming the name starts with category, e.g. stack_linkedlist -> stack
        "description": description,
        "created_at": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(created_time)),
        "modified_at": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modified_time)),
        "lines_of_code": count_lines(file_path)  # Adding lines of code
    }

def count_lines(file_path):
    """
    Count the number of lines in a file.
    """
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

def generate_metadata():
    """
    Walks through the languages folder, generates metadata files, and stores them in the metadata folder.
    Skips test files and node_modules.
    """
    if not os.path.exists(metadata_dir):
        os.makedirs(metadata_dir)
        print(f"Metadata directory created: {metadata_dir}")

    for language in os.listdir(root_dir):
        language_dir = os.path.join(root_dir, language)
        
        if not os.path.isdir(language_dir):
            print(f"Skipping non-directory: {language_dir}")
            continue
        
        # Create metadata folder for each language
        language_metadata_dir = os.path.join(metadata_dir, language)
        if not os.path.exists(language_metadata_dir):
            os.makedirs(language_metadata_dir)
            print(f"Created language metadata directory: {language_metadata_dir}")

        for data_structure in os.listdir(language_dir):
            data_structure_dir = os.path.join(language_dir, data_structure)

            if not os.path.isdir(data_structure_dir):
                print(f"Skipping non-directory: {data_structure_dir}")
                continue

            # Now iterate over the files inside the data structure folders
            for root, dirs, files in os.walk(data_structure_dir):  # This will walk the folder and subfolders
                # Skip the node_modules directory
                if 'node_modules' in root:
                    print(f"Skipping node_modules directory: {root}")
                    continue  # Skip this directory and all its contents
                
                for file in files:
                    file_path = os.path.join(root, file)

                    # Skip directories and files in the 'tests' folder
                    if os.path.isdir(file_path):
                        continue
                    if 'tests' in file_path.lower():  # Skip files that are in the 'tests' folder
                        continue

                    # Only process files and avoid test files
                    if os.path.isfile(file_path):
                        if file.endswith('.py') or file.endswith('.cpp') or file.endswith('.java') or file.endswith('.js') or file.endswith('.go'):
                            print(f"Processing file: {file_path}")
                            data_structure_type = 'data_structure'  # or algorithm depending on the file
                            metadata = extract_metadata(file_path, language, data_structure_type)

                            # Log to see if metadata is being generated
                            print(f"Creating metadata for: {file_path}")
                            print(metadata)

                            # Save to JSON file in metadata directory
                            metadata_file = os.path.join(language_metadata_dir, f"{file.replace('.py', '').replace('.cpp', '').replace('.java', '').replace('.js', '').replace('.go', '')}.json")

                            # Check if file already exists, skip or overwrite as necessary
                            if os.path.exists(metadata_file):
                                print(f"Metadata file already exists for {file}, skipping...")
                            else:
                                with open(metadata_file, 'w') as f:
                                    json.dump(metadata, f, indent=4)
                                print(f"Metadata saved for {file}")

if __name__ == '__main__':
    generate_metadata()
