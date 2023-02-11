import os, sys
try:
    __import__("vip").Main()
except Exception as e:
    exit(str(e))
