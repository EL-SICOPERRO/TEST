import RPi.GPIO as GPIO
import time

STEP_PIN = 18  # BCM, physical pin 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)

print("Sending STEP pulses on GPIO18... Ctrl+C to stop")

try:
    while True:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.05)   # 20 steps per second
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopped and cleaned up")
