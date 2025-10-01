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
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			1000, # Deploy time.
			680, # Hitpoints.
			67, # Damage.
			900, # First attack delay in ms.
			1100, # Attack delay in ms.
			1500, # Attack range.
			2000, # Move Speed.
			MovementType.GROUND, # Movement type.
			TargetType.ONLY_GBH # Target types.
		)

class TroopIndian(Troop):
	"""
	The second initial card, two ranged boys. No any extras in his base classes.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Indians status.
		"""
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			1000, # Deploy time.
			175, # Hitpoints.
			45, # Damage.
			600, # First attack delay in ms.
			900, # Attack delay in ms.
			4500, # Attack range.
			2500, # Move Speed.
			MovementType.GROUND, # Movement type.
			TargetType.ANY # Target types.
		)

class TroopPelican(Troop):
	"""
	The third initial card, a win-condition bird. Extras attributes in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Pelican status.
		"""
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			1000, # Deploy time.
			915, # Hitpoints.
			101, # Damage.
			500, # First attack delay in ms.
			2000, # Attack delay in ms.
			500, # Attack range.
			1000, # Move Speed.
			MovementType.AIR, # Movement type.
			TargetType.ONLY_BH # Target types.
		)
		
		self.__explosion_damages = {
			"hero": 128,
			"troop": 256,
			"building": 384,
		}

class BuildingBomb(Building):
	"""
	The fourth initial card, a defensive bomb. Extra attributes in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Bomb status.
		"""
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			1000, # Deploy time.
			444, # Hitpoints.
			0, # Damage.
			1000, # First attack delay in ms.
			9999, # Attack delay in ms.
			2500, # Attack range.
			TargetType.ANY # Target types.
		)
		
		self.__explosion_damage = 256
		self.__explosion_radius = 2.5

class SpellWave(Building):
	"""
	The fifth initial card, a defensive giant wave. Extra attributes in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Wave status.
		"""
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			500, # Deploy time.
			88, # Damage.
			1000, # First attack delay in ms.
			900, # Attack delay in ms.
			50, # Effect area in tile.
			3000 # Time to destroy in ms.
		)
		
		self.__wave_distance = 500

class TroopBandit(Troop):
	"""
	The sixth initial card, a support bandit. No extras in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Bandit status.
		"""
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			1000, # Deploy time.
			474, # Hitpoints.
			83, # Damage.
			900, # First attack delay in ms.
			1000, # Attack delay in ms.
			6000, # Attack range.
			2000, # Move Speed.
			MovementType.GROUND, # Movement type.
			TargetType.ANY # Target types.
		)

class TroopLRobot(Troop):
	"""
	The seventh initial card, a near-combat robot. No extra attributes in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the L-Robot status.
		"""
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			1000, # Deploy time.
			803, # Hitpoints.
			205, # Damage.
			1000, # First attack delay in ms.
			1600, # Attack delay in ms.
			1000, # Attack range.
			2500, # Move Speed.
			MovementType.GROUND, # Movement type.
			TargetType.ONLY_GBH # Target types.
		)

class TroopBomber(Troop):
	"""
	The eighth initial card, two kamikazes. Extra attributes in his base class.
	"""
	
	def __init__(self, blue_team):
		"""
		Initialize the Rope Bomber status.
		"""
		
		super().__init__(
			blue_team, # Team flag.
			pygame.math.Vector2(0, 0), # Offset.
			1000, # Deploy time.
			173, # Hitpoints.
			113, # Damage.
			500, # First attack delay in ms.
			500, # Attack delay in ms.
			500, # Attack range.
			3000, # Move Speed.
			MovementType.AIR, # Movement type.
			TargetType.ONLY_BH # Target types.
		)


def initialize_units():
	register_troop("troop_gravedigger", TroopGravedigger)
	register_troop("troop_indian", TroopIndian)
	register_troop("troop_pelican", TroopPelican)
	register_building("building_bomb", BuildingBomb)
	register_spell("spell_wave", SpellWave)
	register_troop("troop_bandit", TroopBandit)
	register_spell("troop_l_robot", TroopLRobot)
	register_troop("troop_bomber", TroopBomber)

