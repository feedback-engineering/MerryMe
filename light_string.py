from rgb_led import led

class lightString:
    currentLights = []
    

    def addLight(self, newLight):
        currentLights.append(newLight)
    
    def updateLights(self, newColours):
        #newColours is a list of 2-tuples, the first element of which is a list of RGB values, and the second value is the brightness scaling factor
        if len(newColours) == len(currentLights):
        
            for e in newColours:
        else:
            raise Exception("Number of lights to update does not match number of lights within string.")