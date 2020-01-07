import matplotlib.pyplot as plt
import numpy as np
from Points import Points

class Plotter(object):

    @staticmethod
    def interactive(interactive: bool):
        if interactive:
            plt.ion()
        else:
            plt.ioff()

    @staticmethod
    def draw_points(points: Points):
        plt.plot(points.x, points.y, color=points.color, marker='.', lw=0)
        plt.axis('scaled')

    @staticmethod
    def show():
        plt.show()
    
    @staticmethod
    def draw():
        plt.draw()

if __name__ == "__main__":
    Plotter.interactive(True)
    Plotter.show()
    
    points = Points()
    pointlist = [[1,1], [2,2], [3,3]]
    for point in pointlist:
        points.addpoint(point[0], point[1])
    points.setcolor("red")

    Plotter.draw_points(points)

    input("after-show: enter to continue")
    
    