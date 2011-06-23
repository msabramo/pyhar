#!/usr/bin/env python
import unittest

from pyhar import *

class TestDecode(unittest.TestCase):
    def testDecodeDatetime(self):
        d = HARDecoder()
        self.assertEquals(datetime.datetime(2009, 4, 16, 13, 7, 25, 123),
                          d._decodeDatetime("2009-04-16T12:07:25.123+01:00"))