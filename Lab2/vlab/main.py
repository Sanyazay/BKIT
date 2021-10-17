from faker import Faker 
from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

a = Rectangle(7,7,"синего")
b = Circle(7,"зеленого")
g = Square(5,"dadaad")
d = Faker()
print(repr(a))
print(repr(b))
print(repr(g))
print(d.name())


