# gpio_extension.py
# Optional GPIO integration for Raspberry Pi 5
# Connect a physical button to GPIO pin 17 and LED to GPIO pin 18

import pygame
import sys

try:
    import RPi.GPIO as GPIO
    GPIO_AVAILABLE = True
except ImportError:
    GPIO_AVAILABLE = False
    print("[INFO] RPi.GPIO not found. GPIO features disabled.")


BUTTON_PIN = 17   # Physical button → frog jump
LED_PIN    = 18   # LED blinks on level completion


def setup_gpio():
    """Initialize GPIO pins."""
    if not GPIO_AVAILABLE:
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)
    print("[GPIO] Pins initialized. Button: GPIO17, LED: GPIO18")


def read_button():
    """Return True if the physical button is pressed."""
    if not GPIO_AVAILABLE:
        return False
    return not GPIO.input(BUTTON_PIN)  # Active LOW (pull-up)


def blink_led(times=3, delay_ms=200):
    """Blink the LED a given number of times."""
    if not GPIO_AVAILABLE:
        return
    for _ in range(times):
        GPIO.output(LED_PIN, GPIO.HIGH)
        pygame.time.delay(delay_ms)
        GPIO.output(LED_PIN, GPIO.LOW)
        pygame.time.delay(delay_ms)


def cleanup_gpio():
    """Release GPIO resources."""
    if not GPIO_AVAILABLE:
        return
    GPIO.cleanup()
    print("[GPIO] Cleanup done.")


# ── Usage example ────────────────────────────────────────────────────────────
# In your main game loop, after setup_gpio():
#
#   if read_button():
#       frog.move(0, -GRID_SIZE)   # jump up
#
#   # When level is completed:
#   blink_led(times=3)
#
#   # On exit:
#   cleanup_gpio()
# ─────────────────────────────────────────────────────────────────────────────
