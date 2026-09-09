import os
import re

def remove_extra_spaces(content):
    """Remove extra spaces from the content."""
    return re.sub(r'\s+', ' ', content).strip()

def process_files(input_folder, output_folder):
    """Process all files in the input folder and save cleaned files to the output folder."""
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(input_file_path):
            try:
                # Try reading the file with UTF-8 encoding
                with open(input_file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                # If UTF-8 fails, try reading with 'latin-1' encoding
                with open(input_file_path, 'r', encoding='latin-1') as file:
                    content = file.read()

            # Remove extra spaces
            cleaned_content = remove_extra_spaces(content)

            # Write the cleaned content to the output file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)

            print(f"Processed: {filename}")

# Specify the input and output folders
input_folder = '/Users/dipakkumarbiswas'  # Folder containing the original files
output_folder = '/Users/dipakkumarbiswas'  # Folder to save the cleaned files

# Process all files in the input folder
process_files(input_folder, output_folder)

print("All files processed successfully!")
