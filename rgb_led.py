
class led:
    state = False
    colour = [0,0,0]
    brightness = 0 
    id = None

    def __init__(self, state=False, colour=[0,0,0], brightness=0, id=None):
        self.state = state
        self.colour = colour
        self.brightness = brightness
        self.id = id
        

    def __str__(self):
        print "ID:"+self.id+", State:"+self.state+", Colour:"+self.colour+", Brightness:"+self.brightness

    def updateColour(self, r, g, b):
        self.colour = [r,g,b]