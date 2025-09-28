<<<<<<< HEAD
# Module path: mcards.gameplay.factory.card_factory

from mcards.engine import engine
from mcards.enums import *

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
		
		super().__init__(self, CardNameVariations.GRAVEDIGGER, level, CardRarities.COMMON,
						3, {"troop_gravedigger": 1}, blue_team)

engine.register_card("gravedigger")
=======
# Module path: mcards.gameplay.factory.card_factory

from mcards.engine import engine
from mcards.enums import *

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
		
		super().__init__(self, CardNameVariations.GRAVEDIGGER, level, CardRarities.COMMON,
						3, {"troop_gravedigger": 1}, blue_team)

engine.register_card("gravedigger")
>>>>>>> refs/remotes/origin/main
