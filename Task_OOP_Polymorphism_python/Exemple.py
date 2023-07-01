from task1 import Rectangle, Square, Cirecl


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
# print(rect1.get_rect_area(),
#       rect2.get_rect_area())
#
#
squr1 = Square(5)
squr2 = Square(7)
# print(squr1.get_squr_area(),
#       squr2.get_squr_area())

circl1 = Cirecl(3)
circl2 = Cirecl(2)

# мы хотим, все наши обькты поместить в одну коллекцию.

collec_object = [rect1, rect2, squr1, squr2, circl1, circl2]
for obj in collec_object:
      # if isinstance(obj, Rectangle):
      #       print(f'Площадь {obj.__dict__} прямоугольника равна - {obj.get_rect_area()}')
      # elif isinstance(obj, Cirecl):
      #       print(f'Площадь {obj.__dict__} круга равна - {round(obj.get_circl_area(), 2)}')
      # else:
      #       print(f'Площадь {obj.__dict__} квадрата равна - {round(obj.get_squr_area(), 2)}')
# А можно сделать код менее громоздким и использовать полиморфизм - это обработка разных
# обьектов одним методом
      print(obj, obj.get_area())