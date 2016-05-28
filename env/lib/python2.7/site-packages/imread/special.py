# -*- coding: utf-8 -*-
# Copyright (C) 2012-2013, Luis Pedro Coelho <luis@luispedro.org>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# License: MIT (see COPYING.MIT file)

import imread

def readxcf(xcf_filename, formatstr, _flags):
    '''
    im = readxcf(xcf_filename, formatstr)

    Returns a numpy array with the (flattened) XCF file.

    Depends on `xcf2png` being available.

    Parameters
    ----------
    xcf_filename : str
        Filename

    formatstr : str
        format. Must be 'xcf'

    Returns
    -------
    im : ndarray
    '''
    from os import system, unlink
    from tempfile import NamedTemporaryFile
    if formatstr != 'xcf':
        raise ValueError('imread.imread.readxcf: Format string must be \'xcf\'')

    N = NamedTemporaryFile(suffix='.png')
    output = system('xcf2png %s >%s' % (xcf_filename,N.name))
    if output:
        raise OSError('imread.readxcf: xcf format is only supported through the xcf2png utility, which imread could not run')
    return imread.imread(N.name, return_metadata=True)

special = {
    'xcf' : readxcf,
}
