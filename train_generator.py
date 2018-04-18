import json
import random
from pprint import pprint



config = json.load(open('config.json'))

print(config)

for i in range(config["image_count"]):
    file_name = '{}{}.png'.format(config["file_prefix"], i)

    # build the shape dictionary
    shape_count = random.randint(config["object_count"]["min"], config["object_count"]["max"])

    print('{} - {} shapes'.format(file_name, shape_count))
