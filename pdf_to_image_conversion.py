from pdf2image import convert_from_path
import os

# Function to convert PDF to images
def convert_pdf_to_images(pdf_path, output_dir, poppler_path):
    # Convert the PDF to images
    images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    
    # Save each page as an image and return the image paths
    image_paths = []
    for page_number, image in enumerate(images):
        image_path = f"{output_dir}/page_{page_number + 1}.png"
        image.save(image_path, 'PNG')
        image_paths.append(image_path)
    
    return image_paths
