# VQA
Visual Question and Answer on spatial data from a generated synthetic geometrical dataset

## The Generator

A dataset is created by running the generator:

    python dataset_generator.py

Image files are w


### Configuration

The generator is parameterised by the config file **config.json**

#### image_dimentions

The image size.

#### object_size

Range of possible object sizes as a proportion of the image size.

#### object_count

How many objects in each image.  Ramdomly selected from this range.

#### questions_per_image

The number of questions generated for each image

#### stop_intersection

If set to true, palcement of shapes is constrained so that bounding boxes don't intersect.

#### out_dir

The output directory for the dataset.

#### file_prefix

The image filename prefix.

#### image_count

The number of images to be generated in the dataset.
    
#### thumbnail_scale

Not currently used.