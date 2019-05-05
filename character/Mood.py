from observer.Observer import Observer
from observer.Event import Event

class Mood(Observer):

    def __init__(self):
        print("Mood inizialized.")
        Observer.__init__(self) # Observer's init needs to be called
    def wall_hit(self, who):
        print("I hit a wall")
    