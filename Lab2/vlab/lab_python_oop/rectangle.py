



from lab_python_oop.figure_color import FigColor
from lab_python_oop.geometric_figure import GeoFigure


class Rectangle(GeoFigure):

    figure_type = "Прямоугольник"
    
    def __init__(self,length,width,color):
        self.color=FigColor(color)
        self.length = length
        self.width = width

    #@property

    def find_area(self):
        return self.length*self.width


    def __repr__(self):
        return"{} {} цвета шириной {} и высотой {} площадью {}.".format(
            self.get_figure_type(),
            self.color.getColor,
            self.width,
            self.length,
            self.find_area()
        )
        '''
a = Rectangle(1,2,"dada")
print(repr(a))
'''