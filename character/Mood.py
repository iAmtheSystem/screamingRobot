from observer.Observer import Observer
from observer.Event import Event

import vlc

p = vlc.MediaPlayer("/home/pi/Programming/ScreamingRobot/soundProfiles/angryRobot/hitWallEvent/hit.mp3")

class Mood(Observer):
    def __init__(self):
        print("DEBUG: Mood inizialized.")    
        Observer.__init__(self) # Observer's init needs to be called
        
    def wall_hit(self, who):
        print("DEBUG I hit a wall")
        self.start_talking(p)

    def start_talking(self,soundfile):
        print("DEBUG: I talk now about ")
        soundfile.play()

    def stop_talking(self,soundfile):
        print("DEBUG: Stopping to talk")
        soundfile.stop()



