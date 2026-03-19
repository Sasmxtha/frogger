# settings.py - Game Configuration Constants

# Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
GRID_SIZE = 60

# Colors
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
RED        = (220, 50, 50)
GREEN      = (34, 139, 34)
GRASS_GREEN = (72, 160, 72)
RIVER_BLUE = (100, 180, 230)
ROAD_GRAY  = (80, 80, 80)
YELLOW     = (255, 220, 0)
BROWN      = (139, 90, 43)
DARK_BROWN = (101, 60, 20)

# Layout (based on 800px tall screen, 60px grid)
SAFE_ZONE_TOP  = 0        # Top grass strip
RIVER_TOP      = GRID_SIZE
RIVER_HEIGHT   = GRID_SIZE * 7  # 7 rows of river
RIVER_BOTTOM   = RIVER_TOP + RIVER_HEIGHT
SAFE_ZONE_MID  = RIVER_BOTTOM
ROAD_TOP       = SAFE_ZONE_MID + GRID_SIZE
ROAD_HEIGHT    = GRID_SIZE * 5  # 5 rows of road
ROAD_BOTTOM    = ROAD_TOP + ROAD_HEIGHT
# Bottom grass = ROAD_BOTTOM to SCREEN_HEIGHT

# Lane Y positions (center of lane)
LOG_LANES = [
    RIVER_TOP + GRID_SIZE * 1 - GRID_SIZE // 2,
    RIVER_TOP + GRID_SIZE * 2 - GRID_SIZE // 2,
    RIVER_TOP + GRID_SIZE * 3 - GRID_SIZE // 2,
    RIVER_TOP + GRID_SIZE * 4 - GRID_SIZE // 2,
    RIVER_TOP + GRID_SIZE * 5 - GRID_SIZE // 2,
    RIVER_TOP + GRID_SIZE * 6 - GRID_SIZE // 2,
    RIVER_TOP + GRID_SIZE * 7 - GRID_SIZE // 2,
]

CAR_LANES = [
    ROAD_TOP + GRID_SIZE * 1 - GRID_SIZE // 2,
    ROAD_TOP + GRID_SIZE * 2 - GRID_SIZE // 2,
    ROAD_TOP + GRID_SIZE * 3 - GRID_SIZE // 2,
    ROAD_TOP + GRID_SIZE * 4 - GRID_SIZE // 2,
    ROAD_TOP + GRID_SIZE * 5 - GRID_SIZE // 2,
]

# Frog start position
FROG_START_X = SCREEN_WIDTH // 2 - GRID_SIZE // 2
FROG_START_Y = ROAD_BOTTOM + GRID_SIZE // 4

# Difficulty
DIFFICULTY_SETTINGS = {
    "easy":     {"speed_mult": 0.7},
    "moderate": {"speed_mult": 1.0},
    "hard":     {"speed_mult": 1.6},
}
