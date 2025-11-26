import RPi.GPIO as GPIO
import time

# --- PIN DEFINITIONS (BCM numbering) ---
STEP_PIN = 18   # physical pin 12
DIR_PIN  = 4    # physical pin 7
ENA_PIN  = 22   # physical pin 15

# --- CONFIG ---
DELAY = 0.002   # 2ms = 500 steps/sec (good safe speed)

# --- SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENA_PIN, GPIO.OUT)

# Enable driver
GPIO.output(ENA_PIN, GPIO.HIGH)   # ENA HIGH = enabled

# Set direction
GPIO.output(DIR_PIN, GPIO.LOW)    # LOW = CW, HIGH = CCW

print("Stepper running... Press Ctrl+C to stop.")

try:
    while True:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("\nStopping motor...")

finally:
    GPIO.output(ENA_PIN, GPIO.LOW)  # Disable driver
    GPIO.cleanup()
    print("GPIO cleaned. Done.")
