# Nested Query String Encoder
[![Build Status](https://travis-ci.org/cine-io/nested-query-string.svg?branch=master)](https://travis-ci.org/cine-io/nested-query-string)

Query string encoder that supports nested query strings in the format of [Rack::Utils](http://www.rubydoc.info/github/rack/rack/Rack/Utils) and [Node qs](https://github.com/hapijs/qs).

## Installation

install nested_query_string via pip:

    pip install nested_query_string

## Usage

```python
import nested_query_string
from nested_query_string import NestedQueryString

NestedQueryString.encode({'abc': 'def', 'ghi': 1})
# => 'abc=def&ghi=1'

# with nested list
NestedQueryString.encode({'abc': ['def', 'ghi']})
# => 'abc[]=def&abc[]=ghi'

# with nested dictionary
NestedQueryString.encode({'abc': {'def': 'ghi', 'jkl': 'mno'}, 'pqr': 'stu'})
# => 'abc[def]=ghi&abc[jkl]=mno&pqr=stu'
```

## Gotchas

1. The parameters are not guaranteed to be in a specific order.
* This library doesn't handle stringifing dates or other classes. If you're worried about sending unsupported classes as values, surround with a try/except:
  ```python
  import nested_query_string
  from nested_query_string import NestedQueryString, UnsupportedParameterClassException

  try:
    NestedQueryString.encode({'abc': NestedQueryString})
  except UnsupportedParameterClassException:
    # handle exception
  ```
