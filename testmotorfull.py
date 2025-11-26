import RPi.GPIO as GPIO
import time

STEP_PIN = 18   # pin 12
DIR_PIN  = 4    # pin 7

DELAY = 0.001

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_PIN,  GPIO.OUT, initial=GPIO.LOW)

print("DIR LOW (CW)...")
GPIO.output(DIR_PIN, GPIO.LOW)

try:
    t_end = time.time() + 10
    while time.time() < t_end:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(DELAY)

    print("DIR HIGH (CCW)...")
    GPIO.output(DIR_PIN, GPIO.HIGH)

    t_end = time.time() + 10
    while time.time() < t_end:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("Interrupted.")

finally:
    GPIO.cleanup()
    print("Done.")
