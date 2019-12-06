import matplotlib.pyplot as plt
import numpy as np
from Points import Points

class Plotter(object):

    def interactive(self, interactive: bool):
        if interactive:
            plt.ion()
        else:
            plt.ioff()

    def draw_points(self, points: Points):
        plt.plot(points.x, points.y, color=points.color, marker='.')
    
    def show(self):
        plt.show()
    
    def draw(self):
        plt.draw()

if __name__ == "__main__":
    plotter = Plotter()
    plotter.interactive(True)
    plt.show()
    
    points = Points()
    pointlist = [[1,1], [2,2], [3,3]]
    for point in pointlist:
        points.addpoint(point[0], point[1])
    points.setcolor("red")

    plotter.draw_points(points)

    print("after-show")


    