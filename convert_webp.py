from PIL import Image
import os

input_path = "/Users/josephjose/Desktop/niogod_german/niogod_german/assets/hero-full.png"
output_path = "/Users/josephjose/Desktop/niogod_german/niogod_german/assets/hero-full.webp"

try:
    with Image.open(input_path) as img:
        img.save(output_path, "WEBP", quality=80)
    print(f"Successfully converted {input_path} to {output_path}")
except ImportError:
    print("Error: Pillow library is not installed.")
except Exception as e:
    print(f"An error occurred: {e}")
