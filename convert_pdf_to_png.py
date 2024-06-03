from pdf2image import convert_from_path
from PIL import Image
import os
import argparse

def convert_pdf_to_png(pdf_filename, output_directory, dpi=300, thread_count=1):
    # Disable the decompression bomb error limit
    Image.MAX_IMAGE_PIXELS = None

    try:
        images = convert_from_path(pdf_filename, dpi=dpi, thread_count=thread_count)
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i, image in enumerate(images):
        output_path = os.path.join(output_directory, f"page_{i + 1}.png")
        image.save(output_path, "PNG")
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a PDF to PNG images.")
    parser.add_argument("pdf_filename", help="Path to the PDF file.")
    parser.add_argument("--output_directory", default="output_images", help="Directory to save PNG images.")
    parser.add_argument("--dpi", type=int, default=300, help="DPI for conversion (default: 300).")
    parser.add_argument("--threads", type=int, default=1, help="Number of threads for conversion (default: 1).")

    args = parser.parse_args()

    convert_pdf_to_png(args.pdf_filename, args.output_directory, dpi=args.dpi, thread_count=args.threads)
