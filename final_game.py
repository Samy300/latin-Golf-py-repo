import pygame
import sys
import os 
import math
import random
import time


# Initializing pygame and mixer
pygame.init()
pygame.mixer.init()

# Colors
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 225)
RED = (225, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set the screen 
screen_width, screen_height = 1345, 760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mafia's Golf")

#Load and scale the img
'''title_game = pygame.transform.scale(pygame.image.load("Final proyect v.S/Images/title_game.png"), (760, 400))
background_image = pygame.transform.scale(pygame.image.load("Final proyect v.S/Images/background_potencial.png"), (1345, 760))
play_button_image = pygame.transform.scale(pygame.image.load("Final proyect v.S/Images/boton_play.png").convert_alpha(), (190, 70))
levels_button_image = pygame.transform.scale(pygame.image.load("Final proyect v.S/Images/botones_levels_credits.png").convert_alpha(), (285, 135))
credits_button_image = pygame.transform.scale(pygame.image.load("Final proyect v.S/Images/botones_levels_credits.png").convert_alpha(), (300, 135))
logo_image = pygame.transform.scale(pygame.image.load("Final proyect v.S/Images/latin_mafia_logo.png").convert_alpha(), (3000, 900))
credits_card = pygame.transform.scale(pygame.image.load("Images/credits_card2.png").convert_alpha(), (1250, 750))
arrow_image_up = pygame.transform.scale(pygame.image.load("/Images/flecha_verde.png").convert_alpha(),  (100, 110))
arrow_image_down = pygame.transform.rotate(arrow_image_up, (180))
arrow_image_left = pygame.transform.rotate(arrow_image_up, (90))
arrow_image_right = pygame.transform.rotate(arrow_image_up, (270))
arrow_border_image_up = pygame.transform.scale(pygame.image.load("/Images/flecha_contorno.png").convert_alpha(),  (100, 110))
arrow_border_image_down = pygame.transform.rotate(arrow_border_image_up, (180))
arrow_border_image_left = pygame.transform.rotate(arrow_border_image_up, (90))
arrow_border_image_right = pygame.transform.rotate(arrow_border_image_up, (270))
level_display_image = pygame.transform.scale(pygame.image.load("/Images/carta_niveles.png"), (1100, 660))
level_previews = {
    1: pygame.transform.scale(pygame.image.load("/Images/level1_preview_image.png"), (755, 815)),
    2: pygame.transform.scale(pygame.image.load("/Images/level2_preview_image.png"), (755, 815)),
    3: pygame.transform.scale(pygame.image.load("/Images/level3_preview_image.png"), (755, 815)),
}'''


#function to load the font of the game for buttons and texts
def load_font(relative_path, size):
    base_path = os.path.dirname(__file__)  # Ruta del archivo actual
    absolute_path = os.path.join(base_path, relative_path)
    return pygame.font.Font(absolute_path, size)

# Load fonts
title_font = load_font("fonts/Caveat-VariableFont_wght.ttf", 150)
button_font = load_font("fonts/BagelFatOne-Regular.ttf", 50)



# Load music
pygame.mixer.music.load("musica/cancion__menu_1.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # Play in loop

#Global variables for the first 2 levels, all the elements that they all need 

#Creating a function that loads and scales at the same time all
def load_image(path, width, height, rotate=None):
    image = pygame.image.load(path)
    if rotate:
        image = pygame.transform.rotate(image, rotate)
    return pygame.transform.scale(image, (width, height))

preview_border = load_image("Images/borde_previeew_1try.png", 755, 815)

#loading the picture of the arrow that will be used for the ball
arrow = load_image("Images/arrow.png", 20, 30,rotate = 270)

#Load and scale the img for the main menu
title_game = load_image("Images/title_game.png", 760, 400)
background_image = load_image("Images/background_potencial.png", 1345, 760)
play_button_image = load_image("Images/boton_play.png", 190, 70)
levels_button_image = load_image("Images/botones_levels_credits.png", 285, 135)
credits_button_image = load_image("Images/botones_levels_credits.png", 300, 135)
logo_image = load_image("Images/latin_mafia_logo.png", 3000, 900)
credits_card = load_image("Images/credits_card2.png", 1250, 750)
arrow_image_up = load_image("Images/flecha_verde.png", 100, 110)
arrow_image_down = pygame.transform.rotate(arrow_image_up, (180))
arrow_image_left = pygame.transform.rotate(arrow_image_up, (90))
arrow_image_right = pygame.transform.rotate(arrow_image_up, (270))
arrow_border_image_up = load_image("Images/flecha_contorno.png", 100, 110)
arrow_border_image_down = pygame.transform.rotate(arrow_border_image_up, (180))
arrow_border_image_left = pygame.transform.rotate(arrow_border_image_up, (90))
arrow_border_image_right = pygame.transform.rotate(arrow_border_image_up, (270))
level_display_image = load_image("Images/carta_niveles.png", 1100, 660)
level_previews = {
    1: load_image("Images/level1_preview_image.png", 755, 815),
    2: load_image("Images/level2_preview_image.png", 755, 815),
    3: load_image("Images/level3_preview_image.png", 755, 815),
}

preview_border = load_image("Images/borde_previeew_1try.png", 755, 815)


#Global variables level 1 only!!!!
#Images level 1
ball = load_image('Images/pelota.png',25,25)
tree_1 = load_image("Images/Nivel_1_recursos_normal/arboles_2.png",225, 225)
tree_2 = load_image("Images/Nivel_1_recursos_normal/arboles_2.png",225, 225)
start_flag1 = load_image("Final proyect 2/Imagenes/flag_start.png",100, 85)
hole1 = load_image("Final proyect 2/Imagenes/hoyo.png",60,90)
lake_left_image = load_image("Images/Nivel_1_recursos_normal/lago_abajo_nivel_1.png",750, 750)
lake_right_image = load_image("Images/Nivel_1_recursos_normal/lago_arriba_nivel_1.png",370, 700)
lilducks_image = load_image("Images/Nivel_1_recursos_normal/patitos.png",150,150)
big_duck_image = load_image("Images/Nivel_1_recursos_normal/patote.png",125,125)
sand_image_top = load_image("Images/Nivel_1_recursos_normal/arena_arriba.png",280, 100)
sand_image_center = load_image("Images/Nivel_1_recursos_normal/arena1.png",360, 280,rotate=270)

def load_sound(relative_path):
    base_path = os.path.dirname(__file__)  # Ruta del archivo actual
    absolute_path = os.path.join(base_path, relative_path)
    return pygame.mixer.Sound(absolute_path)

splash_sound = load_sound("Images/Nivel_1_recursos_normal/splash_sound.mp3") #sound when the ball touches the lake

#Rectangles for objects in order for them to move or be able to do something within the game
ball_rec1 = pygame.Rect(239, 650, 25, 25)
start_flag_rec = pygame.Rect (215, 585,60,90)
hole1_rec = pygame.Rect(1100, 605,60,90)
tree_rec = [
    pygame.Rect(550, 665, 35, 35),  #rect left bottom
    pygame.Rect(500, 587, 120, 78),  #rect left 1
    pygame.Rect(468, 548, 191, 39), #rect left 2
    pygame.Rect(480, 505, 165, 39), #rect left 3
    pygame.Rect(1099, 267, 35, 35), #rect right bottom
    pygame.Rect(1050, 195, 120, 78), # rect right 1
    pygame.Rect(1023, 155, 191, 39), #rect right 2
    pygame.Rect(1035, 113, 165, 39), #rect right 3
]
#drawing the rectangles for the sand
sand_rec = [
    pygame.Rect(776, 50, 275, 57),  #rect top sand
    pygame.Rect(800, 107, 190, 43),  #rect top sand, bottom from the image
    
    pygame.Rect(1225, 390, 30, 90),  #rect last right on sand
    pygame.Rect(1190, 350, 45, 200),  #rect middle 1
    pygame.Rect(980, 330, 230, 230),  #rect middle 2
    
    pygame.Rect(940, 330, 40, 200), #rect right, for both
    pygame.Rect(910, 345, 30, 150),

    ]
#lake rec with duck
lake_left_rec = [
    pygame.Rect(260, 300, 227, 57),  # Rectangle 1
    pygame.Rect(328, 357, 212, 27),  # Rectangle 2
    pygame.Rect(319, 244, 212, 56), # rect 3
    pygame.Rect(530, 260, 47, 40), # rect 3
    pygame.Rect(320, 224, 183, 20), # rect 3
]

lake_right_rec = [
    pygame.Rect(705, 551, 130, 61),  # Rectangle 1
    pygame.Rect(705, 612, 98, 23),  # Rectangle 2
    pygame.Rect(788, 526, 45, 25), # rect 3
]

big_duck_rec = pygame.Rect(430,200,125,125)
# semi random locations to where the duck takes you
drop_locations = [ 
    (188, 71),
    (600, 300), 
    (102, 63),
    (427, 640),   
    ]
#Other variables to start the game
FPS = 60
ball_pos1 = pygame.Vector2(ball_rec1.x, ball_rec1.y)
ball_velocity = pygame.Vector2(0, 0)
max_power1 = 70
dragging = False
start_pos1 = pygame.Vector2()
direction1 = pygame.Vector2()
shots_taken = 0
MAX_SHOTS = 5
friction = 0.95
game_finished = False
duck_holding_ball = False
ignore_lake_collision = False
duck_cooldown = False

#function to restart the game level 1
def reset_game():
    global ball_velocity, ball_pos1, shots_taken, game_finished
    ball_velocity = pygame.Vector2(0, 0)
    ball_pos1 = pygame.Vector2(239, 650)
    shots_taken = 0
    game_finished = False



#Global variables LEVEL2 ONLY!!!
moving_speed = 3  # speed
moving_direction = 1  # direction
ball_motion = None  
dragging = False  # checks if you are moving the ball
start_x, start_y = 0, 0 
shots_taken = 0
game_finished = False        
#Loading the object images and resizing them
santa = load_image("Images/Nivel_2_recursos_navidad/santa_nivel_2.png",150, 150)  
start_flag = load_image('Final proyect 2/Imagenes/flag_start.png',100, 85)
win_hole = load_image("Final proyect 2/Imagenes/hoyo.png",60,90)   
ball_image = load_image('Final proyect 2/Imagenes/pelota.png',25,25)
wall1_image = load_image ('Images/Nivel_2_recursos_navidad/muro_regalos_2.png',80, 280, rotate = 90)
wall2_image = load_image('Images/Nivel_2_recursos_navidad/muro_regalos_2.png',80, 280, rotate = 90)
arrow = load_image("Final proyect 2/Imagenes/arrow.png", 20, 30,rotate = 270)
gift1 = load_image("Images/Nivel_2_recursos_navidad/regalo1_nivel_2.png", 100, 100)
gift2 = load_image("Images/Nivel_2_recursos_navidad/regalo2_nivel_2.png",100, 100)
gift3 = load_image("Images/Nivel_2_recursos_navidad/regalo3_nivel_2.png",100, 100)
gift4 = load_image("Images/Nivel_2_recursos_navidad/regalo4_nivel_2.png",100, 100)
gift_images = [gift1 , gift2, gift3, gift4]
last_gift_spawn = 0  # starts counting the time since the last one appeared
GIFT_SPAWN_RATE = 1500 # time between gifts
gifts = []
#The rectangles for the collisions and movements for the global variables level2 
hole_rect = pygame.Rect(1150, 150, 350,350)  #position of the hole
ball_rect = pygame.Rect(200, 620, 25, 25)
collision_rect_width = 80 # collision rectangles for the gift walls
collision_rect_height = 280  
wall1_collision_rect = pygame.Rect((screen_width // 4) - collision_rect_width // 2 + 50 + 20 + 150, 0, collision_rect_width, collision_rect_height)  # Mover 20 píxeles a la derecha
wall2_collision_rect = pygame.Rect(((screen_width // 4) * 2) - collision_rect_width // 2 + 200 + 20 + 80, screen_height - collision_rect_height, collision_rect_width, collision_rect_height)  # Mover 20 píxeles a la derecha
christmas_tree_rectangle1 = pygame.Rect(215, 200, 130, 75)  
christmas_tree_rectangle2 = pygame.Rect(255, 130, 65, 75)
lolipop_tree_1 = pygame.Rect(390, 530, 80, 120)  
lolipop_tree_2 = pygame.Rect(780, 110, 100, 120)
lolipop_tree_3 = pygame.Rect(1100, 440, 80, 120)  
santa_rect = pygame.Rect(1100,-20,150,150)  # collision rectangle for the ball, same size as the ball
# maximum power you con use for shooting the ball
MAX_POWER = 70
# shots limit
shots_left = 5
ball_velocity = pygame.Vector2(0, 0)  # Initial ball velocity

#movement of the ball level 2
class BallMovement:
    def __init__(self, startx, starty, velx, vely):
        self.x = startx
        self.y = starty
        self.velx = velx
        self.vely = vely

    def update_position(self):
        self.velx *= friction
        self.vely *= friction
        self.x += self.velx
        self.y += self.vely

    def is_moving(self):
        return abs(self.velx) > 0.1 or abs(self.vely) > 0.1

# gift walls movement
wall1_direction = 1
wall2_direction = -1
wall_speed = 4 

#Borders with the texts with the buttons
def render_botton_text_with_border(text, font, border_color, border_width, x, y):
    # Renderizar el texto del borde
    text_surface = font.render(text, True, border_color)
    text_rect = text_surface.get_rect(center=(x, y))
    

    for dx in range(-border_width, border_width + 1):
        for dy in range(-border_width, border_width + 1): 
            if dx != 0 or dy != 0:
                screen.blit(text_surface, (text_rect.x + dx, text_rect.y + dy))

# Function for the button
def draw_button(text, x, y):
    button_surface = button_font.render(text, True, (WHITE))
    button_rect = button_surface.get_rect(center=(x, y))
    render_botton_text_with_border(text, button_font, (BLACK), 2, x + 5, y + 5)
   
    
    # Obtener la posición del mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Comprobar si el mouse está sobre el botón
    if button_rect.collidepoint(mouse_x, mouse_y):
        # Desplazar el texto
        offset_x = 5  
        offset_y = -5 
    else:
        
        offset_x = 0
        offset_y = 0

    # Renderizar el texto con el desplazamiento
    text_rect = button_surface.get_rect(center=(x + offset_x, y - offset_y))
    screen.blit(button_surface, text_rect)

    return button_rect

# Helper function to draw text with border
def render_text_with_border(text, font, color, border_color, x, y):
    text_surface = font.render(text, True, border_color)
    text_rect = text_surface.get_rect(center=(x, y))
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if dx != 0 or dy != 0:
                screen.blit(text_surface, (text_rect.x + dx, text_rect.y + dy))
    screen.blit(font.render(text, True, color), text_rect)

# Function to display image buttons and return rectangle for click detection
def draw_image_button(image, x, y):
    button_rect = image.get_rect(center=(x, y))
    screen.blit(image, button_rect)
    return button_rect

def draw_image_border_button_right_arrow( image, border, x, y):
    # Get the button rectangle based on the image
    button_rect = image.get_rect(center=(x - 20, y))
    image_border = border.get_rect(center=(x , y))
    screen.blit(image, button_rect)  # Draw the button image on the screen
    screen.blit(border, image_border)

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Adjusting the position of the border if the mouse is over the button
    if image_border.collidepoint(mouse_x, mouse_y):
        offset_x = - 20
        offset_y = 0  # Move the border upward when hovered
    else:
        offset_x = 0
        offset_y = 0  # Reset border position

    # Draw the border or additional visual effect
    border_move = image_border.move(offset_x, offset_y)
    
    
    

    return button_rect and image_border

def draw_image_border_button_left_arrow( image, border, x, y):
    # Get the button rectangle based on the image
    button_rect = image.get_rect(center=(x - 5, y))
    image_border = border.get_rect(center=(x - 25 , y))
    screen.blit(image, button_rect)  # Draw the button image on the screen
    screen.blit(border, image_border)

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Adjust the position of the border if the mouse is over the button
    if image_border.collidepoint(mouse_x, mouse_y):
        offset_x = + 20
        offset_y = 0  # Move the border upward when hovered
    else:
        offset_x = 0
        offset_y = 0  # Reset border position

    # Draw the border or additional visual effect
    image_border.move(offset_x, offset_y)
    

    return button_rect

run = 0

def intro_screen(run):
      # Indicates that we will use the global variable
    if run == 0:

        # Intro screen 
        opacity = 255
        logo_rect = logo_image.get_rect(center=(screen_width // 2, screen_height // 2))
        while opacity > 0:
            screen.fill(BLACK)
            logo_image.set_alpha(opacity)
            screen.blit(logo_image, logo_rect)
            pygame.display.flip()
            pygame.time.delay(65)
            opacity -= 5
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        #Changing, so that it doesn't run again
        run += 1
                 

                    
# Function for each level
def level_1():
    reset_game()
    global dragging,ball_velocity,ball_pos1, max_power1, start_pos1,direction1,shots_taken,shots_left,game_finished
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Return to menu

        pygame.mixer.init()
        pygame.init()
        clock = pygame.time.Clock()

        # Setting main window
        screen_width, screen_height = 1345, 760
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Mafia's Golf")
        
        # Background
        
        background_image = pygame.image.load("Images/Nivel_1_recursos_normal/fondo_basico.jpg")  
        background_image = pygame.transform.rotate(background_image, 270)  # Rotate the image 270 degrees
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Scale to fit the screen
        
        font1 = pygame.font.SysFont(None, 35)
    
        def draw_window(ball_rec1, dragging, start_pos1, direction, shots_left):
            screen.blit(background_image, (0, 0))
            screen.blit(start_flag1, (start_flag_rec.x, start_flag_rec.y))
            screen.blit(lake_left_image, (85,-50))
            screen.blit(lake_right_image, (570, 240))
            screen.blit(tree_1, (457, 480)) #treee beside the lake 
            screen.blit(tree_2, (1010, 80))
            screen.blit(sand_image_center, (905, 300)) #Sand below the tree
            screen.blit(sand_image_top, (776, 50)) #sand top of the image
            screen.blit(hole1, (hole1_rec.x, hole1_rec.y))
            screen.blit(lilducks_image, (320, 200))
            screen.blit(big_duck_image, (big_duck_rec.x, big_duck_rec.y))
            screen.blit(ball, (ball_rec1.x, ball_rec1.y))

            font = pygame.font.Font(None, 40)
            shots_text = font.render(f"Shots Left: {shots_left}", True, WHITE)
            screen.blit(shots_text, (10, 10))

            if dragging:
                mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                direction = mouse_pos - pygame.Vector2(ball_rec1.center)
                if direction.length() > 0:
                    angle = math.degrees(math.atan2(direction.y, direction.x))
                    rotated_arrow = pygame.transform.rotate(arrow, -angle)
                    arrow_offset = 30
                    offset_x = direction.normalize().x * arrow_offset
                    offset_y = direction.normalize().y * arrow_offset
                    arrow_pos = (ball_rec1.centerx + offset_x, ball_rec1.centery + offset_y)
                    arrow_rect = rotated_arrow.get_rect(center=arrow_pos)
                    screen.blit(rotated_arrow, arrow_rect.topleft)

            pygame.display.update()
        
        
        
         #MThe clamps were implemented in order fix a bug of the duck   
        def clamp_to_screen_bounds(drop_location):
            screen_width, screen_height = 1345, 760
            drop_x, drop_y = drop_location

            # Clamp the drop_location coordinates to be within the screen bounds
            drop_x = max(0, min(screen_width - 1, drop_x))
            drop_y = max(0, min(screen_height - 1, drop_y))

            return drop_x, drop_y

        
        def clamp_ball_position(ball, screen_width, screen_height):
            # Clamp the drop_location coordinates to be within the screen bounds
            ball_rec1.x = max(0, min(screen_width - ball_rec1.width, ball_rec1.x))
            ball_rec1.y = max(0, min(screen_height - ball_rec1.height, ball_rec1.y))


        def reset_ball_by_duck():
            global ball_velocity, ball_pos1, duck_holding_ball, duck_cooldown

            # Drop the ball at a safe location
            valid_drop = False
            attempts = 0
            while not valid_drop and attempts < 10:
                drop_location = random.choice(drop_locations)
                drop_x, drop_y = clamp_to_screen_bounds(drop_location)
                # Ensuring that the drop location is NOT in any lake
                if not any(lake.colliderect(pygame.Rect(drop_x, drop_y, 25, 25)) for lake in lake_left_rec + lake_right_rec):
                    valid_drop = True
                attempts += 1

            if not valid_drop:
                drop_x, drop_y = 239, 650

            # Set ball position and stop movement
            ball_pos1.x, ball_pos1.y = drop_x, drop_y
            ball_velocity = pygame.Vector2(0, 0)

            # Clamp ball to ensure it's within screen bounds
            clamp_ball_position(ball_rec1, 1345, 760)

            # Ensure the duck releases the ball properly
            duck_holding_ball = False
            duck_cooldown = True

            # Redraw the scene to reflect the ball's new position
            draw_window(ball_rec1, dragging, start_pos1, direction1, MAX_SHOTS - shots_taken)
            pygame.display.flip()

            # Cooldown to prevent immediate re-pickup
            pygame.time.set_timer(pygame.USEREVENT + 1, 2000)


        
        


        #Define the function on what to do if the ball collides with the duck
        def duck_collision(ball_x,ball_y):
            global ball, duck_x, duck_y, ball_rec1, duck_holding_ball, duck_cooldown,shots_taken,ball_velocity

            if duck_holding_ball or duck_cooldown:
                return  # If the duck is already holding the ball or is in cooldown, do nothing

            pygame.time.set_timer(pygame.USEREVENT + 1, 2000)
            
            #New postion of the ball
            ball_pos = pygame.Vector2(ball_x, ball_y)

            # Random drop location
            drop_location = pygame.Vector2(random.choice(drop_locations))

            #Start from the current duck position
            duck_pos = pygame.Vector2(big_duck_rec.x, big_duck_rec.y)
            direction_to_target = (drop_location - duck_pos).normalize()
            duck_speed = 5  

            #Setting theat the duck is holding the ball
            duck_holding_ball = True

            # Take the duck along with the ball to the destination
            while duck_pos.distance_to(drop_location) > 10:
                screen.blit(background_image, (0, 0))
                screen.blit(start_flag1, (start_flag_rec.x, start_flag_rec.y))
                screen.blit(lake_left_image, (85, -50))
                screen.blit(lake_right_image, (570, 240))
                screen.blit(tree_1, (457, 480))  
                screen.blit(tree_2, (1010, 80))
                screen.blit(sand_image_center, (905, 300)) 
                screen.blit(sand_image_top, (776, 50))  
                screen.blit(hole1, (hole1_rec.x, hole1_rec.y))

                # Moving the duck and the ball together
                duck_pos += direction_to_target * duck_speed
                ball_rec1.x, ball_rec1.y = duck_pos.x + 20, duck_pos.y + 20  #Adjust the ball positon
                screen.blit(big_duck_image, (duck_pos.x, duck_pos.y))
                screen.blit(ball, (ball_rec1.x, ball_rec1.y))

                pygame.display.flip()
                clock.tick(60)

            #Once the duck reaches the location where the duck droped it, the ball stays stationary
            ball_pos.x, ball_pos.y = drop_location.x, drop_location.y
            ball_rec1.x, ball_rec1.y = drop_location.x, drop_location.y
            
            # Update ball velocity to reset it after being dropped
            ball_velocity = pygame.Vector2(0, 0)

            # Going back to where it was(duck)
            direction_to_home = pygame.Vector2(duck_pos) - duck_pos
            if direction_to_home.length() > 0:  # Only normalize if the vector length is greater than zero
                direction_to_home = direction_to_home.normalize()

            while duck_pos.distance_to(duck_pos) > 10:
                screen.blit(background_image, (0, 0))
                screen.blit(start_flag1, (start_flag_rec.x, start_flag_rec.y))
                screen.blit(lake_left_image, (85, -50))
                screen.blit(lake_right_image, (570, 240))
                screen.blit(tree_1, (457, 480))  # Árbol al lado del lago
                screen.blit(tree_2, (1010, 80))
                screen.blit(sand_image_center, (905, 300))  # Arena debajo del árbol
                screen.blit(sand_image_top, (776, 50))  # Arena en la parte superior
                screen.blit(hole1, (hole1_rec.x, hole1_rec.y))
                screen.blit(big_duck_image, (duck_pos.x, duck_pos.y))
                screen.blit(ball, (ball_pos.x, ball_pos.y))
            pygame.display.flip()
            clock.tick(60)

            #Once the duck is back to its initial position, restore its state
            duck_x, duck_y = duck_pos
            duck_holding_ball = False  # duck no longer holding the ball
            #Set cooldown to prevent the duck from immediately picking up another ball
            duck_cooldown = True
            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  #cooldown of 1 second only!!
            
            reset_ball_by_duck()


        #This will be for show_end screen, once the user clicks the button of playing again it will reset the game
        def reset_level_1():
            global ball_rec1, ball_velocity, shots_taken, game_finished, duck_holding_ball, duck_cooldown
            global tree_rec, sand_rec, lake_left_rec, lake_right_rec, hole1_rec, ball_pos1

            #Reset ball position
            ball_rec1 = pygame.Rect(239, 650, 25, 25) 
            ball_velocity = pygame.Vector2(0, 0)
            ball_pos1 = pygame.Vector2(ball_rec1.x, ball_rec1.y)

            # Reset shot counter and completion status
            shots_taken = 0
            game_finished = False

            #Reset the duck state
            duck_holding_ball = False
            duck_cooldown = False

            #Reset   the hole position and below will be the rest of the values that were previously mentioned before in the global var
            hole1_rec = pygame.Rect(1100, 605, 60, 90)  # Posición inicial del hoyo
            tree_rec = [
                pygame.Rect(550, 665, 35, 35),  
                pygame.Rect(500, 587, 120, 78),  
                pygame.Rect(468, 548, 191, 39),  
                pygame.Rect(480, 505, 165, 39),  
                pygame.Rect(1099, 267, 35, 35),  
                pygame.Rect(1050, 195, 120, 78), 
                pygame.Rect(1023, 155, 191, 39), 
                pygame.Rect(1035, 113, 165, 39), 
            ]
            sand_rec = [
                pygame.Rect(776, 50, 275, 57), 
                pygame.Rect(800, 107, 190, 43), 
                pygame.Rect(1225, 390, 30, 90), 
                pygame.Rect(1190, 350, 45, 200),
                pygame.Rect(980, 330, 230, 230),
                pygame.Rect(940, 330, 40, 200),
                pygame.Rect(910, 345, 30, 150),
            ]
            lake_left_rec = [
                pygame.Rect(260, 300, 227, 57),
                pygame.Rect(328, 357, 212, 27),
                pygame.Rect(319, 244, 212, 56),
                pygame.Rect(530, 260, 47, 40),
                pygame.Rect(320, 224, 183, 20),
            ]

            lake_right_rec = [
                pygame.Rect(705, 551, 130, 61),
                pygame.Rect(705, 612, 98, 23),
                pygame.Rect(788, 526, 45, 25),
            ]

            # Redraw the window
            draw_window(ball_rec1, False, ball_pos1, pygame.Vector2(0, 0), 5)
            pygame.display.update()


        #Modify the ending screen to reset the game state when playing again or going back to menu
        def show_end_screen(result, level_restart_function2, main_menu):
            screen = pygame.display.get_surface()
            screen_width, screen_height = screen.get_size()
            end_screen_running = True

            main_menu_button = pygame.image.load("Final proyect 2/Final proyect/Imagenes/boton_play.png").convert_alpha()
            play_again_button = pygame.image.load("Final proyect 2/Final proyect/Imagenes/botones_levels_credits.png").convert_alpha()

            main_menu_button = pygame.transform.scale(main_menu_button, (250, 70))
            play_again_button = pygame.transform.scale(play_again_button, (290, 120))

            main_menu_rect = main_menu_button.get_rect(center=(screen_width // 3, 2 * screen_height // 3))
            play_again_rect = play_again_button.get_rect(center=(2 * screen_width // 3, 2 * screen_height // 3))

            font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 74)
            button_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 40)

            while end_screen_running:
                screen.fill((0, 0, 0))

                message = "Congratulations!" if result == "win" else "Game Over!"
                text = font.render(message, True, (255, 255, 255))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 3))
                screen.blit(text, text_rect)

                screen.blit(main_menu_button, main_menu_rect.topleft)
                screen.blit(play_again_button, play_again_rect.topleft)

                main_menu_text = button_font.render("Main Menu", True, (0, 0, 0))
                play_again_text = button_font.render("Play Again", True, (0, 0, 0))
                screen.blit(main_menu_text, main_menu_text.get_rect(center=main_menu_rect.center))
                screen.blit(play_again_text, play_again_text.get_rect(center=play_again_rect.center))

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if main_menu_rect.collidepoint(mouse_pos):
                            end_screen_running = False
                            main_menu()
                        elif play_again_rect.collidepoint(mouse_pos):
                            end_screen_running = False
                            reset_level_1()  # Starts the level again with the variables resetted
                            level_1()  # go back to level 1
                
                            
                            
            

        #Main loop of the level 1
        running = True
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN and shots_taken < MAX_SHOTS:
                    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                    if ball_rec1.collidepoint(mouse_pos) and ball_velocity.length() == 0:
                        dragging = True
                        start_pos = mouse_pos

                elif event.type == pygame.MOUSEBUTTONUP and dragging and shots_taken < MAX_SHOTS:
                    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                    direction = mouse_pos - ball_pos1
                    power = min(direction.length(), max_power1)
                    if direction.length() > 0:
                        ball_velocity = direction.normalize() * power * 0.3
                        shots_taken += 1
                    dragging = False

                
            if ball_velocity.length() > 0:
                ball_pos1 += ball_velocity
                ball_velocity *= friction
                ball_rec1.topleft = (ball_pos1.x, ball_pos1.y)
                if ball_velocity.length() < 0.5:
                    ball_velocity = pygame.Vector2(0, 0)

                if ball_rec1.top <= 51 or ball_rec1.bottom >= 700:
                    ball_velocity.y *= -1
                if ball_rec1.left <= 103 or ball_rec1.right >= 1260:
                    ball_velocity.x *= -1
                    
                # Check collisions with trees
                for rect in tree_rec:
                    if ball_rec1.colliderect(rect):
                        ball_velocity *= -0.8  # Reduce speed and bounce back

                # Check collisions with sand (reduce speed more significantly)
                for rect in sand_rec:
                    if ball_rec1.colliderect(rect):
                        ball_velocity *= 0.5  # Reduce speed further

                # Check if ball falls into a lake
                # Inside your ball collision checking (for lakes)
                for rect in lake_left_rec:
                    if ball_rec1.colliderect(rect):
                        if ball_velocity.length() > 0:  # Ball is moving
                            ball_velocity = pygame.Vector2(0, 0)  # Stop the ball
                            pygame.mixer.Sound.play(splash_sound)  # Play splash sound
                            # Call duck interaction only for the left lake
                            duck_collision(ball_rec1.x, ball_rec1.y)

                # Make sure the ball doesn't interact with the right lake (no duck)
                for rect in lake_right_rec:
                    if ball_rec1.colliderect(rect):
                        if ball_velocity.length() > 0:  # Ball is moving
                            ball_velocity = pygame.Vector2(0, 0)  # Stop the ball
                            pygame.mixer.Sound.play(splash_sound)  # Play splash sound
                            
                        

                # Check if ball enters the hole, open ending screen 
                if ball_rec1.colliderect(hole1_rec) and not game_finished:
                    ball_velocity = pygame.Vector2(0, 0)
                    game_finished = True
                    show_end_screen("win", level_1, main_menu)
                        
                if shots_taken >= MAX_SHOTS and not game_finished and ball_velocity.length() == 0:
                    game_finished = True
                    show_end_screen("lose", level_1, main_menu)
                    
            


            draw_window(ball_rec1, dragging, start_pos1, direction1, MAX_SHOTS - shots_taken)

        pygame.quit()




#Function for level 2
def level_2():
    #Starting the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # creates the window
        screen_width, screen_height = 1345, 760
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Mafia's Golf")

        # setting the background
        background_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        background = load_image('Images/Nivel_2_recursos_navidad/fondo_navidad.jpg', screen_width, screen_height, rotate = 90)
        #background = pygame.transform.rotate(background, 90)
        #background = pygame.transform.scale(background, (screen_width, screen_height))
        
        # Fonts
        font1 = pygame.font.SysFont(None, 35)
        # font for the remaining shots
        font2 = pygame.font.SysFont(None, 50)  
        # draws the gifts and move them
        def draw_gifts():
            global gift
            for gift in gifts[:]:
                gift_image, gift_rect, speed = gift
                gift_rect.y += speed  # moves the giftd
                if gift_rect.top > screen_height:
                    gifts.remove(gift)  # deletes the gifts if they go out of the window
                else:
                    screen.blit(gift_image, (gift_rect.x, gift_rect.y))
            
        
        def draw_santa():
            
            global santa_rect, moving_speed, moving_direction

            # Draws the santa image
            screen.blit(santa, santa_rect)

            # defines santas movement
            santa_rect.x += moving_speed * moving_direction

            # checks for collision with walls and makes it change direction
            if santa_rect.left <= 0 or santa_rect.right >= screen_width:
                moving_direction *= -1  # Changes direction

        def draw_walls():
            global wall1_direction, wall2_direction

            # places the images inside the rectangles
            wall1_center_x = wall1_collision_rect.x + (wall1_collision_rect.width - wall1_image.get_width()) // 2
            wall1_center_y = wall1_collision_rect.y + (wall1_collision_rect.height - wall1_image.get_height()) // 2
            wall2_center_x = wall2_collision_rect.x + (wall2_collision_rect.width - wall2_image.get_width()) // 2
            wall2_center_y = wall2_collision_rect.y + (wall2_collision_rect.height - wall2_image.get_height()) // 2

            # draws the images
            screen.blit(wall1_image, (wall1_center_x, wall1_center_y))
            screen.blit(wall2_image, (wall2_center_x, wall2_center_y))

            # gift walls movements
            wall1_collision_rect.y += wall_speed * wall1_direction
            wall2_collision_rect.y += wall_speed * wall2_direction

            # this makes the walls change direction when collide with the window edges
            if wall1_collision_rect.top <= 0 or wall1_collision_rect.bottom >= screen_height:
                wall1_direction *= -1
            if wall2_collision_rect.top <= 0 or wall2_collision_rect.bottom >= screen_height:
                wall2_direction *= -1
                
        def draw_ball():
            # draws the ball inside the collisions rectangle
            screen.blit(ball_image, (ball_rect.x, ball_rect.y))    
                
        def walls_collision():
            global ball_velocity

            # Collisions with the wall 1
            if ball_rect.colliderect(wall1_collision_rect):
                if ball_rect.right > wall1_collision_rect.left and ball_rect.left < wall1_collision_rect.left:
                    # Collision with the left side
                    ball_velocity.x = -abs(ball_velocity.x)
                    ball_rect.right = wall1_collision_rect.left
                elif ball_rect.left < wall1_collision_rect.right and ball_rect.right > wall1_collision_rect.right:
                    # Collision with the right side
                    ball_velocity.x = abs(ball_velocity.x)
                    ball_rect.left = wall1_collision_rect.right
                elif ball_rect.bottom > wall1_collision_rect.top and ball_rect.top < wall1_collision_rect.top:
                    #Collision with the upper side
                    ball_velocity.y = -abs(ball_velocity.y)
                    ball_rect.bottom = wall1_collision_rect.top
                elif ball_rect.top < wall1_collision_rect.bottom and ball_rect.bottom > wall1_collision_rect.bottom:
                    # Collision with the bottom side
                    ball_velocity.y = abs(ball_velocity.y)
                    ball_rect.top = wall1_collision_rect.bottom

            # Collisions with the wall 2
            if ball_rect.colliderect(wall2_collision_rect):  
                if ball_rect.right > wall2_collision_rect.left and ball_rect.left < wall2_collision_rect.left:
                    # Collision with the left side
                    ball_velocity.x = -abs(ball_velocity.x)
                    ball_rect.right = wall2_collision_rect.left
                elif ball_rect.left < wall2_collision_rect.right and ball_rect.right > wall2_collision_rect.right:
                    # COlision with the right side
                    ball_velocity.x = abs(ball_velocity.x)
                    ball_rect.left = wall2_collision_rect.right
                elif ball_rect.bottom > wall2_collision_rect.top and ball_rect.top < wall2_collision_rect.top:
                    # Collision with the upper side
                    ball_velocity.y = -abs(ball_velocity.y)
                    ball_rect.bottom = wall2_collision_rect.top
                elif ball_rect.top < wall2_collision_rect.bottom and ball_rect.bottom > wall2_collision_rect.bottom:
                    # Collision with the bottom side
                    ball_velocity.y = abs(ball_velocity.y)
                    ball_rect.top = wall2_collision_rect.bottom

        def objects_collisions():
            global ball_velocity

            # Collisions with every other rectangle
            rects = [christmas_tree_rectangle1, christmas_tree_rectangle2, lolipop_tree_1, lolipop_tree_2, lolipop_tree_3]

            for rect in rects:
                if ball_rect.colliderect(rect):
                    # Collisions with any side of the rectangle
                    if ball_rect.right > rect.left and ball_rect.left < rect.left:
                        # Left side
                        ball_velocity.x = -abs(ball_velocity.x)
                        ball_rect.right = rect.left
                    elif ball_rect.left < rect.right and ball_rect.right > rect.right:
                        # Right side
                        ball_velocity.x = abs(ball_velocity.x)
                        ball_rect.left = rect.right
                    elif ball_rect.bottom > rect.top and ball_rect.top < rect.top:
                        # Top side
                        ball_velocity.y = -abs(ball_velocity.y)
                        ball_rect.bottom = rect.top
                    elif ball_rect.top < rect.bottom and ball_rect.bottom > rect.bottom:
                        # Bottom side
                        ball_velocity.y = abs(ball_velocity.y)
                        ball_rect.top = rect.bottom

        def window_collision():
            # collisions with the window edges
            global ball_motion

            # here I check for the horizontal edges
            if ball_rect.left <= 0:
                ball_rect.left = 0
                if ball_motion:
                    ball_motion.velx *= -1
            elif ball_rect.right >= screen_width:
                ball_rect.right = screen_width
                if ball_motion:
                    ball_motion.velx *= -1

            # and here for the vertical
            if ball_rect.top <= 0:
                ball_rect.top = 0
                if ball_motion:
                    ball_motion.vely *= -1
            elif ball_rect.bottom >= screen_height:
                ball_rect.bottom = screen_height
                if ball_motion:
                    ball_motion.vely *= -1


        def  collision_gifts():
            global ball_rect, gifts, ball_motion

            # checks for collisions of the gifts with the ball
            for gift_image, gift_rect, speed in gifts[:]:
                if ball_rect.colliderect(gift_rect):
                    # if there is a collision with a gift, we send the ball back to the start position
                    ball_rect.x = 220  # X position of the ball
                    ball_rect.y = screen_height - 150  # Y position 
                    
                    # Restarts the balls movement
                    if ball_motion:
                        ball_motion = None  # stop the previous movement of the ball
                    return True  # means there was a collision with a gift

            return False  # No collisions with gifts            
                
        # Funcition to restart the setting of the game for level 2
        def reset_game_state():
            global ball_rect, ball_velocity, shots_left, game_finished, gifts, santa_rect
            global wall1_collision_rect, wall2_collision_rect, moving_direction, wall1_direction, wall2_direction

            ball_rect = pygame.Rect(220, screen_height - 150, ball_image.get_width(), ball_image.get_height())
            ball_velocity = pygame.Vector2(0, 0)
            shots_left = 5  
            game_finished = False
            gifts = []  
            #Restart the positions of everything in the level
            santa_rect = pygame.Rect(1100, -20, 150, 150)
            wall1_collision_rect.y = 0
            wall2_collision_rect.y = screen_height - wall2_collision_rect.height
            moving_direction = 1
            wall1_direction = 1
            wall2_direction = -1
     

        # The other end screen for level 2, same as 1 but with the diference that calls other values
        def show_end_screen(result, level_reset, main_menu):
            screen = pygame.display.get_surface()
            screen_width, screen_height = screen.get_size()
            end_screen_running = True

            main_menu_button = pygame.image.load("Final proyect 2/Final proyect/Imagenes/boton_play.png").convert_alpha()
            play_again_button = pygame.image.load("Final proyect 2/Final proyect/Imagenes/botones_levels_credits.png").convert_alpha()

            main_menu_button = pygame.transform.scale(main_menu_button, (250, 70))
            play_again_button = pygame.transform.scale(play_again_button, (290, 120))

            main_menu_rect = main_menu_button.get_rect(center=(screen_width // 3, 2 * screen_height // 3))
            play_again_rect = play_again_button.get_rect(center=(2 * screen_width // 3, 2 * screen_height // 3))

            font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 74)
            button_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 40)

            while end_screen_running:
                screen.fill((0, 0, 0))

                message = "Congratulations!" if result == "win" else "Game Over!"
                text = font.render(message, True, (255, 255, 255))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 3))
                screen.blit(text, text_rect)

                screen.blit(main_menu_button, main_menu_rect.topleft)
                screen.blit(play_again_button, play_again_rect.topleft)

                main_menu_text = button_font.render("Main Menu", True, (0, 0, 0))
                play_again_text = button_font.render("Play Again", True, (0, 0, 0))
                screen.blit(main_menu_text, main_menu_text.get_rect(center=main_menu_rect.center))
                screen.blit(play_again_text, play_again_text.get_rect(center=play_again_rect.center))

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if main_menu_rect.collidepoint(mouse_pos):
                            end_screen_running = False
                            main_menu()
                        elif play_again_rect.collidepoint(mouse_pos):
                            end_screen_running = False
                            reset_game_state()  
                            level_2()  # Restarts game 2
                
                                                  
       #main loop for level 2                 
        def main():
            global BallMovement, shots_left, dragging, ball_velocity, friction, game_finished,arrow,last_gift_spawn
            run = True
            clock = pygame.time.Clock()

            while run:
                dt = clock.tick(60) / 1000  # Delta time in seconds

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if shots_left > 0: # This only happens if you still have shots
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if ball_rect.collidepoint(mouse_x, mouse_y) and ball_velocity.length() == 0:
                                dragging = True 
                                start_pos = pygame.Vector2(mouse_x, mouse_y)

                        if event.type == pygame.MOUSEBUTTONUP and dragging:
                            dragging = False
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            direction = pygame.Vector2(mouse_x, mouse_y) - pygame.Vector2(ball_rect.center)
                            if direction.length() > 0:
                                power = min(direction.length(), 70)  # Limits the max power
                                ball_velocity = direction.normalize() * power * 0.3  # adjusts the speed based on the power, will always be the same
                                shots_left -= 1  # Reduces the shots left by one 
                                
                # Updates the position of the ball
                if ball_velocity.length() > 0:
                    ball_rect.x += ball_velocity.x
                    ball_rect.y += ball_velocity.y
                    ball_velocity *= friction  #Apply friction to gradually stop the ball
                    if ball_velocity.length() < 0.5:
                        ball_velocity = pygame.Vector2(0, 0)  #Stops the ball if the speed is low

                #Calls for collisions
                walls_collision()
                objects_collisions()
                window_collision()
                collision_gifts()

                # Screen limit
                if ball_rect.left <= 0 or ball_rect.right >= screen_width:
                    ball_velocity.x *= -1  # Horizontal bounce
                if ball_rect.top <= 0 or ball_rect.bottom >= screen_height:
                    ball_velocity.y *= -1  # Vertical bounce
                
                
                current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
                if current_time - last_gift_spawn > GIFT_SPAWN_RATE:  # Check if enough time has passed
                    last_gift_spawn = current_time  # Update the last spawn time

                    # Randomly choose an image for the gift
                    gift_image = random.choice(gift_images)
                    gift_rect = gift_image.get_rect()

                    # Generate the position of the gifts from Santa's position
                    gift_rect.x = santa_rect.centerx - gift_rect.width // 2  # x-position centered with Santa
                    gift_rect.y = santa_rect.centery  # y-position right where Santa is
                    
                    speed = random.randint(2, 5)  # Random speed for the gifts
                    gifts.append((gift_image, gift_rect, speed))  # Adding the gift to the list of gifts
                    
                screen.blit(background, (0, 0))
                screen.blit(start_flag, (175, 565))
                screen.blit(win_hole, (1150, 150))
                draw_santa()
                draw_walls()
                draw_ball()
                draw_gifts()

                # Draw the arrow while dragging
                if dragging:
                    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                    direction = mouse_pos - pygame.Vector2(ball_rect.center)

                    if direction.length() > 0:
                        angle = math.degrees(math.atan2(direction.y, direction.x))
                        rotated_arrow = pygame.transform.rotate(arrow, -angle)

                        # Position of the arrow in front of the ball
                        offset = direction.normalize() * 30
                        arrow_pos = pygame.Vector2(ball_rect.center) + offset
                        arrow_rect = rotated_arrow.get_rect(center=arrow_pos)
                        screen.blit(rotated_arrow, arrow_rect.topleft)

                #Shots left
                shots_text = font1.render(f"Shots left: {shots_left}", True, (0, 0, 0))  
                text_rect = shots_text.get_rect()
                text_rect.topleft = (10, 10) 
                pygame.draw.rect(screen, (255, 255, 255), text_rect)
                screen.blit(shots_text, text_rect.topleft)

                # Hole collision reaction 
                if ball_rect.colliderect(hole_rect) and not game_finished:
                    ball_velocity = pygame.Vector2(0, 0)
                    game_finished = True
                    show_end_screen("win", level_2, main_menu)
                    
                if shots_left <= 0 and not game_finished and ball_velocity.length() == 0:
                    game_finished = True
                    show_end_screen("lose", level_2, main_menu)

                
                pygame.display.update()

            pygame.quit()

        main()       

def level_3():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        global thief_direction  # Declare global if shared with other parts of the program

        clock = pygame.time.Clock()  # FPS control

        # Ball setup
        ball_rec = pygame.Rect(100, 690, 25, 25)  # Ball rectangle for tracking
        
        # Screen setup
        screen_width, screen_height = 1345, 760
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Mafia's Golf")

        # Load background image
        background_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        background_image = pygame.image.load(os.path.join("Final proyect 2/Imagenes/Nivel_4_recursos_mafialand/fondo_mafialand.PNG"))
        background_image = pygame.transform.rotate(background_image, -90)
        background_image = pygame.transform.scale(background_image, (1345, 760))
        background_surface.blit(background_image, (0, 0))
        background_surface.set_alpha(220)  # Adjusting the transparency of the bg

        # Load images and scale them, set a function which imports the image and sets the width and height so it's easier and cleaner to load the image on each onject
        def load_image(path, width, height, rotate=None):
            image = pygame.image.load(path)
            if rotate:
                image = pygame.transform.rotate(image, rotate)
            return pygame.transform.scale(image, (width, height))

        #load the object images and resize them
        flag_start = load_image("Final proyect 2/Imagenes/flag_start.png", 100, 85)
        hole = load_image("Final proyect 2/Imagenes/hoyo.png", 60, 90)
        ball = load_image("Final proyect 2/Imagenes/pelota.png", 25, 25)
        arrow = load_image("Final proyect 2/Imagenes/arrow.png", 20, 30,rotate = 270)
        car = load_image("Final proyect 2/Imagenes/Nivel_4_recursos_mafialand/car.png", 250, 140, rotate=270)
        bottles = load_image("Final proyect 2/Imagenes/Nivel_4_recursos_mafialand/bottles.png", 90, 83)
        thief = load_image("Final proyect 2/Imagenes/Nivel_4_recursos_mafialand/thief.png", 114, 106)
        bottles2 = load_image("Final proyect 2/Imagenes/Nivel_4_recursos_mafialand/bottles2.png", 89, 90)
        trash = load_image("Final proyect 2/Imagenes/Nivel_4_recursos_mafialand/trash.png", 300, 150)


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
                # Recalculate the direction vector of the ball (it will be dynamic
                # )
                mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                direction = mouse_pos - pygame.Vector2(ball_rec.center)

                if direction.length() > 0:  # Ensure the vector isn't zero
                    angle = math.degrees(math.atan2(direction.y, direction.x))  # Calculate angle in degrees
                    rotated_arrow = pygame.transform.rotate(arrow, -angle)

                    # Offset distance to position the arrow in front of the ball
                    arrow_offset = 30  # value for the distance from the ball
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
                # Generate random x and y coordinates in the screen 
                x = random.randint(0, screen_width - ball_rec.width)
                y = random.randint(0, screen_height - ball_rec.height)
                
                # Ensure the random position is not within the hole area
                if not hole_rec.colliderect(pygame.Rect(x, y, ball_rec.width, ball_rec.height)):
                    return pygame.Vector2(x, y)  # Return as a pygame.Vector2 object
                

        #Endscreen once the game is over, go back to main menu or play again
        def show_end_screen(result, level_restart_function, main_menu):
            screen = pygame.display.get_surface()  # Get the screen surface
            screen_width, screen_height = screen.get_size()  # Get the screen dimensions
            end_screen_running = True
            
            # Preload button images
            main_menu_button = pygame.image.load("Final proyect 2/Final proyect/Imagenes/boton_play.png").convert_alpha()
            play_again_button = pygame.image.load("Final proyect 2/Final proyect/Imagenes/botones_levels_credits.png").convert_alpha()
            
            # Scale buttons to appropriate sizes
            main_menu_button = pygame.transform.scale(main_menu_button, (250, 70))
            play_again_button = pygame.transform.scale(play_again_button, (290, 120))

            
            #Button rectangles for interaction
            main_menu_rect = main_menu_button.get_rect(center=(screen_width // 3, 2 * screen_height // 3))
            play_again_rect = play_again_button.get_rect(center=(2 * screen_width // 3, 2 * screen_height // 3))

            # Fonts for text
            #Font for the buttons and messsage
            font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 74)
            button_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 40)

            while end_screen_running:
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
                            end_screen_running = False
                            main_menu()  # Redirect to the main menu
                        elif play_again_rect.collidepoint(mouse_pos):
                            end_screen_running = False
                            level_restart_function()  # Restart the game'''


        # Game FPS
        FPS = 60
        # to track the thief's initial position and movement direction
        thief_start_y = 610  # Initial Y position
        thief_direction = 1  # 1 for moving down, -1 for moving up
        thief_move_limit = 100  # Maximum movement range 

        # Main game loop
        def main():
            global thief_direction, friction
            
            clock = pygame.time.Clock()  # FPS control
            ball_rec = pygame.Rect(100, 690, 25, 25)  # Ball rectangle for tracking
            ball_pos = pygame.Vector2(ball_rec.x, ball_rec.y)  # Ball position vector
            ball_velocity = pygame.Vector2(0, 0)  # Initial ball velocity 
            max_power = 70  # Max power of shot
            dragging = False
            start_pos = pygame.Vector2()  # Track where the dragging of the ball starts
            direction = pygame.Vector2()  # Direction for the arrow
            shots_taken = 0  # Counter for shots taken
            MAX_SHOTS = 5  # Maximum number of shots allowed
            thief_collision_cooldown = 0  # Cooldown timer for thief collision
            game_finished = False
            running = True

            while running:
                clock.tick(FPS)

                # Reduce the cooldown timer
                if thief_collision_cooldown > 0:
                    thief_collision_cooldown -= 1

                # Loop through all the events
                for event in pygame.event.get():
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

                    # Collision with the hole, and finishing the game  
                    if ball_rec.colliderect(hole_rec) and not game_finished:
                        ball_velocity = pygame.Vector2(0, 0)
                        game_finished = True
                        show_end_screen("win", level_3, main_menu)
                    
                    elif shots_left <= 0 and not game_finished and ball_velocity.length() == 0:
                        game_finished = True
                        show_end_screen("lose", level_3, main_menu)
                # Update thief position (restricted to 100 pixels up and down)
                thief_rec.y += thief_direction * 3  # Adjust speed as necessary
                if thief_rec.y <= thief_start_y - thief_move_limit or thief_rec.y >= thief_start_y + thief_move_limit:
                    thief_direction *= -1  # Reverse direction when hitting the movement range limits

                # Update car position
                car_rec.x += 2.5
                if car_rec.right > screen_width:
                    car_rec.x = -car_rec.width  # Loop the car back to the start


                # Draw the game window
                draw_window(ball_rec, dragging, car_rec, start_pos, direction, MAX_SHOTS - shots_taken)


            pygame.quit()
        main()

#Functions to switch from level to level on the main screen without getting the end screen first
def switch_level(level):
    global game_finished
    # Reset the game state before loading a new level
    reset_game()  # Ensure ball and game state are reset
    game_finished = False
    if level == 1:
        level_1()
    elif level == 2:
        level_2()
    elif level == 3:
        level_3()


#Main menu of the game in general
def main_menu():
    in_levels_view = False  # Controls whether we are in level selection view
    current_level = 1  #Current level shown on the card
    max_levels = 3  # Maximum number of levels available
    card_x = screen_width + 100
    card_y = screen_height // 2 - 50  # Initial card position off-screen
    card_target_x = screen_width // 2 + 15
    card_target_y = screen_height // 2 - 50 #Target card position
    animation_speed = 20  # Card entrance animation speed

    in_credits_view = False
    credits_card_x = screen_width + 100
    credits_card_y = screen_height // 2 - 50  #Initial card position off-screen
    credits_card_target_x = screen_width // 2 + 15  
    credits_card_target_y = screen_height // 2 - 50 #Target position of the card
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if not in_levels_view:
                    if play_button_rect.collidepoint(mouse_x, mouse_y):
                        in_levels_view = True
                        card_x = screen_width + 100
                else:
                    # Navigation in the level chart
                    right_arrow_rect = pygame.Rect(screen_width // 2 + 260, screen_height // 2 - 40, 80, 60)
                    left_arrow_rect = pygame.Rect(screen_width // 2 - 300, screen_height // 2 - 40, 80, 60)
                    back_button_rect = pygame.Rect(screen_width // 2 - 105, screen_height - 100, 190, 80)
                    if right_arrow_rect.collidepoint(mouse_x, mouse_y) and current_level < max_levels:
                        current_level += 1
                    elif left_arrow_rect.collidepoint(mouse_x, mouse_y) and current_level > 1:
                        current_level -= 1
                    elif back_button_rect.collidepoint(mouse_x, mouse_y):
                        in_levels_view = False

                    elif play_button_rect.collidepoint(mouse_x, mouse_y):
                        #Load the corresponding level
                        switch_level(current_level)


                if not in_credits_view: 
                    if credits_button_rect.collidepoint(mouse_x, mouse_y):
                        in_credits_view = True
                        credits_card_x = screen_width + 100
                else: 
                    if back_button_rect.collidepoint(mouse_x, mouse_y):
                        in_credits_view = False
        screen.blit(background_image, (0, 0))

        if in_levels_view:
            # Level card entrance animation
            if card_x > card_target_x and card_y == card_target_y:
                card_x -= animation_speed

            # Draw the level card
            card_levels = draw_image_button(level_display_image, card_x, card_y)
            play_button_rect = draw_image_button(play_button_image, card_x, screen_height // 2 + 135 )
            draw_button("PLAY", card_x, screen_height // 2 + 125)
            level_text = render_text_with_border(f"Level {current_level}", button_font, BLACK, WHITE, card_x, 60)

            preview_image = level_previews.get(current_level)
            if preview_image:
                preview_x = card_x - 172 #Adjust the position according to your design
                preview_y = card_y - 480
                screen.blit(preview_image, (preview_x - 200, preview_y))
            

            #Navigation arrows and back button
            if current_level > 1:
                draw_image_button(arrow_image_left, card_x - 275, screen_height // 2)
                draw_image_border_button_left_arrow(arrow_image_left, arrow_border_image_left, card_x - 265, screen_height // 2)
            if current_level < max_levels:
                draw_image_button(arrow_image_right, card_x + 275, screen_height // 2)
                draw_image_border_button_right_arrow(arrow_image_right, arrow_border_image_right, card_x + 295, screen_height // 2)
            back_button_rect = pygame.Rect(screen_width // 2 - 45, screen_height - 50, 100, 50)
            draw_image_button(levels_button_image, screen_width // 2 + 5, screen_height - 50)
            draw_button("Back", screen_width // 2 + 10, screen_height - 60)
            
            
        elif in_credits_view:
            #Credit card input animation
            if credits_card_x > card_target_x and credits_card_y == card_target_y:
                credits_card_x -= animation_speed

            # Draw the credit card
            card_credits = draw_image_button(credits_card, credits_card_x, credits_card_y)

            # Botón "Back"
            back_button_rect = pygame.Rect(screen_width // 2 - 45, screen_height - 60, 100, 50)
            draw_image_button(levels_button_image, screen_width // 2 + 5, screen_height - 50)
            draw_button("Back", screen_width // 2 + 10, screen_height - 60)
              
        else:
            #Main menu
            draw_image_button(title_game, screen_width // 2 + 15, 225)
            play_button_rect = draw_image_button(play_button_image, screen_width // 2, screen_height // 2 + 50)
            credits_button_rect = draw_image_button(credits_button_image, screen_width // 2, screen_height // 2 + 160)
            draw_button("PLAY", screen_width // 2, screen_height // 2 + 40)
            draw_button("CREDITS", screen_width // 2, screen_height // 2 + 150)

        pygame.display.flip()
        pygame.display.update()



def main(): 

    if run == 0:
     intro_screen(run)
     main_menu()
     
    else :
    
     main_menu(run)

main()
