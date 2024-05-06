import RPi.GPIO as GPIO
import time

blink_led = 5
GPIO.setmode(GPIO.BOARD) # Note This is specifying the physical pins on the Raspberry Pi Header 
GPIO.setwarnings(False)
GPIO.setup(blink_led,GPIO.OUT)

while(True):
  print("LED on")
  GPIO.output(blink_led,GPIO.HIGH)
  time.sleep(1)
  print("LED off")
  GPIO.output(blink_led,GPIO.LOW)
  time.sleep(1)
print('Done')
