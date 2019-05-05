import RPi.GPIO as GPIO
import time

from character.Mood import Mood
from observer.Observer import Observer
from observer.Event import Event

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO22

mood = Mood()
mood.observe('wall_hit',  mood.wall_hit)


try:
    while True:
         button_state = GPIO.input(22)
         if button_state == False:
             print('Button Pressed...')
             Event('wall_hit', 'Lenard')
         else:
             print('Button Not Pressed...')
         time.sleep(0.5)
             
except:
    GPIO.cleanup()
