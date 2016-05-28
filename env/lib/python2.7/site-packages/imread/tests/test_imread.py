from nose.tools import raises
from . import file_path
from imread import imread

def test_with_dot():
    f = imread(file_path('good.png'))
    assert f.shape == (2,2)

def test_uppercase():
    f = imread(file_path('GOOD.PNG'))
    assert f.shape == (2,2)

@raises(ValueError)
def test_no_ext():
    imread('file_without_extension')


def test_formatstr():
    f = imread(file_path('good'), formatstr='png')
    assert f.shape == (2,2)


def test_as_grey():
    im = imread(file_path('star1.bmp'), as_grey=False)
    assert len(im.shape) == 3
    im = imread(file_path('star1.bmp'), as_grey=True)
    assert len(im.shape) == 2
