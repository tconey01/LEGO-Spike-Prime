#monitoring button presses

from hub import button
import time

# Initialize a dictionary to store the count of presses for each button
button_press_count = {
    'power': 0,
    'left': 0,
    'right': 0,
    'connect': 0,
}

# Map the button codes to their names
button_names = {
    1: 'power',
    0: 'left',
    2: 'right',
    3: 'connect',
}

while True:
    # Check each button
    for code, name in button_names.items():
        if button.pressed(code):
            # If the button is pressed, increment its count
            button_press_count[name] += 1
            print('The %s button has been pressed %d times' % (name, button_press_count[name]))
    time.sleep(0.1)
