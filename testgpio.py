import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(18,1); time.sleep(0.1)
    GPIO.output(18,0); time.sleep(0.1)
