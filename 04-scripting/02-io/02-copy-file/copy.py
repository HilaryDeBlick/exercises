#!/usr/bin/env python
import os
import shutil
import sys

shutil.copy(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]))