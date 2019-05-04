import RPi.GPIO as GPIO
import time
import vlc
p = vlc.MediaPlayer("/home/pi/Programming/ScreamingRobot/soundProfiles/angryRobot/hitWallEvent/hit.mp3")



GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

try:
    while True:
         button_state = GPIO.input(22)
         if button_state == False:
             GPIO.output(24, True)
             print('Button Pressed...')
             p.play()
         else:
             GPIO.output(24, False)
             print('Button Not Pressed...')
             p.stop()
         time.sleep(0.5)
             
except:
    GPIO.cleanup()
