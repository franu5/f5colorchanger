from PIL import Image, ImageOps, ImageEnhance

# Load the image
# Change name of your image in box where "image.png" is

image_path = "image.png"
image = Image.open(image_path)

# Convert image to grayscale to isolate text
gray_image = ImageOps.grayscale(image)

# Enhance the text by adjusting contrast
enhancer = ImageEnhance.Contrast(gray_image)
enhanced_image = enhancer.enhance(2)

# Convert enhanced image to RGB to colorize the text
rgb_image = enhanced_image.convert("RGB")

# Create a new image with the same dimensions and red text
red_image = Image.new("RGB", rgb_image.size, "black")
pixels = red_image.load()
for i in range(rgb_image.width):
    for j in range(rgb_image.height):
        if rgb_image.getpixel((i, j))[0] > 100:  # if the pixel is light enough, treat it as part of the text
            pixels[i, j] = (255, 0, 0)  # Change to your color - you can pick it from https://htmlcolorcodes.com/color-picker/

# Combine the red text with the original image
result_image = Image.blend(image, red_image, 0.5)

# Save the result
result_image_path = "image_with_changed_color.png"
result_image.save(result_image_path)

result_image.show()
result_image_path
