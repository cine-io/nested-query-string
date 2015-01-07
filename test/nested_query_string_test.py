import sys, os, time
testdir = os.path.dirname(__file__)
srcdir = '../nested_query_string'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
import unittest

_ver = sys.version_info
#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

#: Python 3.2.x
is_py32 = (is_py3 and _ver[1] == 2)

#: Python 3.3.x
is_py33 = (is_py3 and _ver[1] == 3)

#: Python 3.4.x
is_py34 = (is_py3 and _ver[1] == 4)

from nested_query_string import NestedQueryString, UnsupportedParameterClassException

class EncodeTest(unittest.TestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': 'def'})
    self.assertEqual(qs, 'abc=def')

class EncodeNumericTest(unittest.TestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': 1})
    self.assertEqual(qs, 'abc=1')

class EncodeNumericAndStringTest(unittest.TestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': 'def', 'ghi': 1})
    if is_py33:
      expected = 'ghi=1&abc=def'
    else:
      expected = 'abc=def&ghi=1'
    self.assertEqual(qs, expected)

class EncodeDictTest(unittest.TestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': {'def': 'ghi', 'jkl': 'mno'}, 'pqr': 'stu'})

    if is_py2:
      expected = 'pqr=stu&abc[jkl]=mno&abc[def]=ghi'
    if is_py32:
      expected = 'pqr=stu&abc[jkl]=mno&abc[def]=ghi'
    if is_py33:
      expected = 'pqr=stu&abc[jkl]=mno&abc[def]=ghi'
    if is_py34:
      expected = 'pqr=stu&abc[def]=ghi&abc[jkl]=mno'
    self.assertEqual(qs, expected)

class EncodeListTest(unittest.TestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': ['def', 'ghi']})
    self.assertEqual(qs, 'abc[]=def&abc[]=ghi')

class EncodeMixedTest(unittest.TestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': ['def', {'ghi': 'jkl'}]})
    self.assertEqual(qs, 'abc[]=def&abc[][ghi]=jkl')

class EncodeExceptionTest(unittest.TestCase):
  def runTest(self):
    with self.assertRaises(UnsupportedParameterClassException):
      NestedQueryString.encode({'abc': EncodeExceptionTest})
