"""
nested_query_string
=======

:copyright: (c) 2014 by cine.io
:license: MIT, see LICENSE for more details

"""

from .nested_query_string import NestedQueryString, UnsupportedParameterClassException

from .version import __version__
__all__ = [NestedQueryString, UnsupportedParameterClassException]
__author__ = 'cine.io engineering'
__copyright__ = 'Copyright 2014 cine.io'
__license__ = 'MIT'
__title__ = 'nested_query_string'
__version_info__ = tuple(int(i) for i in __version__.split('.'))
