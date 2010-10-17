# from distutils.core import setup, Extension
# import os
# currdir = os.path.dirname(os.path.realpath(__file__))


# levmar = Extension('_levmar', ['src/pylevmar.c', 'src/lm.c',  'src/Axb.c',  'src/misc.c',  'src/lmlec.c',  'src/lmbc.c',  'src/lmblec.c',  'src/lmbleic.c' ],
#                    libraries = ['m', 'blas', 'lapack'],
#                    extra_compile_args = ['-g'],
#                    library_dirs = ['/usr/lib'],
#                    runtime_library_dirs = [currdir],
#                    include_dirs = ['src'],
#                    depends = ['src/pylevmar.h'])

# setup(name = 'pylevmar',
#       version = '0.1',
#       description = 'Python Bindings to levmar',
#       author = 'Alastair Tse',
#       author_email = 'alastair@liquidx.net',
#       url = 'http://www.liquidx.net/pylevmar/',
#       license = 'BSD',
#       ext_modules = [levmar]
#       )

#!/usr/bin/env python
""" PYLEVMAR, Python bindings to LEVMAR
Levenberg-Marquardt algorithm for (constrained) least-squares problems
"""
DOCLINES = __doc__.split("\n")

# build with: $ python setup.py build_ext --inplace
# clean with: # python setup.py clean --all
# see:
# http://www.scipy.org/Documentation/numpy_distutils
# http://docs.cython.org/docs/tutorial.html

import os
from distutils.core import setup, Extension
from distutils.core import Command
from numpy.distutils.misc_util import get_numpy_include_dirs

# ADAPT THIS TO FIT YOUR SYSTEM
extra_compile_args = ['-g']
include_dirs = [get_numpy_include_dirs(),'src']
library_dirs = ['src']
libraries = ['m','blas', 'lapack']

# PACKAGE INFORMATION
CLASSIFIERS = """\
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: C
Programming Language :: Python
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Linux
"""

NAME                = 'pylevmar'
MAINTAINER          = "Sebastian F. Walter"
MAINTAINER_EMAIL    = "sebastian.walter@gmail.com"
DESCRIPTION         = DOCLINES[0]
LONG_DESCRIPTION    = "\n".join(DOCLINES[2:])
URL                 = "http://www.github.com/b45ch1/pyadolc"
DOWNLOAD_URL        = "http://www.github.com/b45ch1/pyadolc"
LICENSE             = 'GPL'
CLASSIFIERS         = filter(None, CLASSIFIERS.split('\n'))
AUTHOR              = "Alastair Tse, Sebastian F. Walter"
AUTHOR_EMAIL        = "alastair@liquidx.net, sebastian.walter@gmail.com"
PLATFORMS           = ["Linux"]
MAJOR               = 0
MINOR               = 1
MICRO               = 0
ISRELEASED          = False
VERSION             = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

# IT IS USUALLY NOT NECESSARY TO CHANGE ANTHING BELOW THIS POINT
# override default setup.py help output
import sys
if len(sys.argv) == 1:
    print """

    You didn't enter what to do!

    Options:
    1: build the extension with
    python setup.py build_ext --inplace

    2: remove generated files with
    python setup.py clean --all


    Remark: This is an override of the default behaviour of the distutils setup.
    """
    exit()

class clean(Command):
    """
    This class is used in numpy.distutils.core.setup.
    When $python setup.py clean is called, an instance of this class is created and then it's run method is called.
    """

    description = "Clean everything"
    user_options = [("all","a","the same")]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        pass

    def run(self):
        import os
        os.system("rm -rf build")
        os.system("rm *.pyc")


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# find all files that should be included
packages, data_files = [], []
for dirpath, dirnames, filenames in os.walk('levmar'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

options_dict = {}
options_dict.update({
'name':NAME,
'version':VERSION,
'description' :DESCRIPTION,
'long_description' : LONG_DESCRIPTION,
'license':LICENSE,
'author':AUTHOR,
'platforms':PLATFORMS,
'author_email': AUTHOR_EMAIL,
'url':URL,
'packages' :packages,
'ext_package' : 'levmar',
'ext_modules': [Extension('_levmar', ['levmar/src/pylevmar.c', 'levmar/src/lm.c',  'levmar/src/Axb.c',  'levmar/src/misc.c',  'levmar/src/lmlec.c',  'levmar/src/lmbc.c',  'levmar/src/lmblec.c',  'levmar/src/lmbleic.c' ],
                include_dirs = include_dirs,
                library_dirs = library_dirs,
                runtime_library_dirs = library_dirs,
                libraries = libraries),
],

'cmdclass' : {'clean':clean}
})

setup(**options_dict)
                                         
