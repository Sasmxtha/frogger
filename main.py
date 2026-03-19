import pygame
import sys
import random
from settings import *
from sprites import Frog, Car, Log
from ui import draw_text, draw_menu, draw_game_over

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Frogger - Raspberry Pi 5 Edition")
    clock = pygame.time.Clock()

    game_state = "menu"  # menu, playing, game_over
    difficulty = "easy"
    score = 0
    level = 1
    lives = 3

    frog = None
    cars = pygame.sprite.Group()
    logs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    def start_game(diff):
        nonlocal frog, score, level, lives, game_state
        score = 0
        level = 1
        lives = 3
        game_state = "playing"
        cars.empty()
        logs.empty()
        all_sprites.empty()
        frog = Frog()
        all_sprites.add(frog)
        spawn_obstacles(diff, level)

    def spawn_obstacles(diff, lvl):
        cars.empty()
        logs.empty()
        speed_mult = DIFFICULTY_SETTINGS[diff]["speed_mult"] + (lvl - 1) * 0.3

        # Spawn cars on road lanes
        for lane_y in CAR_LANES:
            num_cars = random.randint(2, 4)
            for i in range(num_cars):
                direction = 1 if random.random() > 0.5 else -1
                speed = random.uniform(2.5, 5.0) * speed_mult * direction
                x = random.randint(0, SCREEN_WIDTH)
                car = Car(x, lane_y, speed)
                cars.add(car)
                all_sprites.add(car)

        # Spawn logs on river lanes
        for lane_y in LOG_LANES:
            num_logs = random.randint(2, 4)
            for i in range(num_logs):
                speed = random.uniform(1.5, 3.5) * speed_mult
                x = random.randint(0, SCREEN_WIDTH)
                log = Log(x, lane_y, speed)
                logs.add(log)
                all_sprites.add(log)

    running = True
    while running:
        dt = clock.tick(FPS)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game_state == "menu":
                    if event.key == pygame.K_1:
                        difficulty = "easy"
                        start_game(difficulty)
                    elif event.key == pygame.K_2:
                        difficulty = "moderate"
                        start_game(difficulty)
                    elif event.key == pygame.K_3:
                        difficulty = "hard"
                        start_game(difficulty)
                    elif event.key == pygame.K_q:
                        running = False

                elif game_state == "playing":
                    if event.key == pygame.K_UP:
                        frog.move(0, -GRID_SIZE)
                    elif event.key == pygame.K_DOWN:
                        frog.move(0, GRID_SIZE)
                    elif event.key == pygame.K_LEFT:
                        frog.move(-GRID_SIZE, 0)
                    elif event.key == pygame.K_RIGHT:
                        frog.move(GRID_SIZE, 0)

                elif game_state == "game_over":
                    if event.key == pygame.K_r:
                        game_state = "menu"
                    elif event.key == pygame.K_q:
                        running = False

        if game_state == "playing":
            cars.update()
            logs.update()

            # Check if frog is on a log in the river
            frog_in_river = RIVER_TOP <= frog.rect.centery <= RIVER_BOTTOM
            on_log = False
            if frog_in_river:
                for log in logs:
                    if frog.rect.colliderect(log.rect):
                        frog.rect.x += int(log.speed)
                        on_log = True
                        break
                if not on_log:
                    lives -= 1
                    frog.reset_position()
                    if lives <= 0:
                        game_state = "game_over"

            # Check car collision
            if pygame.sprite.spritecollide(frog, cars, False):
                lives -= 1
                frog.reset_position()
                if lives <= 0:
                    game_state = "game_over"

            # Check if frog went out of bounds
            if frog.rect.left < 0 or frog.rect.right > SCREEN_WIDTH:
                lives -= 1
                frog.reset_position()
                if lives <= 0:
                    game_state = "game_over"

            # Check level completion (frog reaches top)
            if frog.rect.top <= SAFE_ZONE_TOP:
                score += 100 * level
                level += 1
                frog.reset_position()
                spawn_obstacles(difficulty, level)

            # Increment score for upward movement
            score += 1 if frog.rect.centery < SCREEN_HEIGHT // 2 else 0

        # Draw
        screen.fill(BLACK)

        if game_state == "menu":
            draw_menu(screen)
        elif game_state == "playing":
            draw_background(screen)
            all_sprites.draw(screen)
            draw_text(screen, f"Score: {score}", 20, 20, WHITE, 28)
            draw_text(screen, f"Level: {level}", SCREEN_WIDTH - 120, 20, WHITE, 28)
            draw_text(screen, f"Lives: {'❤ ' * lives}", SCREEN_WIDTH // 2 - 60, 20, RED, 24)
        elif game_state == "game_over":
            draw_game_over(screen, score)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def draw_background(screen):
    # Sky / safe zone top
    screen.fill(GRASS_GREEN, (0, 0, SCREEN_WIDTH, SAFE_ZONE_TOP + GRID_SIZE))

    # River
    pygame.draw.rect(screen, RIVER_BLUE, (0, RIVER_TOP, SCREEN_WIDTH, RIVER_HEIGHT))

    # Safe zone middle
    screen.fill(GRASS_GREEN, (0, SAFE_ZONE_MID, SCREEN_WIDTH, GRID_SIZE))

    # Road
    pygame.draw.rect(screen, ROAD_GRAY, (0, ROAD_TOP, SCREEN_WIDTH, ROAD_HEIGHT))

    # Road dashes
    for x in range(0, SCREEN_WIDTH, 80):
        for lane_y in CAR_LANES[1:]:
            pygame.draw.rect(screen, WHITE, (x, lane_y + GRID_SIZE // 2 - 4, 40, 8))

    # Safe zone bottom
    screen.fill(GRASS_GREEN, (0, ROAD_BOTTOM, SCREEN_WIDTH, SCREEN_HEIGHT - ROAD_BOTTOM))


if __name__ == "__main__":
    main()
