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

# Define functions to detect collisions


def hit_back():
    """
    Function to detect is ball hit left wall
    """
    if x + radius > display_width:
        return True
    return False


def hit_sides():
    """
    Function to detect is ball hit top or bottom walls
    """
    if y - radius < 0:
        return True
    if y + radius > display_height:
        return True
    return False


def hit_paddle():
    """
    Function to detect if ball hit paddle
    """
    if x - radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
        return True
    return False


def game_over():
    """
    Function to exit out of game
    """
    exit


# Game Loop
while True:

    # Limit frames per second to 30
    clock.tick(speed)

   # poll for events
   # Get key user pressed
    pressed_key = pygame.key.get_pressed()

    # Check if down or S key was pressed
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height + 10 <= display_height:
            paddle_y += 10

    # Check if Up or W key was pressed
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y - 10 >= 0:
            paddle_y -= 10

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
    # if (x < radius or x > display_width - radius):
    if x < radius:
        game_over()
    if hit_back() or hit_paddle():
        dx *= -1

    # Check if ball hits top or bottom boundaries of display
    # if (y < radius) or (y > display_height - radius):
    if hit_sides():
        dy *= -1

    # Update contents of display window
    pygame.display.update()
