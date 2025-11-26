import RPi.GPIO as GPIO
import time

PIN = 18  # BCM numbering, physical pin 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)

print("Toggling GPIO18... Ctrl+C to stop")

try:
    while True:
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Stopped and cleaned up")
