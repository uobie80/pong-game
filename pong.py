import pygame

pygame.init()

# Setup display
display_width = 500
display_height = 300


# Set ball size, initial position, and speed
x = 100
y = 100
radius = 10
dx = 3
dy = 3

# Create display
display = pygame.display.set_mode((display_width, display_height))

# Set caption
pygame.display.set_caption("Let's Pong!")

# Set display color
display.fill((0, 0, 0))

# draw ball
pygame.draw.circle(display, (255, 255, 255), (x, y), radius)

# Update contents of display window
pygame.display.update()

while True:
    stayopen = True
