from hub import light_matrix
import time

# Define a list of images
images = [
    light_matrix.IMAGE_SNAKE,
    light_matrix.IMAGE_GIRAFFE,
    light_matrix.IMAGE_BUTTERFLY,
    light_matrix.IMAGE_TORTOISE,
    # Add more images here...
]

# Display each image in the list
for image in images:
    light_matrix.show_image(image)
    time.sleep(1)