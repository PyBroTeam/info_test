# The test program based on Pygame
# Importing Pygame and sys moduls
import pygame

# Initialize Pygame
pygame.init()

# Screen
scr = pygame.display.set_mode(size=[600, 400])  # Set screen size parameters
pygame.display.get_surface().fill((255, 255, 255))  # Surface color WHITE
pygame.display.set_caption("Best game")  # Set screen captcha

# Load a background
background = pygame.image.load("D:\Python\pygame_background\pic01.jpg")
background.convert()

scr.blit(background, (0, 0))


# Draw rectangle
def draw_rect():
    for i in range(0, 200, 5):
        # Renewing background
        scr.blit(background, (0, 0))

        # Rectangle
        pygame.draw.rect(scr, (255, 0, 0), (i, i, 60, 60), 2, 10)
        pygame.draw.rect(scr, (255, 0, 0), (300 - i, 300 - i, 60, 60), 2, 10)
        pygame.draw.rect(scr, (255, 0, 0), (300 + i, 300 - i, 60, 60), 2, 10)

        # Update screen after object moving
        pygame.display.update()

        # Clock for screen update per second
        pygame.time.Clock().tick(25)


# Cycle for keeping game run
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            quit()

    draw_rect()

    # Update screen
    pygame.display.update()

    # Limits FPS to 30
    pygame.time.Clock().tick(30)

pygame.quit()
