#!/usr/bin/env python

from uncompyle6 import uncompyle
from uncompyle6.main import decompile
from xdis import sysinfo2float
import sys, inspect

def uncompyle_test():
    frame = inspect.currentframe()
    try:
        co = frame.f_code
        decompile(sysinfo2float(), co, sys.stdout, 1, 1)
        print()
    finally:
        del frame

uncompyle_test()