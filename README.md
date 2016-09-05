Overview
============
A project that trains a  convolutional neural network over a dataset to repaint an novel image in the style of a given painting. This is the implementation of Neural Style Transfer from the paper [A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576) in Keras 1.0.2. This is also the code for 'Build an AI Artist' on [Youtube](https://youtu.be/9Mxw_ilpvwA)

![Alt Text](https://raw.githubusercontent.com/titu1994/Neural-Style-Transfer/master/images/Blue%20Moon%20Lake.gif)


Dependencies
============

* Numpy (http://www.numpy.org/)
* Keras (http://keras.io/#installation)
* Scipy  (https://www.scipy.org/install.html)
* Theano (http://deeplearning.net/software/theano/install.html#install) 
* h5py (http://docs.h5py.org/en/latest/build.html)
* sklearn (http://scikit-learn.org/stable/install.html)
* Pillow (https://pillow.readthedocs.io/en/latest/installation.html)
* CUDA (GPU) (http://docs.nvidia.com/cuda/cuda-getting-started-guide-for-mac-os-x/)
* CUDNN (GPU) (https://developer.nvidia.com/cudnn)
* VGG16 file https://drive.google.com/file/d/0Bz7KyqmuGsilT0J5dmRCM0ROVHc/view?usp=sharing

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies

If you have dependency version issues, use [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) 

Basic Usage
===========

There are 3 images to identify when we run the script

1. Your base image (to artify)
2. Your reference image (the art to learn from)
3. Your generated image

Run the following comand to generate an image in your chosen style

`python network.py --base_image_path /path/to/your/image --style_reference_image_path /path/to/your/painting --result_prefix /path/to/generated/file/you/create` 

Other optional commands are 

- `--image_size`: Size of your output image
- `--content_weight`: How much to weigh the content
- `--style_weight`: How much to weigh the style
- `-style_scale`: How much to scale the style
- `--total_variation_weight`: Uniformity of the generated image
- `--num_iter`: Nmber of iterations
- `--rescale_image`: to rescale or not to rescale
- `--rescale_method`: rescale algorithm 
- `--maintain_aspect_ratio`: to maintain aspect ratio or not 
- `--content_layer`: which layer to focus on for content generation

I'd run this on AWS, but you can run this locally too if you have a GPU. On a 980M GPU, the time required for each epoch depends on mainly image size (gram matrix size) :

- For a 400x400 gram matrix, each epoch takes approximately 11-13 seconds. 
- For a 512x512 gram matrix, each epoch takes approximately 18-22 seconds. 
- For a 600x600 gram matrix, each epoch takes approximately 28-30 seconds. 

Credits
===========
Credit for the vast majority of code here goes to [Somsubra Majumdar](https://github.com/titu1994). I've merely created a wrapper around all of the important functions to get people started.
