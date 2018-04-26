from PIL import Image, ImageDraw
import random

class Shape:
    colors = ["white", "red", "yellow", "blue", "green", "orange", "purple"]

    def __init__(self, color):
        self.color = color

    # @classmethod 
    # def random_init(cls, image_dimentions, object_size):
    #     None

    @classmethod
    def random(cls, image_dimentions, object_size):
        return random.choice([Circle, Rectangle]).random_init(image_dimentions, object_size)


class Circle(Shape):
    def __init__(self, center_x, center_y, radius, color):
        super(Circle, self).__init__(color)

        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def draw(self, draw):
        x1 = self.center_x - self.radius
        x2 = self.center_x + self.radius
        y1 = self.center_y - self.radius
        y2 = self.center_y + self.radius
        draw.ellipse((x1, y1, x2, y2), fill=self.color, outline="black")

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
        super(Rectangle, self).__init__(color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, draw):
        draw.rectangle([self.x1, self.y1, self.x2, self.y2], fill=self.color, outline="black")

    @classmethod 
    def random_init(cls, image_dimentions, object_size):
        width = random.randint(object_size["min"]*image_dimentions["x"], object_size["max"]*image_dimentions["x"])
        height = random.randint(object_size["min"]*image_dimentions["y"], object_size["max"]*image_dimentions["y"])
        x1 = random.randint(0, image_dimentions["x"]-width)
        y1 = random.randint(0, image_dimentions["y"]-height)
        return Rectangle(x1, y1, x1 + width, y1 + height, random.choice(cls.colors))

#class Triangle(Shape):