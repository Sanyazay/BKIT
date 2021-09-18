from abc import ABC,abstractmethod

class GeoFigure(ABC):
    figure_type = None
    @classmethod
    def get_figure_type(cls):
        return cls.figure_type
    @abstractmethod
    def find_area():
        pass
    