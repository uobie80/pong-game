import pygame

pygame.init()

# Game clock
clock = pygame.time.Clock()

# Initialize FRPS (frame rate per second)
speed = 30

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


while True:
    # Limit frames per second to speed
    clock.tick(speed)

    # Set display color
    display.fill((0, 0, 0))

    # Add motion to ball
    x += dx
    y += dy

    # Draw ball
    pygame.draw.circle(display, (255, 255, 255), (x, y), radius)

   # Check if ball hits right or left boundaries
    if (x < radius or x > display_width - radius):
        dx *= -1
    # Check if ball hits top or bottom boundaries
    if (y < radius) or (y > display_height - radius):
        dy *= -1

    # Update contents of display window
    pygame.display.update()
