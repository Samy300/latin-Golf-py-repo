import pygame
import sys
import mafialand_level

# Inicializar el módulo de mixer
pygame.mixer.init()
# Inicia Pygame
pygame.init()


# Colores
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Configurar la pantalla
screen_width, screen_height = 1345, 760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mafia's Golf")
background_image = pygame.image.load("Final proyect 2/Final proyect/Images/fondo_lets_golf4.png")  # Imagen de fondo
# Fuentes
title_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/Caveat-VariableFont_wght.ttf", 150)  # Título
button_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 50)  # Botones
# Cargar imagen de botón
play_button_image = pygame.image.load("Final proyect 2/Final proyect/Images/boton_play.png").convert_alpha()  
levels_button_image = pygame.image.load("Final proyect 2/Final proyect/Images/botones_levels_credits.png").convert_alpha()
credits_button_image = pygame.image.load("Final proyect 2/Final proyect/Images/botones_levels_credits.png").convert_alpha()
arrow_button_up = pygame.image.load("Final proyect 2/Images/arrow_button.png").convert_alpha()
arrow_button_down = pygame.transform.rotate(arrow_button_up, (180))
arrow_button_right = pygame.transform.rotate(arrow_button_up, (90))
arrow_button_left = pygame.transform.rotate(arrow_button_up, (270))
# Cambia a las dimensiones deseadas
play_button_image = pygame.transform.scale(play_button_image, (190, 70))  
levels_button_image = pygame.transform.scale(levels_button_image, (285, 135))  
credits_button_image = pygame.transform.scale(credits_button_image, (300, 135)) 
# Título del juego
title_text = title_font.render("Mafia's Golf", True, YELLOW)
# Cargar la música de fondo
pygame.mixer.music.load("Final proyect 2/Final proyect/musica/cancion__menu_1.mp3") 
pygame.mixer.music.set_volume(0.5)  # Volumen
pygame.mixer.music.play(-1)  # Reproduce en bucle
# Cargar el logo
logo_image = pygame.image.load("Final proyect 2/Final proyect/Images/latin_mafia_logo.png").convert_alpha()
# Escalar el logo si es necesario
logo_image = pygame.transform.scale(logo_image, (3000, 900))  # Ajusta el tamaño deseado

"""
# Playlist
def play_next_song():
    global current_song_index
    pygame.mixer.music.load(playlist[current_song_index])  # Cargar la canción actual
    pygame.mixer.music.play()  # Reproducir la canción
    current_song_index = (current_song_index + 1) % len(playlist)  # Avanzar al siguiente índice en bucle

# Configurar el índice inicial y reproducir la primera canción
current_song_index = 0
play_next_song()

# Configurar evento para detectar cuando una canción termina
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

"""

def intro_screen():
    # Cargar el logo
    logo_image = pygame.image.load("Final proyect 2/Final proyect/Images/latin_mafia_logo.png").convert_alpha()
    logo_image = pygame.transform.scale(logo_image, (3000, 900))  # Ajusta el tamaño del logo

    # Centrar el logo
    logo_rect = logo_image.get_rect(center=(screen_width // 2, screen_height // 2))
    
    # Variable opacidad
    opacity = 255
    fade_out = True  # Controla si la imagen se desvanece

    while True:
        screen.fill(BLACK)  # Fondo negro para la pantalla de carga

        # Ajustar opacidad del logo
        logo_image.set_alpha(opacity)
        screen.blit(logo_image, logo_rect)  # Dibujar el logo en el centro de la pantalla

        # Controlar el desvanecimiento
        if fade_out:
            opacity -= 5  # Reducir opacidad
            if opacity <= 0:
                break  # Salir del bucle cuando esté completamente desvanecido
        else:
            opacity += 5  # Aumentar opacidad

        pygame.display.flip()  # Actualizar pantalla
        pygame.time.delay(65)  # Controla la velocidad del desvanecimiento

        # Procesar eventos para permitir el cierre de la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Borde solo para el titulo porque me equivoque :)
def render_text_with_border(text, font, border_color, border_width, offset=(0, 0)):
    # Renderizar el texto del borde
    text_surface = font.render(text, True, border_color)
    text_rect = text_surface.get_rect()

    for dx in range(-border_width, border_width + 1):
        for dy in range(-border_width, border_width + 1): 
            if dx != 0 or dy != 0:  
                screen.blit(text_surface, (text_rect.x + dx + offset[0], text_rect.y + dy + offset[1]))

# Bordes para los textos con botones
def render_botton_text_with_border(text, font, border_color, border_width, x, y):
    # Renderizar el texto del borde
    text_surface = font.render(text, True, border_color)
    text_rect = text_surface.get_rect(center=(x, y))
    

    for dx in range(-border_width, border_width + 1):
        for dy in range(-border_width, border_width + 1): 
            if dx != 0 or dy != 0:
                screen.blit(text_surface, (text_rect.x + dx, text_rect.y + dy))


# Función para poner botones
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

def draw_image_button(image, x, y):
    # Acomodar los botones
    button_rect = image.get_rect(center=(x, y))  # Obtiene el rectángulo de la imagen para centrar la imagen
    screen.blit(image, button_rect)  # Dibuja la imagen

    
    return button_rect  # Detección de clics

# Llamar a la pantalla de carga antes del menú principal
intro_screen()


def main_menu():

    # Cerrar la ventana sin forzarla
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            """ # En caso de uso de una playlist
                for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                  elif event.type == pygame.USEREVENT + 1:  # Detectar cuando termina una canción
                   play_next_song()  # Reproducir la siguiente canción

                    """
            
            

        screen.blit(background_image, (0, 0))  # Dibujar fondo 
        render_text_with_border("Mafia's Golf", title_font, (BLACK), 2, offset=(350, 60))  # Borde negro
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 60))  # Centrar el título
        
        
 
        # Colocar las imágenes para los botones
        play_button_rect = draw_image_button(play_button_image, screen_width // 2, screen_height // 2 - 50)
        levels_button_rect = draw_image_button(levels_button_image, screen_width // 2 - 3, screen_height // 2 + 60)
        credits_button_rect = draw_image_button(credits_button_image, screen_width // 2, screen_height // 2 + 170)
        
        
        # Dibujar el texto de los botones
        play_button = draw_button("PLAY", screen_width // 2, screen_height // 2 - 60)
        levels_button = draw_button("LEVELS", screen_width // 2, screen_height // 2 + 50)
        credits_button = draw_button("CREDITS", screen_width // 2, screen_height // 2 + 160)
        

        pygame.display.flip()  # Actualizar la pantalla

        # Comprobar si se hace clic en un botón
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Si se hace clic
            if play_button.collidepoint(mouse_x, mouse_y):
                print("Iniciar juego")
            elif levels_button.collidepoint(mouse_x, mouse_y):
               levels_screen()  # Llamar a la pantalla de niveles
            elif credits_button.collidepoint(mouse_x, mouse_y):
                credits_screen()

def play_button_function():

    # Falta trabajar en ello
    pygame.display.flip()

def levels_screen():
    running = True
    current_level = 1  # Iniciar mostrando el nivel 1
    max_levels = 4     # Cambia esto según la cantidad de niveles que tengas
    button_size = (200, 80)

    # Fuentes
    button_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 40)
    levels_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/Caveat-VariableFont_wght.ttf", 80)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Detectar clic en botón de nivel
                level_button_rect = pygame.Rect(screen_width // 2 - button_size[0] // 2, screen_height // 2 - button_size[1] // 2, *button_size)
                if level_button_rect.collidepoint(mouse_x, mouse_y):
                    print(f"Nivel {current_level} seleccionado")  # Aquí iniciarías el nivel

                # Detectar clic en flecha derecha
                right_arrow_rect = pygame.Rect(screen_width - 100, screen_height // 2 - 40, 60, 60)
                if right_arrow_rect.collidepoint(mouse_x, mouse_y) and current_level < max_levels:
                    current_level += 1

                # Detectar clic en flecha izquierda
                left_arrow_rect = pygame.Rect(40, screen_height // 2 - 40, 60, 60)
                if left_arrow_rect.collidepoint(mouse_x, mouse_y) and current_level > 1:
                    current_level -= 1

        # Dibujar fondo
        screen.fill(GREEN)

        # Título de la pantalla
        levels_text = levels_font.render("Select Level", True, WHITE)
        screen.blit(levels_text, (screen_width // 2 - levels_text.get_width() // 2, 50))

        # Dibujar botón de nivel
        level_button_rect = pygame.Rect(screen_width // 2 - button_size[0] // 2, screen_height // 2 - button_size[1] // 2, *button_size)
        pygame.draw.rect(screen, YELLOW, level_button_rect)
        
        # Etiqueta del botón de nivel
        level_text = button_font.render(f"Level {current_level}", True, BLACK)
        text_rect = level_text.get_rect(center=level_button_rect.center)
        screen.blit(level_text, text_rect)

        # Dibujar flechas de navegación
        # Flecha izquierda (solo si no estamos en el primer nivel)
        if current_level > 1:
            pygame.draw.polygon(screen, WHITE, [(10, screen_height // 2), (40, screen_height // 2 - 30), (40, screen_height // 2 + 30)])

        # Flecha derecha (solo si no estamos en el último nivel)
        if current_level < max_levels:
            pygame.draw.polygon(screen, WHITE, [(screen_width - 10, screen_height // 2), (screen_width - 40, screen_height // 2 - 30), (screen_width - 40, screen_height // 2 + 30)])

        pygame.display.flip()

def credits_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Regresar al menú si presionan "ESC"
                    running = False

        # Colorear el fondo
        screen.fill(BLACK)

        # Dibujar el logo
        logo_rect = logo_image.get_rect(center=(660, 400))  # Centrar el logo en la parte superior
        screen.blit(logo_image, logo_rect)
        
        # Texto de créditos
        credits_font = pygame.font.Font("Final proyect 2/Final proyect/fonts/BagelFatOne-Regular.ttf", 40)
        credits_text = credits_font.render("CREDITS", True, WHITE)
        screen.blit(credits_text, (screen_width // 2 - credits_text.get_width() // 2, 50))

        # Bordes de los creditos
        render_text_with_border("Developer: LatinMafia team", credits_font, BLACK, 2, offset=(418, 150))
        render_text_with_border("Lead Programmer: [Nombre]", credits_font, BLACK, 2, offset=(410, 200))
        render_text_with_border("Game Designer: [Nombre]", credits_font, BLACK, 2, offset=(436, 250))
        render_text_with_border("Art Director: [Nombre]", credits_font, BLACK, 2, offset=(458, 300))
        render_text_with_border("Sound Design: [Nombre]", credits_font, BLACK, 2, offset=(450, 350))
        render_text_with_border("Voice Acting: [Nombre]", credits_font, BLACK, 2, offset=(458, 400))
        render_text_with_border("Quality Assurance: [Nombre]", credits_font, BLACK, 2, offset=(405, 450))
        render_text_with_border("Level Designer: [Nombre]", credits_font, BLACK, 2, offset=(440, 500))
        

        # Listar nombres y roles (puedes personalizar estos)
        team_text = [
            "Developer: LatinMafia team",
            "Lead Programmer: [Nombre]",
            "Game Designer: [Nombre]",
            "Art Director: [Nombre]",
            "Sound Design: [Nombre]",
            "Voice Acting: [Nombre]",
            "Quality Assurance: [Nombre]",
            "Level Designer: [Nombre]",
        ]

        
        for i, line in enumerate(team_text):
            line_surface = credits_font.render(line, True, WHITE)
            screen.blit(line_surface, (screen_width // 2 - line_surface.get_width() // 2, 150 + i * 50))

        
            
        

        # Actualizar pantalla
        pygame.display.flip()

# Iniciar el menú
main_menu()


