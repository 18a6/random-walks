class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(object.x + deltaX,
                        object.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y