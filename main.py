import os
from pdf_to_image_conversion import convert_pdf_to_images  # Import the PDF to image conversion function
from check_detection import detect_checks  # Import the check detection function

# Specify paths
poppler_path = r'C:\Users\HP\Documents\poppler-24.08.0\Library\bin'  # Set the correct Poppler path
pdf_path = r'C:\Users\HP\Documents\1000045953.pdf'  # Path to your PDF
output_dir = r'C:\Users\HP\Documents\output_images'  # Directory to save the images

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Convert the PDF to images
image_paths = convert_pdf_to_images(pdf_path, output_dir, poppler_path)

# Process each image and detect checks
for image_path in image_paths:
    detect_checks(image_path)

print("PDF processing and check detection completed.")
