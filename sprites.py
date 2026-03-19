import pygame
import math
from settings import *


def draw_frog_surface(size):
    """Draw a cute frog sprite programmatically."""
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx, cy = size // 2, size // 2
    r = size // 2 - 4

    # Body
    pygame.draw.ellipse(surf, (60, 180, 60), (cx - r + 4, cy - r + 8, r * 2 - 8, r * 2 - 8))

    # Head
    pygame.draw.circle(surf, (70, 200, 70), (cx, cy - 4), r - 6)

    # Eyes (white + pupil)
    eye_r = r // 4
    for ex in [cx - r // 3, cx + r // 3]:
        pygame.draw.circle(surf, WHITE, (ex, cy - r // 2), eye_r)
        pygame.draw.circle(surf, BLACK, (ex + 1, cy - r // 2), eye_r // 2)

    # Mouth
    pygame.draw.arc(surf, (30, 100, 30), (cx - 8, cy, 16, 8), math.pi, 0, 2)

    # Legs
    leg_color = (50, 160, 50)
    # Back legs
    pygame.draw.line(surf, leg_color, (cx - r + 6, cy + r - 10), (cx - r - 4, cy + r + 6), 4)
    pygame.draw.line(surf, leg_color, (cx + r - 6, cy + r - 10), (cx + r + 4, cy + r + 6), 4)

    return surf


def draw_car_surface(w, h, color):
    """Draw a top-down car sprite."""
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    # Body
    pygame.draw.rect(surf, color, (4, 8, w - 8, h - 16), border_radius=8)
    # Windshield
    pygame.draw.rect(surf, (180, 220, 255, 200), (8, 12, w - 16, 12), border_radius=4)
    # Rear window
    pygame.draw.rect(surf, (180, 220, 255, 160), (8, h - 22, w - 16, 10), border_radius=4)
    # Wheels
    wheel_color = (30, 30, 30)
    for wx, wy in [(2, 10), (w - 10, 10), (2, h - 22), (w - 10, h - 22)]:
        pygame.draw.rect(surf, wheel_color, (wx, wy, 8, 12), border_radius=3)
    # Headlights
    pygame.draw.circle(surf, (255, 255, 180), (10, 10), 4)
    pygame.draw.circle(surf, (255, 255, 180), (w - 10, 10), 4)
    return surf


def draw_log_surface(w, h):
    """Draw a wooden log sprite."""
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    # Main log body
    pygame.draw.rect(surf, BROWN, (0, 4, w, h - 8), border_radius=6)
    # Bark lines
    bark = (101, 60, 20)
    for lx in range(20, w - 10, 25):
        pygame.draw.line(surf, bark, (lx, 6), (lx + 4, h - 6), 2)
    # End circles
    pygame.draw.ellipse(surf, DARK_BROWN, (w - 20, 2, 20, h - 4))
    pygame.draw.ellipse(surf, (160, 100, 50), (w - 18, 4, 16, h - 8))
    # Ring
    pygame.draw.ellipse(surf, DARK_BROWN, (w - 16, 8, 12, h - 16), 2)
    return surf


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = draw_frog_surface(GRID_SIZE - 8)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.centerx = FROG_START_X + GRID_SIZE // 2
        self.rect.centery = FROG_START_Y + GRID_SIZE // 2

    def move(self, dx, dy):
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy
        # Clamp horizontally
        new_x = max(0, min(SCREEN_WIDTH - self.rect.width, new_x))
        # Clamp vertically
        new_y = max(0, min(SCREEN_HEIGHT - self.rect.height, new_y))
        self.rect.x = new_x
        self.rect.y = new_y


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.speed = speed
        w, h = GRID_SIZE + 20, GRID_SIZE - 16
        self.image = draw_car_surface(w, h, YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y

    def update(self):
        self.rect.x += int(self.speed)
        # Wrap around
        if self.speed > 0 and self.rect.left > SCREEN_WIDTH + 20:
            self.rect.right = -20
        elif self.speed < 0 and self.rect.right < -20:
            self.rect.left = SCREEN_WIDTH + 20


class Log(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.speed = speed
        w = random.randint(GRID_SIZE + 40, GRID_SIZE + 100)
        h = GRID_SIZE - 12
        self.image = draw_log_surface(w, h)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y

    def update(self):
        self.rect.x += int(self.speed)
        if self.speed > 0 and self.rect.left > SCREEN_WIDTH + 20:
            self.rect.right = -20
        elif self.speed < 0 and self.rect.right < -20:
            self.rect.left = SCREEN_WIDTH + 20


import random
