import sys, os, time

test_dir = os.path.dirname(__file__)
src_dir = '../nested_query_string'
sys.path.insert(0, os.path.abspath(os.path.join(test_dir, src_dir)))
import unittest

from nested_query_string import NestedQueryString, UnsupportedParameterClassException


class NestedQueryStringTestCase(unittest.TestCase):
    def assertEqualQueryStrings(self, expected, actual):
        self.assertEqual(sorted(expected), sorted(actual))


class EncodeTest(NestedQueryStringTestCase):
    def runTest(self):
        qs = NestedQueryString.encode({'abc': 'def'})
        self.assertEqualQueryStrings(qs, 'abc=def')


class EncodeNumericTest(NestedQueryStringTestCase):
    def runTest(self):
        qs = NestedQueryString.encode({'abc': 1})
        self.assertEqualQueryStrings(qs, 'abc=1')


class EncodeFloatTest(NestedQueryStringTestCase):
    def runTest(self):
        qs = NestedQueryString.encode({'abc': 12345.12345})
        self.assertEqualQueryStrings(qs, 'abc=12345.12345')


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


class EncodeBooleanTest(NestedQueryStringTestCase):
    def runTest(self):
        encode_params = {
            'name': True,
            'deep': {
                'deep_name': False
            }
        }
        expected = 'name=true&deep[deep_name]=false'
        qs = NestedQueryString.encode(encode_params)
        self.assertEqual(expected, qs)


class EncodeMixedTest(NestedQueryStringTestCase):
    def runTest(self):
        qs = NestedQueryString.encode({'abc': ['def', {'ghi': 'jkl'}]})
        self.assertEqualQueryStrings(qs, 'abc[]=def&abc[][ghi]=jkl')


class EncodeExceptionTest(NestedQueryStringTestCase):
    def runTest(self):
        with self.assertRaises(UnsupportedParameterClassException):
            NestedQueryString.encode({'abc': EncodeExceptionTest})
