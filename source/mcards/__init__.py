__all__ = ["engine", "enums", "gvars", "gdefs"]

from . import engine
from . import enums
from . import gdefs
from . import gvars

from .gameplay.core import units, cards
from .gameplay.factory import unit_factory, card_factory
from .gameplay import player, game_state

__version__ = "1.0.0"

gvars.ENGINE = engine.Engine()

print(f"Hello from Multiverse Cards v{__version__}")
