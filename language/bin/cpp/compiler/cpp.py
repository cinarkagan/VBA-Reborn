import os
import sys

if len(sys.argv) == 2:
    path = sys.argv[0]
    os.system("g++ "+path)