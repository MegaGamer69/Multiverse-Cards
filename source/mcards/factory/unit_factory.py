"""
Caminho do módulo: mcards.factory.unit_factory
"""

from mcards.base.unit import Troop, Spell, Hero
from mcards.globals.gvars import *
from mcards.globals.gdefs import register_troop, register_spell

class HeroPirate(Hero):
	"""
	Uma classe que estende a base de herói e representa o Pirata.
	"""
	
	def __init__(self, blue_team: bool, level: int) -> None:
		"""
		Crie uma nova instância do herói.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(blue_team, 1440, 45, 1000, 1000, 3500)

class HeroMightyIndian(Hero):
	"""
	Uma classe que estende a base de herói e representa o Pajé Bombado.
	"""
	
	def __init__(self, blue_team: bool, level: int) -> None:
		"""
		Crie uma nova instância do herói.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(blue_team, 1500, 20, 300, 500, 1500)

class UnitGravedigger(Troop):
	"""
	Uma classe que estende a base de tropa e representa uma Coveirinha.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 100, 100)), blue_team,
						660, 79, 900, 1200, 2000, 750, TroopMoveType.GROUND, TroopTargetType.ONLY_GBH)

class UnitIndian(Troop):
	"""
	Uma classe que estende a base de tropa e representa um Indígena.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 75, 75)), blue_team,
						160, 43, 800, 900, 2500, 2500, TroopMoveType.GROUND, TroopTargetType.ANY)

class UnitPelican(Troop):
	"""
	Uma classe que estende a base de tropa e representa um Pelicano.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 100, 100)), blue_team,
						895, 100, 500, 1900, 1000, 500, TroopMoveType.AIR, TroopTargetType.ONLY_BH)
		
		self.__explosion_damages = {
			"troops": 100,
			"buildings": 175,
			"heroes": 150,
		}

class UnitSeagull(Troop):
	"""
	Uma classe que estende a base de tropa e representa uma Gaivota.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 60, 60)), blue_team,
						36, 36, 1000, 1100, 2000, 350, TroopMoveType.AIR, TroopTargetType.ANY)

class UnitBandit(Troop):
	"""
	Uma classe que estende a base de tropa e representa um Bandido.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 100, 100)), blue_team,
						420, 70, 800, 1000, 2000, 3500, TroopMoveType.GROUND, TroopTargetType.ANY)

class UnitLRobot(Troop):
	"""
	Uma classe que estende a base de tropa e representa um Robô-L.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 90, 90)), blue_team,
						782, 110, 1000, 1500, 2500, 500, TroopMoveType.GROUND, TroopTargetType.ONLY_GBH)

class UnitStorm(Spell):
	"""
	Uma classe que estende a base de feitiço e representa uma Baleia.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 60, 60)), blue_team,
						85, 750, SpellTargetType.ANY)

class UnitWhale(Spell):
	"""
	Uma classe que estende a base de feitiço e representa uma Baleia.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 90, 90)), blue_team,
						333, 750, SpellTargetType.ANY)

class UnitCrusher(Troop):
	"""
	Uma classe que estende a base de tropa e representa um Esmagador.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 100, 100)), blue_team,
						1288, 222, 1200, 1800, 1500, 500, TroopMoveType.GROUND, TroopTargetType.ONLY_GBH)
		
		self.__damage_bonus = {
			"troops": 1.0,
			"buildings": 1.25,
			"heroes": 0.9,
		}

class UnitHeroHunter(Troop):
	"""
	Uma classe que estende a base de tropa e representa uma Caçadora de Heróis.
	"""
	
	def __init__(self, blue_team: bool, level: int, index: int) -> None:
		"""
		Crie uma nova instância da tropa.
		
		:param blue_team: -> Determinador de time da instância.
		:param level: -> O nível atual da instância.
		:param index: -> O índice atual da instância.
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__([pygame.math.Vector2(0, 0)], index, pygame.Rect((0, 0, 80, 80)), blue_team,
						777, 80, 1000, 1300, 2500, 500, TroopMoveType.GROUND, TroopTargetType.ONLY_GBH)
		
		self.__damage_bonus_heroes = 1.7
		self.__dash_distance = {
			"max": 2500,
			"min": 1500,
		}
		self.__dash_damage = 200

def initialize_units() -> None:
	"""
	Registre todas as unidades do jogo.
	
	:return: -> Nenhum valor a ser retornado.
	"""
	
	register_hero("hero_pirate", HeroPirate)
	register_hero("hero_mighty_indian", HeroMightyIndian)
	register_troop("troop_gravedigger", UnitGravedigger)
	register_troop("troop_indian", UnitIndian)
	register_troop("troop_pelican", UnitPelican)
	register_troop("troop_seagull", UnitSeagull)
	register_troop("troop_bandit", UnitBandit)
	register_troop("troop_l_robot", UnitLRobot)
	register_spell("spell_storm", UnitStorm)
	register_spell("spell_whale", UnitWhale)
	register_troop("troop_crusher", UnitCrusher)
	register_troop("troop_hero_hunter", UnitHeroHunter)
