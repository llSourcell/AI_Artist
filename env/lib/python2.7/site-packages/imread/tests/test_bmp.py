from nose.tools import with_setup, raises
import numpy as np
from imread import imread
from . import file_path

def test_read():
    im = imread(file_path('star1.bmp'))
    assert np.any(im)
    assert im.shape == (128, 128, 3)

def test_indexed():
    im = imread(file_path('py-installer-indexed.bmp'))
    assert np.any(im)
    assert im.shape == (352, 162, 3)
    assert np.any(im[:,:,0])
    assert np.any(im[:,:,1])
    assert np.any(im[:,:,2])
