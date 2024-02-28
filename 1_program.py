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
