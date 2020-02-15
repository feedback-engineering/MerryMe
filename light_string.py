from rgb_led import led
import neopixel, machine
class lightString:
    lights = []
    

    def addLight(self, newLight):
        self.lights.append(newLight)
    
    def updateLights(self, newColours):
        #newColours is a list of 2-tuples, the first element of which is a 3-tuple of RGB values (in format R, G, B), and the second value is the brightness scaling factor
        if len(newColours) == len(self.lights):
        
            for i in range(0, len(newColours),1):
                self.lights[i].updateColour(newColours[i][0], newColours[i][1])

        else:
            raise Exception("Number of lights to update does not match number of lights within string.")

    def sendString(self):
        np = neopixel.NeoPixel(machine.Pin(5), len(self.lights))
        for i in range(0, len(self.lights),1):
            np[i] = self.lights[i].getColour()