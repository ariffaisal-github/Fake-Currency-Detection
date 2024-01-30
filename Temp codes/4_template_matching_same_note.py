"""
Matching the same note no.22 with different templates
Then, getting the coordinates of the matched templates

Output:
Template: bangabandhu.jpg, Coordinates: (900, 1219), (1461, 1923)
Template: bangla_1000.jpg, Coordinates: (878, 1029), (1371, 1184)
Template: bangla_1000_bottom.jpg, Coordinates: (2495, 1876), (3105, 2025)
Template: circles.jpg, Coordinates: (3053, 1521), (3105, 1798)
Template: flower_mid.jpg, Coordinates: (2255, 1408), (2390, 1546)
Template: oblique_lines.jpg, Coordinates: (3014, 1232), (3126, 1517)
Template: ovi.jpg, Coordinates: (2540, 1019), (3045, 1172)

Lower the threshold for less accurate match and getting more matches
"""


import cv2
import os
import numpy as np  # Import NumPy

def template_match(template_folder, target_image_path, output_folder):
    # Read the target image
    target_image = cv2.imread(target_image_path)
    
    # Iterate through each template image in the folder
    for template_file in os.listdir(template_folder):
        template_path = os.path.join(template_folder, template_file)
        
        # Read the template image
        template = cv2.imread(template_path)
        
        # Perform template matching
        result = cv2.matchTemplate(target_image, template, cv2.TM_CCOEFF_NORMED)
        
        # Set a threshold to identify matches
        threshold = 0.8
        loc = cv2.findNonZero((result >= threshold).astype(np.uint8))
        
        # Draw rectangles around the matched areas
        for pt in loc:
            rect_start = (pt[0][0], pt[0][1])
            rect_end = (pt[0][0] + template.shape[1], pt[0][1] + template.shape[0])
            cv2.rectangle(target_image, rect_start, rect_end, (255, 0, 0), 2) # Draw rectangle of color Blue with thickness 2 around the matched template
            
            # Print coordinates and template name
            print(f"Template: {template_file}, Coordinates: {rect_start}, {rect_end}")

        # Save the result image
        result_image_path = os.path.join(output_folder, f"result_{template_file}")
        cv2.imwrite(result_image_path, target_image)

# Replace 'path_to_notes_folder' and 'path_to_templates_folder' with the actual paths
notes_folder_path = './notes/'
templates_folder_path = './sample_templates/'
output_folder_path = './output/'

# Replace '22.jpg' with the specific image you want to use as the target
target_image_path = os.path.join(notes_folder_path, '22.jpg')  # taken from 22.jpg, and matches 23.jpg, 

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Perform template matching
template_match(templates_folder_path, target_image_path, output_folder_path)
