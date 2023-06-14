import argparse
import os

import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

from util import sigmas


def create_pipeline(*operations):
    def pipeline(data):
        for operation in operations:
            data = operation(data)
        return data

    return pipeline


def normalize(image):
    return image / 255


def add_noise(image, mean=0, std=0.1):
    noise = np.random.normal(mean, std, image.shape)
    return np.clip(image + noise, 0, 1)


def main(image_path):
    # Open the image and convert to grayscale
    image = Image.open(image_path).convert("L")
    image_np = np.array(image)

    # Create blur operations with different sigma values
    blur_operations = [(lambda image: gaussian_filter(image, sigma)) for sigma in sigmas]

    # Create our pipeline with these operations
    operations = [normalize, add_noise] + blur_operations
    pipeline = create_pipeline(*operations)

    # Apply it to our image
    processed_image_np = pipeline(image_np)

    # Convert back to the range 0-255 and PIL Image object
    processed_image_np = np.clip(processed_image_np * 255, 0, 255).astype(np.uint8)
    processed_image = Image.fromarray(processed_image_np)

    # Create output filename by appending "_modified" before the extension
    base, ext = os.path.splitext(image_path)
    output_path = f"{base}_modified{ext}"

    if os.path.exists(output_path):
        os.remove(output_path)

    # Save the processed image
    processed_image.save(output_path)
    print(f"Processed image saved as {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process an image.')
    parser.add_argument('image_path', type=str, help='Path to the image file.')

    args = parser.parse_args()

    main(args.image_path)
