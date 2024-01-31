import os
from PIL import Image

def rotate_images(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through each file in the folder
    for file_name in files:
        # Build the full path for the image
        file_path = os.path.join(folder_path, file_name)
        
        # Open the image and rotate it by 180 degrees
        image = Image.open(file_path)
        rotated_image = image.rotate(180)
        
        # Save the rotated image back to the file
        rotated_image.save(file_path)

# Replace 'path_to_notes_folder' with the actual path to your notes folder
notes_folder_path = './notes'

# Call the function to rotate images
rotate_images(notes_folder_path)
