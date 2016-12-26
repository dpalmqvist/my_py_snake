import pygame, sys
from snake import Snake
from snack import Snack
pygame.init()

FPS = 5 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 500), 0, 32)
pygame.display.set_caption('Snake!')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BOARDWIDTH = 400
BOARDHEIGHT = 400

HEADWIDTH = 10
HEADHEIGHT = 10

headx = 200
heady = 200
direction = 'right'
snake = Snake()
snack = Snack(BOARDWIDTH, BOARDWIDTH, snake)
point_font = pygame.font.Font(pygame.font.get_default_font(), 15)

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                snake.turn(event.key)
            elif event.key == pygame.K_SPACE:
                snake.extend()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, BOARDWIDTH, BOARDHEIGHT), 2)

    snack.step()
    if not snack.alive():
        snack = Snack(BOARDWIDTH, BOARDHEIGHT, snake)

    snake.step(snack)
    if not snake.alive(BOARDWIDTH, BOARDHEIGHT):
        print snake.length
        pygame.quit()
        sys.exit()
    snake.draw(DISPLAYSURF)
    snack.draw(DISPLAYSURF)
    label = point_font.render("Score: %d"%snake.length, 0, (127,0,127))
    DISPLAYSURF.blit(label, (10, 410))
    pygame.display.update()
    fpsClock.tick(5 + snake.length)