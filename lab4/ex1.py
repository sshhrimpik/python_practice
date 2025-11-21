import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angry Smiley")

GRAY   = (220, 220, 220)
YELLOW = (255, 255,   0)
RED    = (255,   0,   0)
BLACK  = (0,   0,   0)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)

    center = (300, 330)
    radius = 170
    pygame.draw.circle(screen, YELLOW, center, radius)

    left_eye_center  = (240, 300)
    right_eye_center = (360, 300)
    outer_eye_radius = 35
    inner_eye_radius = 15

    pygame.draw.circle(screen, RED,   left_eye_center, outer_eye_radius)
    pygame.draw.circle(screen, RED,   right_eye_center, outer_eye_radius)

    pygame.draw.circle(screen, BLACK, left_eye_center, inner_eye_radius)
    pygame.draw.circle(screen, BLACK, right_eye_center, inner_eye_radius)

    eyebrow_width = 15
    pygame.draw.line(screen, BLACK, (180, 250), (280, 290), eyebrow_width)  # left
    pygame.draw.line(screen, BLACK, (320, 290), (420, 250), eyebrow_width)  # right

    mouth_rect = pygame.Rect(230, 400, 140, 30)
    pygame.draw.rect(screen, BLACK, mouth_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
