from nose.tools import with_setup, raises
import numpy as np
from imread import imread, imsave
from . import file_path
_filename = 'imread_testing_file.jpg'

def remove_files(filelist):
    def perform_removal():
        from os import unlink
        for f in filelist:
            try:
                unlink(f)
            except:
                pass
    def wrap(f):
        return with_setup(teardown=perform_removal)(f)
    return wrap

@remove_files([_filename])
def test_jpeg():
    f = np.arange(64*16).reshape((64,16))
    f %= 16
    f = f.astype(np.uint8)
    imsave(_filename, f, 'jpeg')
    g = imread(_filename).squeeze()
    assert np.mean(np.abs(f.astype(float)-g)) < 1.


@raises(RuntimeError)
def test_error():
    imread(file_path('error.jpg'))

@raises(OSError)
def test_error_noent():
    imread(file_path('this-file-does-not-exist.jpeg'))



@remove_files(['imread_def.jpg', 'imread_def91.jpg'])
def test_quality():
    def pixel_diff(a):
        return np.mean(np.abs(a.astype(float) - data))

    data = np.arange(256*256*3)
    data %= 51
    data = data.reshape((256,256,3))
    data = data.astype(np.uint8)
    imsave('imread_def.jpg', data)
    imsave('imread_def91.jpg', data, opts={'jpeg:quality': 91} )
    readback    = imread('imread_def.jpg')
    readback91  = imread('imread_def91.jpg')
    assert pixel_diff(readback91) < pixel_diff(readback)
