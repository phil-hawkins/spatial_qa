import unittest
import json
from shape import Circle, Rectangle, Triangle, Shape

class Test_Shapes(unittest.TestCase):
    config = json.load(open('config.json')) 

    @classmethod
    def setUpClass(cls):
        cls.config = json.load(open('config.json'))

    def test_circle_rand_init(self):
        config = self.__class__.config
        circle = Circle.random_init(config["image_dimentions"], config["object_size"])
        self.assertGreaterEqual(circle.x1, 0)
        self.assertGreaterEqual(circle.y1, 0)
        self.assertGreaterEqual(circle.x2, circle.x1)
        self.assertGreaterEqual(circle.y2, circle.y1)
        self.assertLessEqual(circle.x2, config["image_dimentions"]["x"])
        self.assertLessEqual(circle.y2, config["image_dimentions"]["y"])
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

    def test_triangle_rand_init(self):
        config = self.__class__.config
        triangle = Triangle.random_init(config["image_dimentions"], config["object_size"])
        self.assertGreaterEqual(triangle.vx1, 0)
        self.assertGreaterEqual(triangle.vy1, 0)
        self.assertGreaterEqual(triangle.vx2, 0)
        self.assertGreaterEqual(triangle.vy2, 0)
        self.assertGreaterEqual(triangle.vx3, 0)
        self.assertGreaterEqual(triangle.vy3, 0)
        self.assertLessEqual(triangle.vx1, config["image_dimentions"]["x"])
        self.assertLessEqual(triangle.vy1, config["image_dimentions"]["y"])
        self.assertLessEqual(triangle.vx2, config["image_dimentions"]["x"])
        self.assertLessEqual(triangle.vy2, config["image_dimentions"]["y"])
        self.assertLessEqual(triangle.vx3, config["image_dimentions"]["x"])
        self.assertLessEqual(triangle.vy3, config["image_dimentions"]["y"])
        self.assertIn(triangle.color, Shape.colors)        

    def test_random_shape(self):
        config = self.__class__.config
        shape = Shape.random(config["image_dimentions"], config["object_size"])
        self.assertIsInstance(shape, Shape)

    def test_intersection_area(self):
        # shape bounding boxes intesect
        shape1 = Shape(10, 10, 40, 40)
        shape2 = Shape(30, 30, 50, 50)
        ia = shape1.intersection_area(shape2)
        self.assertEquals(ia, 100)

        # shape bounding boxes don't intesect
        shape1 = Shape(10, 10, 40, 40)
        shape2 = Shape(30, 40, 50, 50)
        ia = shape1.intersection_area(shape2)
        self.assertEquals(ia, 0)

    def test_intersects_any(self):
        # shape bounding boxes intesect
        shape1 = Shape(10, 10, 40, 40)
        shapes = [Shape(30, 30, 50, 50), Shape(30, 40, 50, 50)]
        self.assertTrue(shape1.intersects_any(shapes))

        # shape bounding boxes don't intesect
        shape2 = Shape(0, 0, 10, 10)
        self.assertFalse(shape2.intersects_any(shapes))

    def test_shape_classes(self):
        sc = Shape.shape_classes()
        self.assertEquals(len(sc), 3)

    def test_filterby_class(self):
        shapes = [Triangle(0, 0, 10, 0, 5, 10, "red"), Circle(10, 10, 5, "blue"), Circle(20, 20, 10, "yellow")]
        shapes = Shape.filterby_class(shapes, Circle)
        self.assertEquals(len(shapes), 2)

    def test_filterby_color(self):
        shapes = [Triangle(0, 0, 10, 0, 5, 10, "red"), Circle(10, 10, 5, "blue"), Circle(20, 20, 10, "red")]
        shapes = Shape.filterby_color(shapes, "red")
        self.assertEquals(len(shapes), 2)