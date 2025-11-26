import RPi.GPIO as GPIO
import time

# --- BCM pins ---
STEP_PIN = 18    # physical pin 12
DIR_PIN  = 4     # physical pin 7
ENA_PIN  = 22    # physical pin 15

DELAY = 0.001    # adjust for speed (smaller = faster)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_PIN,  GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENA_PIN,  GPIO.OUT, initial=GPIO.HIGH)   # HIGH = enabled

# Set direction (LOW = CW, HIGH = CCW)
GPIO.output(DIR_PIN, GPIO.LOW)

print("Motor spinning... Press Ctrl+C to stop")

try:
    while True:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("\nStopping motor...")

finally:
    GPIO.output(ENA_PIN, GPIO.LOW)   # disable driver (motor freewheels)
    GPIO.cleanup()
    print("Done.")
