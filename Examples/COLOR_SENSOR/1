from hub import port
import color_sensor, time

# Define the color sensor
light = port.A

colors = {
    -1:'UNKNOWN',
    0:"BLACK",
    1:"MAGENTA",
    2:"PURPLE",
    3:"BLUE",
    4:"AZURE",
    5:"TURQUOISE",
    6:"GREEN",
    7:"YELLOW",
    8:"ORANGE",
    9:"RED",
    10:"WHITE",
    11:"DIM_WHITE",
}

while True:
    # Get the color from the sensor
    color = color_sensor.color(light)
    
    # Print the color
    print("The color is", colors[color])
    
    # Wait for a short period before the next scan
    time.sleep(0.6)
