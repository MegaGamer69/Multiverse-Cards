__all__ = ["engine", "enums", "gvars"]

from . import engine
from . import enums
from . import gvars

from .gameplay.core import units, cards
from .gameplay import player
from .gameplay import game_state

__version__ = "1.0.0"

print(f"Hello from Multiverse Cards v{__version__}")
