from PIL import Image, ImageDraw

class Shape:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.x1 = center_x - radius
        self.x2 = center_x + radius
        self.y1 = center_y - radius
        self.y2 = center_y + radius

    def draw(self, draw)
        draw.ellipse((self.x1, self.y1, self.x2, self.y2))

#class Rectangle(Shape):

#class Triangle(Shape):