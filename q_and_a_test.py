import unittest
from q_and_a import BinaryExistenceQandA, NumericExistenceQandA
from shape import Circle, Rectangle, Triangle, Shape

class Test_Shapes(unittest.TestCase):

    def test_binary_existence(self):
        shapes = [Triangle(0, 0, 10, 0, 5, 10, "red"), Circle(10, 10, 5, "blue"), Circle(20, 20, 10, "red")]
        qanda = BinaryExistenceQandA(shapes)
        qanda.new_text(Triangle, "red")
        self.assertEquals(qanda.question, 'Are there any red triangles?')
        self.assertEquals(qanda.answer, 'yes')

        qanda = BinaryExistenceQandA(shapes)
        qanda.new_text(Circle, "yellow")
        self.assertEquals(qanda.question, 'Are there any yellow circles?')
        self.assertEquals(qanda.answer, 'no')

    def test_numeric_existence(self):
        shapes = [Triangle(0, 0, 10, 0, 5, 10, "purple"), Circle(10, 10, 5, "blue"), Circle(20, 20, 10, "blue")]
        qanda = NumericExistenceQandA(shapes)
        qanda.new_text(Triangle, "purple")
        self.assertEquals(qanda.question, 'How many purple triangles are there?')
        self.assertEquals(qanda.answer, '1')

        qanda = NumericExistenceQandA(shapes)
        qanda.new_text(Circle, "blue")
        self.assertEquals(qanda.question, 'How many blue circles are there?')
        self.assertEquals(qanda.answer, '2')