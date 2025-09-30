# Module path: mcards.gameplay.factory.unit_factory

from mcards.enums import *
from mcards.gdefs import *
from mcards.gvars import *

from mcards.gameplay.core.units import Hero, Troop, Spell, Building

class TroopGravedigger(Troop):
	"""
	The first initial card, a near-combat girl. No any extras in her base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Gravedigger status.
		"""
		
		super().__init__(pygame.math.Vector2(0, 0), 1000, 730, 67, 900, 1100, 1500, 2000, MovementType.GROUND, TargetType.ONLY_GBH)

class TroopIndian(Troop):
	"""
	The second initial card, two ranged boys. No any extras in his base classes.
	"""
	
	def __init__(self, blue_team, index):
		"""
		Initialize the Indians status.
		"""
		
		super().__init__(pygame.math.Vector2(1 if index == 0 else -1, 0), 1000, 178, 47, 800, 900, 5000, 2500, MovementType.GROUND, TargetType.ANY)

class TroopPelican(Troop):
	"""
	The third initial card, a win-condition bird. Extras attributes in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Pelican status.
		"""
		
		super().__init__(pygame.math.Vector2(0, 0), 1200, 985, 110, 500, 2000, 100, 1000, MovementType.GROUND, TargetType.ONLY_BH)
		
		self.__explosion_damages = {
			"hero": 128,
			"troop": 256,
			"building": 384,
		}

class BuildingBomb(Building):
	"""
	The fourth initial card, a defensive bomb. No extras in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Bomb status.
		"""
		
		super().__init__(pygame.math.Vector2(0,0), 1000, 444, 0, 9999, 9999, 10000, TargetType.ANY)

def initialize_units():
	register_troop("troop_gravedigger", TroopGravedigger)
	register_troop("troop_indian", TroopIndian)
	register_troop("troop_pelican", TroopPelican)
	register_building("building_bomb", BuildingBomb)
