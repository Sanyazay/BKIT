from math import pi
from lab_python_oop.figure_color import FigColor
from lab_python_oop.geometric_figure import GeoFigure

class Circle(GeoFigure):
    figure_type = "Круг"
    def __init__(self,r,color):
        self.r=r
        self.color = FigColor(color)
    
    def find_area(self):
        return pi*self.r*self.r

    def __repr__(self):
        return"{} {} цвета радиуса {} площадью {}.".format(
            self.get_figure_type(),
            self.color.getColor,
            self.r,
            self.find_area()
        )
