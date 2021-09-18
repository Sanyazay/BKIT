

from lab_python_oop.rectangle import Rectangle



class Square(Rectangle):
    figure_type = "Квадрат"
    def __init__(self, side, color):
        super().__init__(side, side, color)

    
    def __repr__(self):
        return"{} {} цвета длиной стороны {} и площадью {}.".format(
            self.get_figure_type(),
            self.color.getColor,
            self.width,
            self.find_area()
        )

