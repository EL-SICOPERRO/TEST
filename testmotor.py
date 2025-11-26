import RPi.GPIO as GPIO
import time

STEP_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)

DELAY = 0.0001   # 2ms high, 2ms low = 250Hz = 250 steps/sec

print("Medium speed...")

try:
    while True:
        GPIO.output(STEP_PIN, 1)
        time.sleep(DELAY)
        GPIO.output(STEP_PIN, 0)
        time.sleep(DELAY)

except KeyboardInterrupt:
    GPIO.cleanup()
