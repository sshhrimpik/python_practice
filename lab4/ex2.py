import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("House Scene")

SKY        = (170, 230, 255)
GRASS      = (0, 150, 0)
HOUSE      = (140, 90, 10)
ROOF       = (230, 60, 80)
WINDOW     = (10, 130, 150)
TREE_TRUNK = (0, 0, 0)
TREE_LEAF1 = (0, 90, 0)
TREE_LEAF2 = (0, 70, 0)
SUN        = (255, 180, 200)
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    pygame.draw.rect(screen, GRASS, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    house_rect = pygame.Rect(130, 220, 200, 150)
    pygame.draw.rect(screen, HOUSE, house_rect)
    pygame.draw.rect(screen, BLACK, house_rect, 2)  # outline

    roof_points = [(130, 220), (230, 130), (330, 220)]
    pygame.draw.polygon(screen, ROOF, roof_points)
    pygame.draw.polygon(screen, BLACK, roof_points, 2)

    win_rect = pygame.Rect(190, 260, 70, 60)
    pygame.draw.rect(screen, WINDOW, win_rect)
    pygame.draw.rect(screen, BLACK, win_rect, 2)

    cloud_y = 140
    cloud_x = 380
    radius = 35
    offsets = [(-50, 0), (-20, -25), (20, -10), (50, 5)]
    for ox, oy in offsets:
        center = (cloud_x + ox, cloud_y + oy)
        pygame.draw.circle(screen, WHITE, center, radius)
        pygame.draw.circle(screen, BLACK, center, radius, 2)

    trunk_rect = pygame.Rect(560, 260, 25, 120)
    pygame.draw.rect(screen, TREE_TRUNK, trunk_rect)

    leaf_centers = [(555, 230), (595, 230), (575, 200), (575, 270)]
    for i, (cx, cy) in enumerate(leaf_centers):
        color = TREE_LEAF1 if i < 3 else TREE_LEAF2
        pygame.draw.circle(screen, color, (cx, cy), 45)
        pygame.draw.circle(screen, BLACK, (cx, cy), 45, 2)

    sun_center = (700, 90)
    sun_radius = 35

    pygame.draw.circle(screen, SUN, sun_center, sun_radius)

    for angle in range(0, 360, 15):
        rad = math.radians(angle)
        x = sun_center[0] + int((sun_radius + 10) * math.cos(rad))
        y = sun_center[1] + int((sun_radius + 10) * math.sin(rad))
        pygame.draw.circle(screen, SUN, (x, y), 6)

    pygame.draw.circle(screen, BLACK, sun_center, sun_radius + 10, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
