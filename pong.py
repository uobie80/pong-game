import pygame
import random

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

# Initialize game score
game_score = 0

# Create display
display = pygame.display.set_mode((display_width, display_height))

# Set caption
pygame.display.set_caption("Let's Pong!")

# Define functions to detect collisions


def randomize_start():
    """
    Function to set random starting position of ball
    """
    global x, y, dy
    x = random.randint(int(display_width/4), display_width - 20)
    y = random.randint(10, display_height - 10)
    if random.randint(0, 2) % 2 == 0:
        dy *= -1


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
    global game_score
    if x - radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
        game_score += 100
        return True
    return False


def game_over():
    """
    Function to exit out of game if user presses specific keys
    """
    global game_score
    end_game = True

    # Clear screen before displaying text
    display.fill((0, 0, 0))

    font_title = pygame.font.Font(None, 36)
    font_instructions = pygame.font.Font(None, 24)

    # Create game over text
    announcement = font_title.render("Game Over", True, (255, 255, 255))

    # Create surface to hold text
    announcement_rect = announcement.get_rect(
        center=(int(display_width/2), int(display_height/3)))

    # Copy game over text onto surface
    display.blit(announcement, announcement_rect)

    # Set instructions to proceed
    qinstructions = font_instructions.render(
        "Press q to Quit", True, (255, 255, 255))
    qinstructions_rect = qinstructions.get_rect(
        center=(int(display_width/2), int(display_height/1.5)))
    display.blit(qinstructions, qinstructions_rect)

    # Allow user to resume play
    rinstructions = font_instructions.render(
        "Press r to Resume", True, (255, 255, 255))
    rinstructions_rect = rinstructions.get_rect(
        center=(int(display_width/2), int(display_height/1.3)))
    display.blit(rinstructions, rinstructions_rect)

    # Display final game score
    final_score = "Final score: " + str(game_score)
    score_announce = font_instructions.render(
        final_score, True, (255, 255, 255))
    score_announce_rect = score_announce.get_rect(
        center=(int(display_width/2), int(display_height/2)))
    display.blit(score_announce, score_announce_rect)

    # Display game over text
    pygame.display.flip()

    while(end_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    end_game = False


# Clear screen
display.fill((0, 0, 0))

# Display welcome screen
welcome_screen = pygame.font.Font(None, 30)
welcome = welcome_screen.render("Let's Play Pong!", True, (255, 255, 255))
welcome_rect = welcome.get_rect(
    center=(int(display_width/2), int(display_height/3)))

startmsg = welcome_screen.render(
    "Hit 'y' to start, or autostart in 10 seconds", True, (255, 255, 255))
startmsg_rect = startmsg.get_rect(
    center=(int(display_width/2), int(display_height/4)))
display.blit(welcome, welcome_rect)
display.blit(startmsg, startmsg_rect)
pygame.display.flip()

# Pause for 5 seconds
pygame.time.set_timer(pygame.USEREVENT, 10000)

# Catch timer and keydown event
timer_active = True
while (timer_active):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            timer_active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                timer_active = False

randomize_start()

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

        # Reset game
        randomize_start()
        dx = abs(dx)  # Reset ball to travel toward the back wall
        game_score = 0
    if hit_back() or hit_paddle():
        dx *= -1

    # Check if ball hits top or bottom boundaries of display
    # if (y < radius) or (y > display_height - radius):
    if hit_sides():
        dy *= -1

    # Update contents of display window
    pygame.display.update()
