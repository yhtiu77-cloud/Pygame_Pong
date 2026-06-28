import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

# paddle settings
paddle_width = 15
paddle_height = 100
speed = 6

# left paddle
left_x = 50
left_y = height // 2 - paddle_height // 2

# right paddle
right_x = width - 50 - paddle_width
right_y = height // 2 - paddle_height // 2

running = True

ball_x = 400
ball_y = 300
ball_speed_x = 4
ball_speed_y = 4



left_score = 0
right_score = 0

font = pygame.font.Font(None, 50)
text = font.render(f"{left_score} : {right_score}", True, (255,255,255))

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = 400
    ball_y = 300
    ball_speed_x *= -1



while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # controls (player 1)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        left_y -= speed
    if keys[pygame.K_s]:
        left_y += speed

    # controls (player 2)
    if keys[pygame.K_UP]:
        right_y -= speed
    if keys[pygame.K_DOWN]:
        right_y += speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x < 10:
        right_score += 1
        reset_ball()

    if ball_x > width - 10:
        left_score += 1
        reset_ball()


    # draw
    screen.fill((0, 0, 0))

    left_paddle = pygame.draw.rect(screen, (255, 255, 255), (left_x, left_y, paddle_width, paddle_height))
    right_paddle = pygame.draw.rect(screen, (255, 255, 255), (right_x, right_y, paddle_width, paddle_height))
    ball = pygame.draw.circle(screen, (255,255,255), (ball_x, ball_y), 10)
    screen.blit(text,(width // 2 - 30, 20))


    if ball_x < 10 or ball_x > 790:
        ball_speed_x = ball_speed_x * -1
    if ball_y <= 10 or ball_y >= height - 10:
        ball_speed_y *= -1




    if ball.colliderect(left_paddle):
        ball_speed_x *= -1

    if ball.colliderect(right_paddle):
        ball_speed_x *= -1


    text = font.render(f"{left_score} : {right_score}", True, (255,255,255))
    screen.blit(text,(width // 2 - 30, 20))

    pygame.display.update()

pygame.quit()
