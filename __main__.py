from PIL import Image
import pathlib
import argparse


# define function
def convert_to_transparent(image_path, output_path, threshold=170, increase_blue=True):
    # Load the image
    img = Image.open(image_path)
    img = img.convert("RGBA")  # Ensure image is in RGBA mode to handle transparency

    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b, a = pixels[i, j]
            # Calculate luminance to determine brightness
            luminance = 0.299*r + 0.587*g + 0.114*b
            # If the pixel is lighter than the threshold, make it transparent
            if luminance >= threshold:
                pixels[i, j] = (255, 255, 255, 0)  # Set to transparent
            else: # make it more blue
                if increase_blue == True:
                    pixels[i, j] = (
                        pixels[i, j][0], 
                        pixels[i, j][1], 
                        min(pixels[i, j][2] + 50, 255), 
                        pixels[i, j][3]
                    )

    # Save the modified image with a transparent background
    img.save(output_path, "PNG")


# call function
if __name__ == "__main__":
    # argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input_file', help='Name of the input image', required=True)
    parser.add_argument('-o','--output_file', help='Name of the output image', required=True)
    args = parser.parse_args()

    # set path
    main_path = pathlib.Path(__file__).parent.resolve()

    convert_to_transparent(
        main_path / args.input_file, 
        main_path / args.output_file, 
        threshold=170
    )