#pir
import RPi.GPIO as GPIO
import time

pirPin = 24

GPIO.setmode(BCM)
GPIO.setup(pirPin, GPIO.IN)

try:
  while True:
    if GPIO.input(pirPin) == False:
      print("Detected")
      time.sleep(0.5)
except KeyboardInterrupt:
  GPIO.cleanup()
