import pygame
pygame.init()

win_width = 700
win_height = 500

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Ping Pong")
bg_color = (0, 0, 0)
win.fill(bg_color)

clock = pygame.time.Clock()
FPS = 120

game = True

while game:
    win.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(FPS)

quit()