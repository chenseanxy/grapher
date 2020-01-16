from typing import List

class Points(object):

    def __init__(self):
        self.x = []
        self.y = []
        self.color = (0, 0, 0)

    def addpoint(self, x_pos: float, y_pos: float):
        self.x.append(x_pos)
        self.y.append(y_pos)
    
    def setcolor(self, color):
        if type(color) == str:
            builtin_colors = ('RED', 'YELLOW', 'GREEN', 'BLUE', 'BLACK')
            
            color = color.upper()
            if color in builtin_colors:
                if color == "BLACK":
                    self.color = (0, 0, 0)
                else:
                    # For R, G, B, Y: directly supported by matplotlib
                    self.color = color[0].lower()
        
        elif type(color) == tuple:
            # Convert (255, 255, 255) to (1, 1, 1)
            self.color = (color[0]/255.0, color[1]/255.0, color[2]/255.0)
        
        else:
            raise TypeError("Invalid type for color: should be str or tuple")

