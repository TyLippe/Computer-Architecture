#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
# from branch_test import *

cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()