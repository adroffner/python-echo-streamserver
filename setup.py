#! /usr/bin/env python
#
# Echo StreamServer API Client for Python
# ======================================================================
# Build distutils packages
# ======================================================================
# See Configuration: ./setup.cfg
#
# RPM Spec can't find the right python interpreter w/o help.
# So, bdist_rpm needs some extra parameters.
#
#% ./setup.py bdist_rpm --python='/usr/bin/python2.6'
# ======================================================================

from distutils.core import setup
from echo import __version__

setup(name='python-echo-streamserver',
      version=__version__,
      license='PSF Licensed',
      description='Echo StreamServer API Client',
      long_description="""Echo StreamServer API
This is a Python version of the Echo StreamServer API.
http://aboutecho.com/developers/index.html
>>> import echo
""",
      author='Andrew Droffner',
      author_email='adroffne@advance.net',
      url='http://code.google.com/p/python-echo-streamserver/',
      packages=['echo', 'echo.feeds', 'echo.items', 'echo.eql'],
      scripts=['scripts/eql_shell.py'],
     )

