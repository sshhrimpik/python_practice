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



def draw_house(surface, x, y, w, h):
    body_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, HOUSE, body_rect)
    pygame.draw.rect(surface, BLACK, body_rect, 2)

    roof_height = int(h * 0.75)
    apex_x = x + w // 2
    apex_y = y - roof_height // 2
    roof_points = [(x, y), (apex_x, apex_y), (x + w, y)]
    pygame.draw.polygon(surface, ROOF, roof_points)
    pygame.draw.polygon(surface, BLACK, roof_points, 2)

    win_w = int(w * 0.33)
    win_h = int(h * 0.38)
    win_x = x + (w - win_w) // 2
    win_y = y + (h - win_h) // 2
    win_rect = pygame.Rect(win_x, win_y, win_w, win_h)
    pygame.draw.rect(surface, WINDOW, win_rect)
    pygame.draw.rect(surface, BLACK, win_rect, 2)


def draw_tree(surface, trunk_rect, leaf_centers, radius):
    pygame.draw.rect(surface, TREE_TRUNK, trunk_rect)

    for i, (cx, cy) in enumerate(leaf_centers):
        color = TREE_LEAF1 if i < len(leaf_centers) - 1 else TREE_LEAF2
        pygame.draw.circle(surface, color, (cx, cy), radius)
        pygame.draw.circle(surface, BLACK, (cx, cy), radius, 2)


def draw_cloud(surface, base_x, base_y, radius):
    offsets = [(-45, 0), (-15, -22), (20, -10), (45, 4)]
    for ox, oy in offsets:
        center = (base_x + ox, base_y + oy)
        pygame.draw.circle(surface, WHITE, center, radius)
        pygame.draw.circle(surface, BLACK, center, radius, 2)


def draw_sun(surface, center, main_radius, bump_radius=7, step=15):
    pygame.draw.circle(surface, SUN, center, main_radius)

    outer_r = main_radius + bump_radius + 3
    for angle in range(0, 360, step):
        rad = math.radians(angle)
        x = center[0] + int(outer_r * math.cos(rad))
        y = center[1] + int(outer_r * math.sin(rad))
        pygame.draw.circle(surface, SUN, (x, y), bump_radius)

    pygame.draw.circle(surface, BLACK, center, outer_r + 2, 2)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)
    pygame.draw.rect(screen, GRASS, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    draw_sun(screen, center=(85, 80), main_radius=30)

    draw_cloud(screen, base_x=230, base_y=120, radius=30)  # left big
    draw_cloud(screen, base_x=410, base_y=110, radius=25)  # middle smaller
    draw_cloud(screen, base_x=620, base_y=120, radius=30)  # right big

    draw_house(screen, x=90, y=240, w=220, h=160)

    draw_house(screen, x=430, y=260, w=150, h=130)

    trunk_center = pygame.Rect(310, 250, 30, 150)
    leaves_center = [
        (295, 250), (335, 250), (315, 220),
        (315, 280), (315, 305)
    ]
    draw_tree(screen, trunk_center, leaves_center, radius=40)

    trunk_right = pygame.Rect(615, 270, 25, 120)
    leaves_right = [
        (605, 260), (635, 260), (620, 235), (620, 285)
    ]
    draw_tree(screen, trunk_right, leaves_right, radius=32)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
