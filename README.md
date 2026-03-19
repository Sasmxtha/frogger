# 🐸 Frogger Game — Raspberry Pi 5 Edition

A Python + Pygame implementation of the classic Frogger arcade game, developed as an educational tool for teaching school students **Python programming** and **embedded systems** concepts on the **Raspberry Pi 5**.

> 📄 This project is described in the paper:  
> *"Teaching School Students Python Programming and Embedded Systems using Frogger Game on Raspberry Pi 5"*  
> Department of AI & Data Science, Amrita Vishwa Vidyapeetham, Coimbatore

---

## 🎮 Gameplay

Navigate the **frog** from the bottom of the screen to the top by:
- **Crossing the road** — dodge moving yellow cars
- **Crossing the river** — hop on floating logs to avoid drowning
- Reach the **safe zone at the top** to score points and advance levels!

---

## 📸 Screenshots

| Menu | Gameplay |
|------|----------|
| *(Run the game to see the menu)* | ![Gameplay](screenshots/gameplay.png) |

---

## 🗂️ Project Structure

```
frogger_game/
├── main.py        # Game loop, collision logic, rendering
├── settings.py    # Constants: screen size, colors, lane positions
├── sprites.py     # Frog, Car, Log sprite classes (drawn programmatically)
├── ui.py          # Menu, HUD, Game Over screen
└── README.md
```

---

## 🧰 Requirements

| Hardware | Software |
|----------|----------|
| Raspberry Pi 5 (or any PC) | Python 3.11+ |
| HDMI Display | Pygame library |
| Keyboard | Raspbian OS (Bookworm) or any OS |
| GPIO components (optional) | RPi.GPIO (for GPIO features) |

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/sasmxtha/frogger.git
cd frogger-rpi5

# 2. Install Pygame
pip install pygame

# 3. Run the game
python main.py
```

On Raspberry Pi, you can also open `main.py` in **Thonny IDE** and press Run.

---

## 🎯 Controls

| Key | Action |
|-----|--------|
| ↑ Arrow | Move Up |
| ↓ Arrow | Move Down |
| ← Arrow | Move Left |
| → Arrow | Move Right |
| `1` | Select Easy difficulty |
| `2` | Select Moderate difficulty |
| `3` | Select Hard difficulty |
| `R` | Restart (from Game Over) |
| `Q` | Quit |

---

## 🌟 Features

- **3 Difficulty Levels** — Easy, Moderate, Hard (obstacle speed scales up)
- **River Crossing Logic** — frog rides on moving logs; falls if no log underneath
- **Dynamic Obstacles** — cars and logs with randomized speeds and directions
- **Level Progression** — obstacles get faster each level
- **Score System** — earn points for advancing and completing levels
- **Lives System** — 3 lives before game over
- **Programmatic Sprites** — all graphics drawn with Pygame (no external image files needed)

---

## 🔌 GPIO Extension (Raspberry Pi)

To add hardware interaction (as described in the paper):

```python
import RPi.GPIO as GPIO

BUTTON_PIN = 17
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

# In game loop:
if not GPIO.input(BUTTON_PIN):   # Button pressed
    frog.move(0, -GRID_SIZE)     # Jump up

# On level complete:
GPIO.output(LED_PIN, GPIO.HIGH)
pygame.time.delay(300)
GPIO.output(LED_PIN, GPIO.LOW)
```

---

## 📚 Educational Concepts Covered

- Python syntax, functions, and OOP (classes)
- Pygame game loop, event handling, sprite management
- Collision detection algorithms
- Hardware-software integration via GPIO
- Computational thinking and problem-solving

---

## 📖 References

- [Python Official Docs](https://www.python.org)
- [Pygame Library](https://www.pygame.org)
- [Raspberry Pi Documentation](https://www.raspberrypi.org)
- M. Prensky, "Digital Game-Based Learning," *Computers in Entertainment*, 2003.

---

*Amrita Vishwa Vidyapeetham, Coimbatore — Dept. of AI & Data Science*
