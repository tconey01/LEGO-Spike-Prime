#Display a image controllable with the buttons on the hub

#import the light_matrix
from hub import light_matrix

#import buttons
from hub import button

while True:
    if button.pressed(button.LEFT):
        light_matrix.show_image(light_matrix.IMAGE_HAPPY)

    elif button.pressed(button.RIGHT):
        light_matrix.show_image(light_matrix.IMAGE_SAD)