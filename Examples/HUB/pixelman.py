from hub import light_matrix
from hub import button
import time
import random
from hub import sound


# Define the notes (in Hz)
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

# Define a simple tune (a sequence of notes)
tune = [C4, D4, E4, F4, G4, A4, B4, C5]


# Play the tune

for note in tune:
    sound.beep(note, 500)  # Play each note for 500 ms
    time.sleep_ms(100)  # Wait for 100 ms between notes


player_x, player_y = 2, 4
light_matrix.set_pixel(player_x, player_y, 100)

# Initialize the enemies off the screen
enemies = [{'x': random.randint(0, 4), 'y': -i*5} for i in range(5)]

start_time = time.time()

# Game control flag
game_over = False
winner = False

while not game_over:
    light_matrix.clear()
    time.sleep_ms(30)

    # Move the player based on button presses
    if button.pressed(button.LEFT) and player_x > 0:
        player_x -= 1
    elif button.pressed(button.RIGHT) and player_x < 4:  # Assuming the matrix is 5x5
        player_x += 1
    elif button.pressed(button.POWER) and player_y > 0:
        player_y -= 1
        if player_y == 0:  # Player has reached the top
            print("You win!")
            winner = True
            break
    elif button.pressed(button.CONNECT) and player_y < 4:
        player_y += 1

    # Move the enemies down the screen
    for enemy in enemies:
        enemy['y'] += 1

        # Check if the enemy has hit the player
        if enemy['x'] == player_x and enemy['y'] == player_y:
            print("Game Over!")
            game_over = True  # This will exit the game loop
            break

        # Check if the enemy has moved off the screen
        if enemy['y'] > 4:
            # Reset the enemy to a random position at the top of the screen
            enemy['x'], enemy['y'] = random.randint(0, 4), -1

    # Draw the player
    light_matrix.set_pixel(player_x, player_y, 100)

    # Draw the enemies if they're within the screen bounds
    for enemy in enemies:
        if 0 <= enemy['y'] <= 4:
            light_matrix.set_pixel(enemy['x'], enemy['y'], 50)

    # Increase the speed of the enemies over time
    if time.time() - start_time > 55:  # Every 60 seconds
        start_time = time.time()
        for enemy in enemies:
            enemy['y'] += 1

    time.sleep_ms(200)

if winner:
    print("Congratulations! You reached the top!")
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    
else:
    print("Better luck next time!")
    light_matrix.show_image(light_matrix.IMAGE_SKULL)
