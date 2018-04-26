from PIL import Image, ImageDraw
import random

class Shape:
    colors = ["red", "yellow", "blue", "green", "orange", "purple"]


    def __init__(self, x1, y1, x2, y2, color="black"):
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @classmethod
    def shape_classes(cls):
        return [Circle, Rectangle, Triangle]

    @classmethod
    def filterby_class(cls, shapes, shape_class):
        result = []
        for shape in shapes:
            if isinstance(shape, shape_class):
                result.append(shape)
        return result

    @classmethod
    def filterby_color(cls, shapes, color):
        result = []
        for shape in shapes:
            if shape.color == color:
                result.append(shape)
        return result

    @classmethod
    def random(cls, image_dimentions, object_size):
        return random.choice(cls.shape_classes()).random_init(image_dimentions, object_size)

    # area of intersection of bounding boxes
    def intersection_area(self, other):
        intersect_x = max(min(self.x2, other.x2) - max(self.x1, other.x1), 0)
        intersect_y = max(min(self.y2, other.y2) - max(self.y1, other.y1), 0) 
        return intersect_x * intersect_y

    def intersects_any(self, shapes):
        intersects = False
        for other in shapes:
            if self.intersection_area(other) > 0:
                intersects = True
        return intersects

class Circle(Shape):
    def __init__(self, center_x, center_y, radius, color):
        super(Circle, self).__init__(center_x - radius, center_y - radius, center_x + radius, center_y + radius, color)

    def draw(self, draw):
        draw.ellipse([self.x1, self.y1, self.x2, self.y2], fill=self.color, outline="black")

    @classmethod 
    def random_init(cls, image_dimentions, object_size):
        min_dim = min(image_dimentions["x"], image_dimentions["y"])        
        radius = random.randint(object_size["min"]*min_dim/2, object_size["max"]*min_dim/2)
        return Circle(random.randint(radius, image_dimentions["x"]-radius), 
                      random.randint(radius, image_dimentions["y"]-radius),
                      radius,
                      random.choice(cls.colors))

class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2, color):
        super(Rectangle, self).__init__(x1, y1, x2, y2, color)

    def draw(self, draw):
        draw.rectangle([self.x1, self.y1, self.x2, self.y2], fill=self.color, outline="black")

    @classmethod 
    def random_init(cls, image_dimentions, object_size):
        width = random.randint(object_size["min"]*image_dimentions["x"], object_size["max"]*image_dimentions["x"])
        height = random.randint(object_size["min"]*image_dimentions["y"], object_size["max"]*image_dimentions["y"])
        x1 = random.randint(0, image_dimentions["x"]-width)
        y1 = random.randint(0, image_dimentions["y"]-height)
        return Rectangle(x1, y1, x1 + width, y1 + height, random.choice(cls.colors))

class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        super(Triangle, self).__init__(min([x1, x2, x3]), min([y1, y2, y3]), max([x1, x2, x3]), max([y1, y2, y3]), color)
        self.vx1 = x1
        self.vy1 = y1
        self.vx2 = x2
        self.vy2 = y2
        self.vx3 = x3
        self.vy3 = y3

    def draw(self, draw):
        draw.polygon([self.vx1, self.vy1, self.vx2, self.vy2, self.vx3, self.vy3], fill=self.color, outline="black")

    @classmethod 
    def random_init(cls, image_dimentions, object_size):
        width = random.randint(object_size["min"]*image_dimentions["x"], object_size["max"]*image_dimentions["x"])
        height = random.randint(object_size["min"]*image_dimentions["y"], object_size["max"]*image_dimentions["y"])
        x1 = random.randint(0, image_dimentions["x"]-width)
        y1 = random.randint(0, image_dimentions["y"]-height)
        return Triangle(x1, y1 + height, x1 + (width/2), y1, x1 + width, y1 + height, random.choice(cls.colors)) 

