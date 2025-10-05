"""
Caminho do módulo: mcards
"""

from . import register
from .globals import gvars
from .globals import gdefs 

__all__ = ["register", "gvars", "gdefs"]
__version__ = "0.0.1"

print(f"Hello from the Multiverse Cards v{__version__}")
