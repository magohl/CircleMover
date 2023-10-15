import pygame

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410

BLACK = (  0,   0,   0)
#WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Circle Mover")

circle = pygame.draw.circle(screen, RED, (100,100), 50)
circle_draging = False

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if circle.collidepoint(event.pos):
                    circle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = circle.x - mouse_x
                    offset_y = circle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                circle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if circle_draging:
                mouse_x, mouse_y = event.pos
                circle.x = mouse_x + offset_x
                circle.y = mouse_y + offset_y

    screen.fill(BLACK)

    pygame.draw.circle(screen, RED, (circle.x, circle.y), 50)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()