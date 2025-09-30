# Module path: mcards.gameplay.factory.card_factory

from mcards.enums import *
from mcards.gdefs import *
from mcards.gvars import *

from mcards.gameplay.core.cards import Card

class Gravedigger(Card):
	"""
	Card name: Gravedigger;
	Card rarity: Common;
	Card type: Troop;
	
	Card description (EN-US): 'Never mess with her fellings, her big brother is literally the Reaper.'
	Card description (PT-BR): 'Nunca mexa com seus sentimentos, o irmão da Coveira é o próprio Ceifador.'
	Card description (ES-SP): 'Nunca juegues con sus sentimientos, su hermano mayor es literalmente la Parca.'
	Card description (DE-DE): 'Mach dich niemals mit ihren Gefühlen lustig, ihr großer Bruder ist buchstäblich der Sensenmann.'
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(self, CardNameVariations.GRAVEDIGGER, level, CardRarities.COMMON, 3, {"troop_gravedigger": 1}, blue_team)

class Indians(Card):
	"""
	Card name: Indians;
	Card rarity: Common;
	Card type: Troop;
	
	Card description (EN-US): 'Two indians that comes for the milk. There's some milk?'
	Card description (PT-BR): 'Uma dupla de indígenas que vieram pelo mingal. Tem mingal aí?'
	Card description (ES-SP): 'Dos indios que vienen por la leche. ¿Hay leche?'
	Card description (DE-DE): 'Zwei Indianer, die für die Milche kommen. Gibt es hier Milche?'
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(self, CardNameVariations.INDIANS, level, CardRarities.COMMON, 2, {"troop_indian": 2}, blue_team)

class Pelican(Card):
	"""
	Card name: Pelican;
	Card rarity: Rare;
	Card type: Troop;
	
	Card description (EN-US): 'A maniacal pelican with a bomb in its mouth. If you defeat him, the bomb explodes and don't even ask me how.'
	Card description (PT-BR): 'Um pelicano maníaco com uma bomba em sua boca. Se derrotar-lo, a bomba acende e nem me pergunte como.'
	Card description (ES-SP): 'Un pelícano maníaco con una bomba en la boca. Si lo derrotas, la bomba explota y ni me preguntes cómo.'
	Card description (DE-DE): 'Ein manischer Pelikan mit einer Bombe im Maul. Wenn du ihn besiegst, explodiert die Bombe und frag mich gar nicht wie.'
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(self, CardNameVariations.INDIANS, level, CardRarities.COMMON, 5, {"troop_pelican": 1}, blue_team)

def initialize_cards():
	register_card("card_gravedigger", Gravedigger)
	register_card("card_indians", Indians)
	register_card("card_pelican", Pelican)
