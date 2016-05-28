from nose.tools import raises
from imread import imread
from . import file_path

@raises(RuntimeError)
def test_error():
    imread(file_path('error.unknown'))
