from spectcl.client import *
from spectcl.data import Spectrum

__version__ = '0.2.0'
__author__ = 'Tong Zhang <zhangt@frib.msu.edu>'
__name__ = "PySpecTcl"
__doc__ ="""Python interface to SpecTcl REST server."""

def info():
    print(f"{__name__} (v{__version__}): {__doc__}\nDeveloped by: {__author__}")