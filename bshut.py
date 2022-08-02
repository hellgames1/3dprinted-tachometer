import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BCM)
buttonpin=26
GPIO.setup(buttonpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
	buttonstate=GPIO.input(buttonpin)
	if buttonstate == False:
		os.system("shutdown now -h")
		break
	time.sleep(0.2)
