from imread import imsave
import numpy as np
from nose.tools import raises

@raises(Exception)
def test_non_existing():
    # in 0.2.5 this led to a hard crash!
    arr = np.arange(64,dtype=np.uint8).reshape((8,8))
    imsave('/tmp/test-me.png', arr, 'some format which does not exist')


@raises(TypeError)
def test_bad_args():
    arr = np.arange(64,dtype=np.uint8).reshape((8,8))
    imsave('/tmp/test-me.png', arr, arr)


@raises(TypeError)
def test_save_float():
    im = (np.arange(64*64).reshape((64,64)) % 32 ) * 2.
    imsave('test.jpeg', im)
