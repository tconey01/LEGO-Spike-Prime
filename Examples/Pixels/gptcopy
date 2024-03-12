from hub import button, sound
import time, random

# Define notes for tune
C4, D4, E4, F4, G4, A4, B4, C5 = 262, 294, 330, 349, 392, 440, 494, 523
tune = [C4, D4, E4, F4, G4, A4, B4, C5]

# Play tune
for note in tune:
    sound.beep(note, 500)  # Play note for 500 ms
    time.sleep_ms(100)  # Pause for 100 ms

# Initialize player and enemies
player_x, player_y = 2, 4
enemies = [{'x': random.randint(0, 4), 'y': -i*5} for i in range(5)]

start_time = time.time()
game_over, winner = False, False

while not game_over:
    time.sleep_ms(30)

    # Player movement
    if button.pressed(button.LEFT) and player_x > 0: player_x -= 1
    elif button.pressed(button.RIGHT) and player_x < 4: player_x += 1
    elif button.pressed(button.POWER) and player_y > 0: player_y -= 1
    elif button.pressed(button.CONNECT) and player_y < 4: player_y += 1

    # Check if player has reached the top
    if player_y == 0:
        end_time = time.time()  # Stop the timer
        print("You win! Time taken: {:.2f} seconds".format(end_time - start_time))
        winner = True
        break

    # Enemy movement and collision detection
    for enemy in enemies:
        enemy['y'] += 1
        if enemy['x'] == player_x and enemy['y'] == player_y:
            print("Game Over!")
            game_over = True
            break
        if enemy['y'] > 4: enemy['x'], enemy['y'] = random.randint(0, 4), -1

    # Draw game state in console
    for y in range(5):
        for x in range(5):
            if (x, y) == (player_x, player_y):
                print('P', end='')  # Print 'P' for player
            elif any(enemy['x'] == x and enemy['y'] == y for enemy in enemies):
                print('E', end='')  # Print 'E' for enemy
            else:
                print('.', end='')  # Print '.' for empty space
        print()  # Newline at the end of each row

    # Increase enemy speed over time
    if time.time() - start_time > 70:
        start_time = time.time()
        for enemy in enemies: enemy['y'] += 1

    time.sleep_ms(200)

# Game end message
if winner:
    print("Congratulations! You reached the top!")
else:
    print("Better luck next time!")
