#!/usr/bin/env python
"""
Scale kicad_mod format footprint.

$ scale_kicad_mod.py 0.3 < old.kicad_mod > new.kicad_mod

The MIT License

Copyright (c) 2013 David Siroky (siroky@dasir.cz)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys
import re

###########################################################################
###########################################################################

def scale(kicad_mod, ratio):
    def scale_xy(match):
        return "xy %f %f" % (float(match.group(1)) * ratio,
                            float(match.group(2)) * ratio)
    def scale_width(match):
        return "width %f" % (float(match.group(1)) * ratio)
    buf = re.sub(r"xy +(-?\d+.\d+) (-?\d+.\d+)", scale_xy, kicad_mod)
    buf = re.sub(r"width +(\d+.\d+)", scale_width, buf)
    return buf

###########################################################################
###########################################################################

print scale(sys.stdin.read(), float(sys.argv[1]))
