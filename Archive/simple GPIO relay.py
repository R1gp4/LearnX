import RPi.GPIO as GPIO  
import time  

GPIO.setmode(GPIO.BOARD)  
number = 37  
GPIO.setup(number,GPIO.OUT)  
GPIO.output(number,True) 

GPIO.setup(GPIO.BCM)  
number = 37  
GPIO.setup(number, GPIO.IN)  
GPIO.input(number, True)  