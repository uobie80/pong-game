import pygame

pygame.init()

# Game clock
clock = pygame.time.Clock()

# Initialize FPS (frames per second)
speed = 30

# Setup display
display_width = 500
display_height = 300

# Set ball initial position, size, and speed
x = 100
y = 100
radius = 10
dx = 3
dy = 3

# Set paddle initial position, length and width
paddle_x = 10
paddle_y = 10
paddle_width = 3
paddle_height = 40

# Create display
display = pygame.display.set_mode((display_width, display_height))

# Set caption
pygame.display.set_caption("Let's Pong!")

# Game Loop
while True:

    # Limit frames per second to 30
    clock.tick(speed)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Set display color
    display.fill((0, 0, 0))

    # Render game
    # Add motion to ball
    x += dx
    y += dy

    # Draw paddle
    pygame.draw.rect(display, (255, 255, 255), (paddle_x,
                     paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(display, (255, 255, 255), (x, y), radius)

   # Check if ball hits right or left boundaries of display
    if (x < radius or x > display_width - radius):
        dx *= -1

    # Check if ball hits top or bottom boundaries of display
    if (y < radius) or (y > display_height - radius):
        dy *= -1

    # Update contents of display window
    pygame.display.update()
