from shape import Circle, Rectangle, Triangle, Shape
import random

class QandA:
    def __init__(self, shapes):
        self.question = None
        self.answer = None
        self.shapes = shapes

    @classmethod
    def qanda_classes(cls):
        return[BinaryExistenceQandA, NumericExistenceQandA]

class ExistenceQandA(QandA):
    def __init__(self, shapes):
        super(ExistenceQandA, self).__init__(shapes)

    def new_text(self, shape_class, shape_color):
        pass

    def random_qanda(self):
        self.shape_class = random.choice(Shape.shape_classes())
        self.shape_color = random.choice(Shape.colors)
        self.new_text(self.shape_class, self.shape_color)

    def count_matches(self, shape_class, shape_color):
        class_matches = Shape.filterby_class(self.shapes, shape_class)
        return len(Shape.filterby_color(class_matches, shape_color))

class BinaryExistenceQandA(ExistenceQandA):
    def __init__(self, shapes):
        super(BinaryExistenceQandA, self).__init__(shapes)

    def new_text(self, shape_class, shape_color):
        count = super(BinaryExistenceQandA, self).count_matches(shape_class, shape_color)

        self.question = 'Are there any {} {}s?'.format(shape_color, shape_class.__name__.lower())
        self.answer = 'yes' if (count > 0) else 'no'

class NumericExistenceQandA(ExistenceQandA):
    def __init__(self, shapes):
        super(NumericExistenceQandA, self).__init__(shapes)

    def new_text(self, shape_class, shape_color):
        count = super(NumericExistenceQandA, self).count_matches(shape_class, shape_color)

        self.question = 'How many {} {}s are there?'.format(shape_color, shape_class.__name__.lower())
        self.answer = str(count)