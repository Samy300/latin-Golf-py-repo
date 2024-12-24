import pygame
import os
import math
import random


pygame.init()

# Screen setup
screen_width, screen_height = 1345, 760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mafia's Golf")

# Load background image
background_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
background_image = pygame.image.load(os.path.join("Final proyect 2/Images/Nivel_4_recursos_mafialand/fondo_mafialand.PNG"))
background_image = pygame.transform.rotate(background_image, -90)
background_image = pygame.transform.scale(background_image, (1345, 760))
background_surface.blit(background_image, (0, 0))

# Set transparency for the background
background_surface.set_alpha(220)  # Adjust the alpha value for desired transparency (0-255)

# Load images and scale them, set a function which imports the image and sets the width and height so it's easier and cleaner to load the image on each onject
def load_image(path, width, height, rotate=None):
    image = pygame.image.load(path)
    if rotate:
        image = pygame.transform.rotate(image, rotate)
    return pygame.transform.scale(image, (width, height))

#load the object images and resize them
flag_start = load_image("Final proyect 2/Images/flag_start.png", 100, 85)
hole = load_image("Final proyect 2/Images/hoyo.png", 60, 90)
ball = load_image("Final proyect 2/Images/pelota.png", 25, 25)
arrow = load_image("Final proyect 2/Images/arrow.png", 20, 30,rotate = 270)
car = load_image("Final proyect 2/Images/Nivel_4_recursos_mafialand/car.png", 250, 140, rotate=270)
bottles = load_image("Final proyect 2/Images/Nivel_4_recursos_mafialand/bottles.png", 90, 83)
thief = load_image("Final proyect 2/Images/Nivel_4_recursos_mafialand/thief.png", 114, 106)
bottles2 = load_image("Final proyect 2/Images/Nivel_4_recursos_mafialand/bottles2.png", 89, 90)
trash = load_image("Final proyect 2/Images/Nivel_4_recursos_mafialand/trash.png", 300, 150)


# object rectangles, it will be the way for them to move or interact with the ball in the game 
hole_rec = pygame.Rect(1160, 660, 60, 90)
bottles_rec = pygame.Rect(755, 160, 90, 83)
bottles2_rec = pygame.Rect(625, 520, 89, 90)
trash_rec = pygame.Rect(990, 30, 300, 150)
ball_rec = pygame.Rect(100, 690, 25, 25)
thief_rec = pygame.Rect(370, 610, 114, 106)
car_rec = pygame.Rect(100, 310, 250, 140)



# Draw everything on the window
#Remember the order of drawing objcts in the window: Background,static objects and lastly dynamic objects
def draw_window(ball_rec, dragging, car_rec, start_pos, direction, shots_left):
    screen.blit(background_surface, (0, 0))
    screen.blit(flag_start, (70, 625))
    screen.blit(hole, (hole_rec.x, hole_rec.y))
    screen.blit(bottles, (bottles_rec.x, bottles_rec.y))
    screen.blit(thief, (thief_rec.x, thief_rec.y))
    screen.blit(bottles2, (bottles2_rec.x, bottles2_rec.y))
    screen.blit(trash, (trash_rec.x, trash_rec.y))
    screen.blit(car, (car_rec.x, car_rec.y))
    screen.blit(ball, (ball_rec.x, ball_rec.y))  

    # Display the shots left
    font = pygame.font.Font(None, 40)  
    shots_text = font.render(f"Shots Left: {shots_left}", True, (0, 0, 0))  
    screen.blit(shots_text, (10, 10))  # Position in the top-left corner

    if dragging:
        # Recalculate the direction vector dynamically
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        direction = mouse_pos - pygame.Vector2(ball_rec.center)

        if direction.length() > 0:  # Ensure the vector isn't zero-length
            angle = math.degrees(math.atan2(direction.y, direction.x))  # Calculate angle in degrees
            rotated_arrow = pygame.transform.rotate(arrow, -angle)

            # Offset distance to position the arrow in front of the ball
            arrow_offset = 30  # Adjust this value for desired distance from the ball
            offset_x = direction.normalize().x * arrow_offset
            offset_y = direction.normalize().y * arrow_offset

            # Position the arrow in front of the ball
            arrow_pos = (ball_rec.centerx + offset_x, ball_rec.centery + offset_y)
            arrow_rect = rotated_arrow.get_rect(center=arrow_pos)
            screen.blit(rotated_arrow, arrow_rect.topleft)

    pygame.display.update()
    
#Thief throw the ball away in a random place in the map
def get_random_position(hole_rec):
    while True:
        # Generate random x and y coordinates within the screen boundaries
        x = random.randint(0, screen_width - ball_rec.width)
        y = random.randint(0, screen_height - ball_rec.height)
        
        # Ensure the random position is not within the hole area
        if not hole_rec.colliderect(pygame.Rect(x, y, ball_rec.width, ball_rec.height)):
            return pygame.Vector2(x, y)  # Return as a pygame.Vector2 object
        

#Endscreen once the game is over, go back to main menu or play again
def show_end_screen(result, level_restart_function, menu_function):
    screen = pygame.display.get_surface()  # Get the screen surface
    screen_width, screen_height = screen.get_size()  # Get the screen dimensions
    end_screen_running = True
    
    # Preload button images
    main_menu_button = pygame.image.load("Final proyect 2/Final proyect/Images/boton_play.png").convert_alpha()
    play_again_button = pygame.image.load("Final proyect 2/Final proyect/Images/botones_levels_credits.png").convert_alpha()
    
    # Scale buttons to appropriate sizes
    main_menu_button = pygame.transform.scale(main_menu_button, (250, 70))
    play_again_button = pygame.transform.scale(play_again_button, (290, 120))

    
    # Create button rectangles for interaction
    main_menu_rect = main_menu_button.get_rect(center=(screen_width // 3, 2 * screen_height // 3))
    play_again_rect = play_again_button.get_rect(center=(2 * screen_width // 3, 2 * screen_height // 3))

    # Fonts for text
    #Font for the buttons and messsage
    font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 74)
    button_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 40)

    while end_screen_running:
        background_image = pygame.image.load(os.path.join("Final proyect 2/Images/Nivel_4_recursos_mafialand/fondo_mafialand.PNG"))
        background_image = pygame.transform.rotate(background_image, -90)
        background_image = pygame.transform.scale(background_image, (1345, 760))
        background_surface.blit(background_image, (0, 0))

        # Set transparency for the background
        background_surface.set_alpha(220)  # Adjust the alpha value for desired transparency (0-255)
        
        screen.fill((0,0,0))

        # Display win or lose message
        message = "Congratulations!" if result == "win" else "Game Over!"
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 3))
        screen.blit(text, text_rect)

        # Draw the buttons
        screen.blit(main_menu_button, main_menu_rect.topleft)
        screen.blit(play_again_button, play_again_rect.topleft)

        # Draw text on buttons
        main_menu_text = button_font.render("Main Menu", True, (0, 0, 0))
        play_again_text = button_font.render("Play Again", True, (0, 0, 0))
        screen.blit(main_menu_text, main_menu_text.get_rect(center=main_menu_rect.center))
        screen.blit(play_again_text, play_again_text.get_rect(center=play_again_rect.center))

        pygame.display.update()  # Update the screen to show the new content

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if main_menu_rect.collidepoint(mouse_pos):
                    from game import main_menu
                    end_screen_running = False
                    main_menu()  # Redirect to the main menu
                elif play_again_rect.collidepoint(mouse_pos):
                    end_screen_running = False
                    level_restart_function()  # Restart the game


# Game FPS
FPS = 60
# to track the thief's initial position and movement direction
thief_start_y = 610  # Initial Y position
thief_direction = 1  # 1 for moving down, -1 for moving up
thief_move_limit = 100  # Maximum movement range 

# Main game loop
def main():
    global thief_direction
    clock = pygame.time.Clock()  # FPS control

    ball_rec = pygame.Rect(100, 690, 25, 25)  # Ball rectangle for tracking
    ball_pos = pygame.Vector2(ball_rec.x, ball_rec.y)  # Ball position vector
    ball_velocity = pygame.Vector2(0, 0)  # Initial ball velocity
    friction = 0.95  # Friction to reduce ball speed
    max_power = 70  # Max power of shot
    dragging = False
    start_pos = pygame.Vector2()  # Track where the dragging of the ball starts
    direction = pygame.Vector2()  # Direction for the arrow

    shots_taken = 0  # Counter for shots taken
    MAX_SHOTS = 15  # Maximum number of shots allowed
    thief_collision_cooldown = 0  # Cooldown timer for thief collision
    game_finished = False
    message_displayed = False
    running = True

    while running:
        clock.tick(FPS)

        # Reduce the cooldown timer
        if thief_collision_cooldown > 0:
            thief_collision_cooldown -= 1

        # Loop through all the events
        for event in pygame.event.get():
            # Check if the user wants to close the window
            if event.type == pygame.QUIT:
                running = False

            # Check for a mouse button press (click) and ensure the player can still take shots
            elif event.type == pygame.MOUSEBUTTONDOWN and shots_taken < MAX_SHOTS:
                mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                if ball_rec.collidepoint(mouse_pos) and ball_velocity.length() == 0:
                    dragging = True
                    start_pos = mouse_pos  # Start of dragging

            # Check for releasing the mouse button while dragging and within the shot limit
            elif event.type == pygame.MOUSEBUTTONUP and dragging and shots_taken < MAX_SHOTS:
                mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                direction = mouse_pos - ball_pos  # Direction of shot
                power = min(direction.length(), max_power)  # Cap power to max
                if direction.length() > 0:
                    ball_velocity = direction.normalize() * power * 0.3  # Adjust velocity based on power
                    shots_taken += 1  # Increment the shot counter
                dragging = False

            # Check for mouse movement while dragging
            elif event.type == pygame.MOUSEMOTION and dragging:
                # Update the direction of the vector from the ball and the current mouse pos
                direction = pygame.Vector2(pygame.mouse.get_pos()) - pygame.Vector2(ball_rec.center)

        # Update ball position
        if ball_velocity.length() > 0:
            ball_pos += ball_velocity
            ball_velocity *= friction  # Apply friction to reduce speed
            ball_rec.topleft = (ball_pos.x, ball_pos.y)  # Update ball rect position

            # Stop ball when it slows down enough
            if ball_velocity.length() < 0.5:
                ball_velocity = pygame.Vector2(0, 0)

            # Collision with screen boundaries
            if ball_rec.left <= 0 or ball_rec.right >= screen_width:
                ball_velocity.x *= -1  # Reverse horizontal velocity
                ball_pos.x = max(0, min(screen_width - ball_rec.width, ball_pos.x))  # Keep in bounds
            if ball_rec.top <= 0 or ball_rec.bottom >= screen_height:
                ball_velocity.y *= -1  # Reverse vertical velocity
                ball_pos.y = max(0, min(screen_height - ball_rec.height, ball_pos.y))  # Keep in bounds

            # Collision with the thief
            if ball_rec.colliderect(thief_rec) and thief_collision_cooldown == 0:
                # Generate a new random position for the ball, excluding the hole area
                new_ball_pos = get_random_position(hole_rec)
                
                # Update the ball's position to the new random position
                ball_rec.topleft = (new_ball_pos.x, new_ball_pos.y)
                ball_pos.update(new_ball_pos.x, new_ball_pos.y)
                ball_velocity = pygame.Vector2(0, 0)  # Stop the ball movement
                # counter of shots -1
                shots_taken += 1  # Deduct one shot
                thief_collision_cooldown = FPS  # Set cooldown to prevent repeated deductions

            # Collision with the car
            if ball_rec.colliderect(car_rec):
                ball_rec.topleft = (100, 690)  # Reset ball to start position
                ball_pos.update(100, 690)
                ball_velocity = pygame.Vector2(0, 0)  # Stop ball movement
                
            #Collision with the bottles
            if ball_rec.colliderect(bottles_rec):
                # Reverse the ball's velocity and reduce its magnitude to simulate energy loss
                ball_velocity.x *= -1  # Reverse horizontal velocity
                ball_velocity.y *= -1  # Reverse vertical velocity
                ball_velocity *= 0.8  # Reduce speed to simulate energy loss

            #Collision with the bottles2
            if ball_rec.colliderect(bottles2_rec):
                # Reverse the ball's velocity and reduce its magnitude to simulate energy loss
                ball_velocity.x *= -1  # Reverse horizontal velocity
                ball_velocity.y *= -1  # Reverse vertical velocity
                ball_velocity *= 0.8  # Reduce speed to simulate energy loss
            
            
            #Collision with the trash
            if ball_rec.colliderect(trash_rec):
                ball_velocity = pygame.Vector2(0,0)

            # Collision with the hole
            if ball_rec.colliderect(hole_rec) and not game_finished:
                ball_velocity = pygame.Vector2(0, 0)
                game_finished = True
                show_end_screen("win", main, lambda: print("Back to Menu"))
            elif shots_taken >= MAX_SHOTS:
                game_finished = True
                show_end_screen("lose", main, lambda: print("Back to Menu"))

        # Update thief position (restricted to 100 pixels up and down)
        thief_rec.y += thief_direction * 3  # Adjust speed as necessary
        if thief_rec.y <= thief_start_y - thief_move_limit or thief_rec.y >= thief_start_y + thief_move_limit:
            thief_direction *= -1  # Reverse direction when hitting the movement range limits

        # Update car position
        car_rec.x += 2
        if car_rec.right > screen_width:
            car_rec.x = -car_rec.width  # Loop the car back to the start

        # Calculate shots left
        shots_left = MAX_SHOTS - shots_taken

        # Draw the game window
        draw_window(ball_rec, dragging, car_rec, start_pos, direction, MAX_SHOTS - shots_taken)


    pygame.quit()


if __name__ == "__main__":
    main()
    
    
    
    
    




'''        #load the object images and resize them
        flag_start = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/flag_start.png", 100, 85)
        hole = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/hoyo.png", 60, 90)
        ball = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/pelota.png", 25, 25)
        arrow = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/arrow.png", 20, 30,rotate = 270)
        car = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/car.png", 250, 140, rotate=270)
        bottles = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/bottles.png", 90, 83)
        thief = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/thief.png", 114, 106)
        bottles2 = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/bottles2.png", 89, 90)
        trash = load_image("Final proyect/Images/Nivel_4_recursos_mafialand/trash.png", 300, 150)
background_image = pygame.image.load(os.path.join("Final proyect/Images/Nivel_4_recursos_mafialand/fondo_mafialand.PNG"))
main_menu_button = pygame.image.load("Final proyect/Images/boton_play.png").convert_alpha()
play_again_button = pygame.image.load("Final proyect/Images/botones_levels_credits.png").convert_alpha()
            font = pygame.font.Font("Final proyect/Final proyect/fonts/BagelFatOne-Regular.ttf", 74)
            button_font = pygame.font.Font("Final proyect/Final proyect/fonts/BagelFatOne-Regular.ttf", 40)
            background_image = pygame.image.load(os.path.join("Final proyect/Images/Nivel_4_recursos_mafialand/fondo_mafialand.PNG"))
'''