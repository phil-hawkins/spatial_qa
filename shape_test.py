import unittest
import json
from shape import Circle, Rectangle, Shape

class Test_Shapes(unittest.TestCase):
    config = None #= json.load(open('config.json')) 

    @classmethod
    def setUpClass(cls):
        cls.config = json.load(open('config.json'))

    def test_circle_rand_init(self):
        config = self.__class__.config
        circle = Circle.random_init(config["image_dimentions"], config["object_size"])
        self.assertGreaterEqual(circle.center_x, circle.radius)
        self.assertGreaterEqual(circle.center_y, circle.radius)
        self.assertLessEqual(circle.center_x, config["image_dimentions"]["x"] - circle.radius)
        self.assertLessEqual(circle.center_y, config["image_dimentions"]["y"] - circle.radius)
        self.assertIn(circle.color, Shape.colors)

    def test_rectangle_rand_init(self):
        config = self.__class__.config
        rectangle = Rectangle.random_init(config["image_dimentions"], config["object_size"])
        self.assertGreaterEqual(rectangle.x1, 0)
        self.assertGreaterEqual(rectangle.y1, 0)
        self.assertGreaterEqual(rectangle.x2, rectangle.x1)
        self.assertGreaterEqual(rectangle.y2, rectangle.y1)
        self.assertLessEqual(rectangle.x2, config["image_dimentions"]["x"])
        self.assertLessEqual(rectangle.y2, config["image_dimentions"]["y"])
        self.assertIn(rectangle.color, Shape.colors)

    def test_random_shape(self):
        config = self.__class__.config
        shape = Shape.random(config["image_dimentions"], config["object_size"])
        self.assertIsInstance(shape, Shape)


