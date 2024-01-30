import os

def rename_files(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)
    
    # Sort the files to maintain order
    files.sort()
    
    # Counter for serial numbering
    serial_number = 1
    
    # Iterate through each file in the folder
    for file_name in files:
        # Construct the new file name
        new_file_name = f"{serial_number}.jpg"
        
        # Build the full paths for the old and new names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment the serial number for the next file
        serial_number += 1

# Replace 'path_to_notes_folder' with the actual path to your notes folder
notes_folder_path = 'path_to_notes_folder'

# Call the function to rename files
rename_files(notes_folder_path)
