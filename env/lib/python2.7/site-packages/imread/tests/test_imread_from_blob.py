import imread
from imread.imread import imread_from_blob
import numpy as np
def test_imread_from_blob():
    def compare_with_blob(filename, formatstr):
        from os import path
        filename = path.join(
                        path.dirname(__file__),
                        'data',
                        filename)
        fromfile= imread.imread(filename)
        fromblob = imread_from_blob(open(filename, 'rb').read(), formatstr)
        assert np.all(fromblob == fromfile)
    yield compare_with_blob, 'good.png', 'png'
    yield compare_with_blob, 'good.png', None
    yield compare_with_blob, 'GOOD.PNG', 'png'
    yield compare_with_blob, 'mono.tif', 'tif'
    yield compare_with_blob, 'mono.tif', 'tiff'
    yield compare_with_blob, 'py-installer-indexed.bmp', 'bmp'
