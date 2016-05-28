from nose.tools import with_setup, raises
import numpy as np
from imread import imread, imsave, imread_multi
from . import file_path

_filename = 'imread_testing_file.tiff'

def _remove_file():
    from os import unlink
    try:
        unlink(_filename)
    except:
        pass

@raises(RuntimeError)
def test_error():
    imread(file_path('error.tif'))


@with_setup(teardown=_remove_file)
def test_read_back():
    simple = np.arange(16*16).reshape((16,16))
    simple = simple.astype(np.uint8)
    imsave(_filename, simple)
    back = imread(_filename)
    assert np.all(simple == back)

@with_setup(teardown=_remove_file)
def test_read_back_16():
    np.random.seed(21)
    simple = np.random.random_sample((128,128))
    simple *= 8192
    simple = simple.astype(np.uint16)
    imsave(_filename, simple)
    back = imread(_filename)
    assert np.all(simple == back)

def test_monochrome():
    mono = imread(file_path('mono.tif'))
    assert mono.shape == (8,8)
    z = np.zeros((8,8),np.uint8)
    z.flat[::3] = 1
    assert np.all(z == mono)


def test_multi():
    assert len(imread_multi(file_path('stack.tiff'))) == 2

@with_setup(teardown=_remove_file)
def test_read_back_with_metadata():
    simple = np.arange(16*16).reshape((16,16))
    simple = simple.astype(np.uint8)
    meta = b'123qwe'
    imsave(_filename, simple, metadata=meta)
    back,meta_read = imread(_filename, return_metadata=True)
    assert np.all(simple == back)
    assert meta == meta_read


@with_setup(teardown=_remove_file)
def test_read_back_colour():
    im = np.arange(256).astype(np.uint8).reshape((32,-1))
    im = np.dstack([im, im*0, 255-im])
    imsave(_filename, im)
    im2 = imread(_filename)
    assert im.shape == im2.shape
    assert np.all(im == im2)

@with_setup(teardown=_remove_file)
def test_horizontal_predictor():
    im = imread(file_path('arange512_16bit.png'))
    im2 = im.copy()
    imsave(_filename, im, opts={'tiff:horizontal-predictor': True})
    assert np.all(im == im2)

    im3 = imread(_filename)
    assert np.all(im == im3)

