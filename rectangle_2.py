from rectangle import Rectangle, Square, Circle
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square(),
      square_2.get_area_square())

s_1 = Circle(8)
s_2 = Circle(10)
print(s_1.get_area_circl())
print(s_2.get_area_circl())


figures = [rect_1, rect_2, square_1, square_2, s_1, s_2]

for figure in figures:
    if isinstance(figure, Square):
        print("Площадь квадрата:", figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print("Площадь прямоугольника:", figure.get_area())
    else:
        print("Площадь круга:", figure.get_area_circl())


