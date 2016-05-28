# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014, Luis Pedro Coelho <luis@luispedro.org>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# License: MIT (see COPYING.MIT file)

import numpy as np

from . import _imread

from .special import special

def _parse_formatstr(filename, formatstr, funcname):
    if formatstr is not None:
        return formatstr
    from os import path
    _,ext = path.splitext(filename)
    if len(ext) and ext[0] == '.':
        return ext[1:].lower()
    raise ValueError('imread.%s: Could not identify format from filename: `%s`' % (funcname,filename))

def _as_grey(im, as_grey):
    if not as_grey or len(im.shape) != 3: return im
    if im.shape[2] == 1:
        return im.squeeze()
    # these are the values that wikipedia says are typical
    transform = np.array([ 0.30,  0.59,  0.11])
    return np.dot(im, transform)

def imread(filename, as_grey=False, formatstr=None, return_metadata=False):
    '''
    im = imread(filename, as_grey=False, formatstr={filename extension}, return_metadata=False)
    im,meta = imread(filename, as_grey=False, formatstr={filename extension}, return_metadata=True)

    Read an image into a ndarray from a file.

    Parameters
    ----------
    filename : str
        filename
    as_grey : boolean, optional
        Whether to convert to grey scale image (default: no)
    formatstr : str, optional
        Format name. This is typically the same as the extension of the file
        and inferred from there. However, if you have a file whose extension
        does not correspond to the format, you can pass it explicitly.
    return_metadata : bool, optional
        Whether to return metadata (default: False)

    Returns
    -------
    im : ndarray
        The type of this array will depend on the contents of the file and of
        `as_grey`. Conversion from colour to grayscale will return a floating
        point image.
    meta: str
        Metadata. The metadata in the file Only returned if ``return_metadata``.

    See Also
    --------
    imread_from_blob : function
        Read from a in-memory string
    '''
    formatstr = _parse_formatstr(filename, formatstr, 'imread')
    reader = special.get(formatstr, _imread.imread)
    flags = ('m' if return_metadata else '')
    imdata,meta = reader(filename, formatstr, flags)
    imdata = _as_grey(imdata, as_grey)
    if return_metadata:
        return imdata, meta
    return imdata

imload = imread


def imread_from_blob(blob, formatstr=None, as_grey=False, return_metadata=False):
    '''
    imdata = imread_from_blob(blob, formatstr=None, as_grey=False, return_metadata={True})
    imdata,metadata = imread_from_blob(blob, formatstr=None, as_grey={False}, return_metadata=True)

    Read an image into a ndarray from an in-memory blob.

    Note that the parameter order is changed wrt. ``imread`` because
    **formatstr** is a mandatory parameter to this function!

    Parameters
    ----------
    blob : str (bytes in Py3)
        input data
    formatstr : str, optional
        Format name. This is the file extension typically associated with this
        format. If None is given, then ``detect_format`` is used to auto-detect
        the format.
    as_grey : boolean, optional
        Whether to convert to grey scale image (default: no)
    return_metadata : bool, optional
        Whether to return metadata (default: False)

    Returns
    -------
    im : ndarray
        The type of this array will depend on the contents of the file and of
        `as_grey`. Conversion from colour to grayscale will return a floating
        point image.
    meta: str
        Metadata. The metadata in the file Only returned if ``return_metadata``.

    See Also
    --------
    imread : function
        Read from a file on disk
    '''
    reader = _imread.imread_from_blob
    if formatstr is None:
        formatstr = detect_format(blob, is_blob=True)
    flags = ('m' if return_metadata else '')
    imdata,meta = reader(blob, formatstr, flags)
    imdata = _as_grey(imdata, as_grey)
    if return_metadata:
        return imdata,meta
    return imdata

imload_from_blob = imread_from_blob

def imread_multi(filename, formatstr=None):
    '''
    images = imread_multi(filename, formatstr={from filename})

    The file type is guessed from `filename`.

    Parameters
    ----------
    filename : str
        filename

    formatstr : str, optional
        file format. If ``None``, then it is derived from the filename.

    Returns
    -------
    images : list
    '''
    formatstr = _parse_formatstr(filename, formatstr, 'imread')
    return _imread.imread_multi(filename, formatstr, '')

imload_multi = imread_multi


def imsave(filename, array, formatstr=None, metadata=None, opts=None):
    '''
    imsave(filename, array, formatstr={auto-detect}, metadata={None}, opts={})

    Writes `array` into file `filename`

    Parameters
    ----------
    filename : str
        path on file system
    array : ndarray-like
    formatstr: str, optional
        format string
    metadata: bytes, optional
        metadata to write to file. Note that not all formats support writing
        metadata.
    opts: dict, optional
        This is a dictionary of options. Any non-applicable option is typically
        silently ignored. Currently, the following options are accepted:

        jpeg:quality
            An integer 1-100 determining the quality used by JPEG backend
            (default is libjpeg default: 75).

        tiff:compress
            Whether to use compression when saving TIFF (default: True)

        tiff:horizontal-predictor
            Whether to use horizontal prediction in TIFF. This defaults to True
            for 16 bit images, and to False for 8 bit images. This is because
            compressing 16 bit images without horizontal prediction is often
            counter-productive (see http://www.asmail.be/msg0055176395.html)

    '''
    if opts is None:
        opts = {}
    if not np.issubdtype(array.dtype, np.integer):
        raise TypeError('imread.imsave: only integer images are supported')
    array = np.ascontiguousarray(array)
    if formatstr is None:
        dot = filename.rfind('.')
        if dot < 0:
            raise ValueError('imread.imsave: dot not found in filename (%s)' % filename)
        formatstr = filename[dot+1:]
    if metadata is not None:
        opts['metadata'] = metadata
    _imread.imsave(filename, formatstr, array, opts)

imwrite = imsave

def detect_format(filename_or_blob, is_blob=False):
    '''
    Detect format using magic numbers

    Note that this function does not perform any checks that the data is OK,
    just checks magic numbers. Not all formats can be autodetected.

    Parameters
    ----------
    filename_or_blob : bytes (str in Python 2)
    is_blob : boolean, optional
        If true, then filename_or_blob is interpreted as a blob; otherwise,

    Returns
    -------
    format : str or None
        Representation of the format if detected. When no format matches, None
        is returned.
    '''
    return _imread.detect_format(filename_or_blob, bool(is_blob))
