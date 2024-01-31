import os
from PIL import Image

def crop_and_save_images(folder_path, crop_coordinates):
    # Create a directory for the cropped images
    output_folder = './cropped/'
    os.makedirs(output_folder, exist_ok=True)

    # Get the list of files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through each file in the folder
    for file_name in files:
        # Build the full path for the image
        file_path = os.path.join(folder_path, file_name)

        # Open the image
        image = Image.open(file_path)

        # Crop the image based on the specified coordinates
        cropped_image = image.crop(crop_coordinates)

        # Create a directory for each cropped image
        output_subfolder = os.path.join(output_folder, file_name.split('.')[0])
        os.makedirs(output_subfolder, exist_ok=True)

        # Save the cropped image to the corresponding subfolder
        output_path = os.path.join(output_subfolder, file_name)
        cropped_image.save(output_path)

# Replace 'path_to_notes_folder' with the actual path to your notes folder
notes_folder_path = './notes'

# Define the crop coordinates (left, upper, right, lower)
crop_coordinates = (100, 50, 400, 300)

# Call the function to crop and save images
crop_and_save_images(notes_folder_path, crop_coordinates)
