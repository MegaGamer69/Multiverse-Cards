"""
Caminho do módulo: mcards.factory.card_factory
"""

from mcards.base.card import Card
from mcards.globals.gvars import *
from mcards.globals.gdefs import register_troop

# Cartas instânciadas.

class CardGravedigger(Card):
	"""
	Uma classe que estende a base de carta e representa a Coveirinha.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.GRAVEDIGGER, 3, CardDescriptions.GRAVEDIGGER, {"troop_gravedigger": 1})

class CardIndians(Card):
	"""
	Uma classe que estende a base de carta e representa os Indígenas.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.INDIANS, 3, CardDescriptions.INDIANS, {"troop_indian": 2})

class CardPelican(Card):
	"""
	Uma classe que estende a base de carta e representa o Pelicano.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.PELICAN, 5, CardDescriptions.PELICAN, {"troop_pelican": 1})

class CardSeagulls(Card):
	"""
	Uma classe que estende a base de carta e representa o Gaivotas.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.SEAGULLS, 2, CardDescriptions.SEAGULLS, {"troop_seagull": 3})

class CardBandit(Card):
	"""
	Uma classe que estende a base de carta e representa o Bandido.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.BANDIT, 4, CardDescriptions.BANDIT, {"troop_bandit": 1})

class CardLRobot(Card):
	"""
	Uma classe que estende a base de carta e representa o Robô-L.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.L_ROBOT, 4, CardDescriptions.L_ROBOT, {"troop_l_robot": 1})

class CardStorm(Card):
	"""
	Uma classe que estende a base de carta e representa a Tempestade.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.STORM, 2, CardDescriptions.STORM, {"spell_storm": 1})

class CardWhale(Card):
	"""
	Uma classe que estende a base de carta e representa a Baleia.
	"""
	
	def __init__(self) -> None:
		"""
		Crie uma nova instância da carta.
		
		:return: -> Nenhum valor a ser retornado.
		"""
		
		super().__init__(CardNames.WHALE, 4, CardDescriptions.WHALE, {"spell_whale": 1})

def initialize_cards() -> None:
	"""
	Inicialize as cartas para registrar-las.
	"""
	
	register_card("gravedigger", CardGravedigger)
	register_card("indians", CardIndians)
	register_card("pelican", CardPelican)
	register_card("seagulls", CardSeagulls)
	register_card("bandit", CardBandit)
	register_card("l_robot", CardLRobot)
	register_card("storm", CardStorm)
	register_card("whale", CardWhale)
