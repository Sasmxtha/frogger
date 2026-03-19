import pygame
from settings import *


def draw_text(surface, text, x, y, color=WHITE, size=28, bold=False):
    """Render text at given position."""
    font = pygame.font.SysFont("freesansbold.ttf", size, bold=bold)
    label = font.render(text, True, color)
    surface.blit(label, (x, y))
    return label.get_rect(topleft=(x, y))


def draw_menu(screen):
    """Draw the main menu screen."""
    screen.fill((20, 40, 20))

    # Title background
    title_rect = pygame.Rect(50, 80, SCREEN_WIDTH - 100, 120)
    pygame.draw.rect(screen, (0, 100, 0), title_rect, border_radius=16)
    pygame.draw.rect(screen, (0, 200, 80), title_rect, 3, border_radius=16)

    # Title
    draw_text(screen, "FROGGER", SCREEN_WIDTH // 2 - 110, 100, (0, 255, 100), 64, bold=True)
    draw_text(screen, "Raspberry Pi 5 Edition", SCREEN_WIDTH // 2 - 155, 170, (180, 255, 180), 22)

    # Divider
    pygame.draw.line(screen, (0, 180, 80), (80, 230), (SCREEN_WIDTH - 80, 230), 2)

    # Instructions
    draw_text(screen, "Select Difficulty:", SCREEN_WIDTH // 2 - 110, 260, WHITE, 28, bold=True)

    options = [
        ("1", "EASY",     "Slow obstacles, relaxed gameplay",    (100, 220, 100)),
        ("2", "MODERATE", "Standard speed, balanced challenge",  (255, 220, 60)),
        ("3", "HARD",     "Fast obstacles, intense gameplay",     (255, 100, 80)),
    ]

    for i, (key, label, desc, color) in enumerate(options):
        y = 320 + i * 110
        box = pygame.Rect(80, y, SCREEN_WIDTH - 160, 90)
        pygame.draw.rect(screen, (30, 60, 30), box, border_radius=12)
        pygame.draw.rect(screen, color, box, 2, border_radius=12)

        draw_text(screen, f"[{key}]", 110, y + 20, color, 32, bold=True)
        draw_text(screen, label, 165, y + 20, color, 32, bold=True)
        draw_text(screen, desc, 110, y + 58, (180, 200, 180), 18)

    draw_text(screen, "Arrow Keys to Move   |   [Q] Quit", SCREEN_WIDTH // 2 - 175, 680, (120, 160, 120), 20)

    # Frog emoji-style hint
    draw_text(screen, "🐸 → Navigate to the top to score!", SCREEN_WIDTH // 2 - 175, 720, (100, 255, 140), 18)


def draw_game_over(screen, score):
    """Draw game over screen."""
    # Dim overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    box = pygame.Rect(80, 220, SCREEN_WIDTH - 160, 360)
    pygame.draw.rect(screen, (30, 10, 10), box, border_radius=20)
    pygame.draw.rect(screen, RED, box, 3, border_radius=20)

    draw_text(screen, "GAME OVER", SCREEN_WIDTH // 2 - 130, 250, RED, 52, bold=True)

    pygame.draw.line(screen, (150, 30, 30), (100, 330), (SCREEN_WIDTH - 100, 330), 2)

    draw_text(screen, f"Final Score: {score}", SCREEN_WIDTH // 2 - 110, 360, WHITE, 32, bold=True)

    draw_text(screen, "[R] Return to Menu", SCREEN_WIDTH // 2 - 120, 450, (200, 200, 200), 24)
    draw_text(screen, "[Q] Quit Game",      SCREEN_WIDTH // 2 - 90,  500, (180, 180, 180), 24)
