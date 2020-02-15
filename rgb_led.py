import math

class led:
    state = False
    colour = (0,0,0)
    brightness = 0 
    id = None

    def __init__(self, state=False, colour=(0,0,0), brightness=0, id=None):
        self.state = state
        self.colour = colour
        self.brightness = brightness
        self.id = id

        

    def __str__(self):
        print("ID:"+self.id+", State:"+self.state+", Colour:"+self.colour+", Brightness:"+self.brightness)

    def getColour(self):
        return self.colour

    def updateColour(self, rgb, brightness):
        self.colour = (math.floor(rgb[0]*(brightness/255)),math.floor(rgb[1]*(brightness/255)),math.floor(rgb[2]*(brightness/255)))