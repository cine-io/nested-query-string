import sys, os, time
testdir = os.path.dirname(__file__)
srcdir = '../nested_query_string'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
import unittest

from nested_query_string import NestedQueryString, UnsupportedParameterClassException

class NestedQueryStringTestCase(unittest.TestCase):
  def assertEqualQueryStrings(self, expected, actual):
    expectedValues = expected.split("&")
    actualValues = actual.split("&")
    self.assertEqual(sorted(expected), sorted(actual))

class EncodeTest(NestedQueryStringTestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': 'def'})
    self.assertEqualQueryStrings(qs, 'abc=def')

class EncodeNumericTest(NestedQueryStringTestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': 1})
    self.assertEqualQueryStrings(qs, 'abc=1')

class EncodeNumericAndStringTest(NestedQueryStringTestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': 'def', 'ghi': 1})
    self.assertEqualQueryStrings(qs, "abc=def&ghi=1")

class EncodeDictTest(NestedQueryStringTestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': {'def': 'ghi', 'jkl': 'mno'}, 'pqr': 'stu'})
    self.assertEqualQueryStrings(qs, "abc[def]=ghi&abc[jkl]=mno&pqr=stu")

class EncodeListTest(NestedQueryStringTestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': ['def', 'ghi']})
    self.assertEqualQueryStrings(qs, 'abc[]=def&abc[]=ghi')

class EncodeMixedTest(NestedQueryStringTestCase):
  def runTest(self):
    qs = NestedQueryString.encode({'abc': ['def', {'ghi': 'jkl'}]})
    self.assertEqualQueryStrings(qs, 'abc[]=def&abc[][ghi]=jkl')

class EncodeExceptionTest(NestedQueryStringTestCase):
  def runTest(self):
    with self.assertRaises(UnsupportedParameterClassException):
      NestedQueryString.encode({'abc': EncodeExceptionTest})
