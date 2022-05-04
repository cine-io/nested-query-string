import sys

_ver = sys.version_info
#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

if is_py2:
  from urllib import quote

elif is_py3:
  from urllib.parse import quote

class UnsupportedParameterClassException(Exception):
  def __init__(self, value, obj):
    self.value = value
    self.obj = obj
  def __str__(self):
    return repr(self.value) + " <" + repr(self.obj.__class__.__name__) +":" + repr(self.obj) +">"

class NestedQueryString:

  @classmethod
  def encode(cls, value, key = None):
    class_name = value.__class__
    if class_name == dict:
      result = []
      for k, v in value.items():
        result.append(cls.encode(v, cls.__append_key(key, k)))
      result = '&'.join(result)
      return result
    elif class_name == list:
      result = []
      for v in value:
        result.append(cls.encode(v, key+'[]'))
      result = '&'.join(result)
      return result
    elif class_name == str:
      return key + "=" + cls.__escape(value)
    elif class_name == int:
      return key + "=" + str(value)
    elif class_name == bool:
      return value
    elif class_name == None:
      return ''
    else:
      raise UnsupportedParameterClassException('Unknown value class', value)

  @classmethod
  def __escape(cls, value):
    return quote(value)

  @classmethod
  def __append_key(cls, root_key, key):
    if root_key is None:
      return key
    else:
      return root_key + "["+key+"]"
