"""
Caminho do módulo: mcards.factory.unit_factory
"""

from mcards.base.unit import Troop, Spell
from mcards.globals.gvars import *
from mcards.globals.gdefs import register_troop

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
						160, 43, 800, 900, 2500, 3500, TroopMoveType.GROUND, TroopTargetType.ANY)

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
						885, 75, 800, 1800, 1000, 500, TroopMoveType.AIR, TroopTargetType.ONLY_BH)
		
		self.__explosion_damages = {
			"troops": 75,
			"buildings": 150,
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
						530, 77, 800, 1000, 2000, 5000, TroopMoveType.GROUND, TroopTargetType.ANY)

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
						782, 98, 1000, 1600, 2500, 500, TroopMoveType.GROUND, TroopTargetType.ONLY_GBH)

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
						333, 750, SpellTargetTypes.ANY)

def initialize_units() -> None:
	"""
	Registre todas as unidades do jogo.
	
	:return: -> Nenhum valor a ser retornado.
	"""
	
	register_troop("troop_gravedigger", UnitGravedigger)
	register_troop("troop_indian", UnitIndian)
	register_troop("troop_pelican", UnitPelican)
	register_troop("troop_seagull", UnitSeagull)
	register_troop("troop_bandit", UnitBandit)
	register_troop("troop_l_robot", UnitLRobot)
	register_troop("spell_storm", UnitStorm)
	register_troop("spell_whale", UnitWhale)
