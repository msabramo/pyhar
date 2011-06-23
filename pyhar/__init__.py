#!/usr/bin/env python

try:
    import json    
except ImportError:
    import simplejson as json
    
__version__ = '0.1.0'

__all__ = [
    'dump', 'dumps', 'load', 'loads',
    'HAREncoder', 'HARDecoder', 'HARDecodeError'
]

__author__ = 'Flier Lu <flier.lu@gmail.com>'

from encoder import HAREncoder
from decoder import HARDecoder, HARDecodeError

def dump(obj, fp, cls=HAREncoder, **kwds):
    json.dump(fp, cls(**kwds).encode(obj))

def dumps(obj, cls=HAREncoder, **kwds):
    return json.dumps(cls(**kwds).encode(obj))

def load(fp, encoding=None, cls=HARDecoder, **kwds):
    return loads(fp.read(), encoding=encoding, cls=cls, **kwds)

def loads(s, encoding=None, cls=HARDecoder, **kwds):
    obj = json.loads(s, self.encoding)
    
    return cls(encoding=encoding, **kwds).decode(obj)