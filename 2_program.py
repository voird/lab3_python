class Shape:
    def __init__(self, identifier):
        self.identifier = identifier
        self.vertices = []

    def add_vertex(self, coordinates):
        self.vertices.append(coordinates)

class Rectangle(Shape):
    def __init__(self, identifier, x, y, width):
        super().__init__(identifier)
        
        self.add_vertex((x, y))
        self.add_vertex((x + width, y))
        self.add_vertex((x + width, y + width))
        self.add_vertex((x, y + width))

        if width < 0:
            print("Значение ширины должно быть положительным")

        self.width = width

    def area(self):
        return self.width * self.width
    
class Pentagon(Shape):
    def __init__(self, identifier, x, y, side_length):
        import math
        super().__init__(identifier)
        
        self.add_vertex((x, y))
        for i in range(1, 6):
            angle = i * 2 * math.pi / 5
            self.add_vertex((x + side_length * math.cos(angle + math.pi/2), y + side_length * math.sin(angle + math.pi/2)))

        if side_length < 0:
            print("Значения длины должны быть положительными")

        self.side_length = side_length

    def area(self):
        import math
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side_length**2

def compare(shape1, shape2):
    return shape1.area() - shape2.area()

def is_include(shape1, shape2):
    if not isinstance(shape1, Rectangle) or not isinstance(shape2, Pentagon):
        print("Оба объекта должны быть экземплярами соответствующих классов")

    for vertex in shape1.vertices:
        if not is_point_inside_polygon(vertex, shape2.vertices):
            return False

    return True

def is_point_inside_polygon(point, polygon_vertices):
    x, y = point
    n = len(polygon_vertices)
    inside = False

    p1x, p1y = polygon_vertices[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon_vertices[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y

    return inside

print("Введите значения x, y, w для прямоугольника: ")
x = int(input("x: "))
y = int(input("y: "))
w = int(input("w: "))
rectangle1 = Rectangle("R1", x, y, w)

print("Введите значения x, y, l для пятиугольника: ")
x = int(input("x: "))
y = int(input("y: "))
l = int(input("l: "))
pentagon1 = Pentagon("P1", x, y, l)

print("Прямоугольник :", rectangle1.area())
print("Пятиугольник:", pentagon1.area())

if is_include(rectangle1, pentagon1):
    print("Прямоугольник включен в пятиугольник")
else:
    print("Прямоугольник не включен в пятиугольник")

area_comparison = compare(rectangle1, pentagon1)
if area_comparison > 0:
    print("Прямоугольник больше пятиугольника")
elif area_comparison < 0:
    print("Прямоугольник меньше пятиугольника")
else:
    print("Прямоугольник равен пятиугольнику")
