import json
import random
from pprint import pprint
from shape import Circle, Rectangle, Shape
from PIL import Image, ImageDraw


config = json.load(open('config.json'))
# size of image
canvas = (config["image_dimentions"]["x"], config["image_dimentions"]["y"])
# scale ratio
scale = config["thumbnail_scale"]
thumb = canvas[0]/scale, canvas[1]/scale

print(config)

for i in range(config["image_count"]):
    file_name = './dataset/{}{}.png'.format(config["file_prefix"], i)

    # build the shape list
    shape_count = random.randint(config["object_count"]["min"], config["object_count"]["max"])
    shapes = []
    for s in range(shape_count):
        shapes.append(Shape.random(config["image_dimentions"], config["object_size"]))

    print('{} - {} shapes : {}'.format(file_name, shape_count, shapes))

    # draw the image
    im = Image.new('RGBA', canvas, (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)    
    for shape in shapes:
        shape.draw(draw)
    # make thumbnail
    #im.thumbnail(thumb)

    # save image
    im.save(file_name)
