import os
from PIL import Image

def crop_and_save_images(folder_path, crop_coordinates, name):
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
        output_path = os.path.join(output_subfolder, name)
        cropped_image.save(output_path)

# Replace 'path_to_notes_folder' with the actual path to your notes folder
notes_folder_path = './notes'


# Call the function to crop and save images

for i in range(8):
    name = ""
    if i == 1:
        name = "bangabandhu.jpg"
        crop_coordinates = (900, 1219, 1461, 1923)
        crop_and_save_images(notes_folder_path, crop_coordinates, name)
    elif i == 2:
        name = "bangla_1000.jpg"
        crop_coordinates = (878, 1029, 1371, 1184)
        crop_and_save_images(notes_folder_path, crop_coordinates, name)
    elif i == 3:
        name = "bangla_1000_bottom.jpg"
        crop_coordinates = (2495, 1876, 3105, 2025)
        crop_and_save_images(notes_folder_path, crop_coordinates, name)
    elif i == 4:
        name = "circles.jpg"
        crop_coordinates = (3053, 1521, 3105, 1798)
        crop_and_save_images(notes_folder_path, crop_coordinates, name)
    elif i == 5:
        name = "flower_mid.jpg"
        crop_coordinates = (2255, 1408, 2390, 1546)
        crop_and_save_images(notes_folder_path, crop_coordinates, name)
    elif i == 6:
        name = "oblique_lines.jpg"
        crop_coordinates = (3014, 1232, 3126, 1517)
        crop_and_save_images(notes_folder_path, crop_coordinates, name)
    elif i == 7:
        name = "ovi.jpg"
        crop_coordinates = (2540, 1019, 3045, 1172)
        crop_and_save_images(notes_folder_path, crop_coordinates, name)
    