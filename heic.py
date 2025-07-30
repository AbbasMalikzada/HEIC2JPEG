import sys
import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(input_path, output_path):
    heif_file = pillow_heif.read_heif(input_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw"
    )
    image.save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
    if not os.path.exists("Converted"):
        os.makedirs("Converted")
    for file in os.listdir('.'):
        if file.lower().endswith('.heic'):
            input_path = file
            output_path = os.path.join("Converted", os.path.splitext(file)[0] + ".jpg")
            convert_heic_to_jpg(input_path, output_path)
    print("All HEIC files have been converted to JPEG in the 'Converted' folder.")