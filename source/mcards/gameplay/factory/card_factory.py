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
	
	Card description (EN-US): \"Never mess with her fellings, her big brother is literally the Reaper.\"
	Card description (PT-BR): \"Nunca mexa com seus sentimentos, o irmão da Coveira é o próprio Ceifador.\"
	Card description (ES-SP): \"Nunca juegues con sus sentimientos, su hermano mayor es literalmente la Parca.\"
	Card description (DE-DE): \"Mach dich niemals mit ihren Gefühlen lustig, ihr großer Bruder ist buchstäblich der Sensenmann.\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(CardNameVariations.GRAVEDIGGER, level, CardRarities.COMMON, 3, {"troop_gravedigger": 1}, blue_team)

class Indians(Card):
	"""
	Card name: Indians;
	Card rarity: Common;
	Card type: Troop;
	
	Card description (EN-US): \"Two indians that comes for the milk. There's some milk?\"
	Card description (PT-BR): \"Uma dupla de indígenas que vieram pelo mingal. Tem mingal aí?\"
	Card description (ES-SP): \"Dos indios que vienen por la leche. ¿Hay leche?\"
	Card description (DE-DE): \"Zwei Indianer, die für die Milche kommen. Gibt es hier Milche?\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(CardNameVariations.INDIANS, level, CardRarities.COMMON, 2, {"troop_indian": 2}, blue_team)

class Pelican(Card):
	"""
	Card name: Pelican;
	Card rarity: Rare;
	Card type: Troop;
	
	Card description (EN-US): \"A maniacal pelican with a bomb in its mouth. If you defeat him, the bomb explodes and don't even ask me how.\"
	Card description (PT-BR): \"Um pelicano maníaco com uma bomba em sua boca. Se derrotar-lo, a bomba acende e nem me pergunte como.\"
	Card description (ES-SP): \"Un pelícano maníaco con una bomba en la boca. Si lo derrotas, la bomba explota y ni me preguntes cómo.\"
	Card description (DE-DE): \"Ein manischer Pelikan mit einer Bombe im Maul. Wenn du ihn besiegst, explodiert die Bombe und frag mich gar nicht wie.\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(CardNameVariations.PELICAN, level, CardRarities.RARE, 5, {"troop_pelican": 1}, blue_team)

class Bomb(Card):
	"""
	Card name: Bomb;
	Card rarity: Common;
	Card type: Building;
	
	Card description (EN-US): \"Look the Bomb! Holy s... When destroyed, the Bomb deals explosion damage.\"
	Card description (PT-BR): \"Olha a Bomba! Caral... Quando destruída, a Bomba inflinge dano de explosão.\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initializes the Bomb status.
		"""
		
		super().__init__(CardNameVariations.BOMB, level, CardRarities.COMMON, 3, {"building_bomb": 1}, blue_team)

class Wave(Card):
	"""
	Card name: Wave;
	Card rarity: Rare;
	Card type: Spell;
	
	Card description (EN-US): \"Oh... literally a giant wave! The Wave deals single-attack damage per hitted unit.\"
	Card description (PT-BR): \"Oh literalmente uma onda gigante! A Onda inflinge dano de ataque único por cada inimigo.\"
	Card description (ES-SP): \"...\"
	Card description (DE-DE): \"...\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initializes the Bomb status.
		"""
		
		super().__init__(CardNameVariations.WAVE, level, CardRarities.RARE, 4, {"spell_waves": 1}, blue_team)

class Bandit(Card):
	"""
	Card name: Bandit;
	Card rarity: Common;
	Card type: Troop;
	
	Card description (EN-US): \"A normal bandit with a normal lever-action rifle... WAIT, WHAT!?\"
	Card description (PT-BR): \"Um bandido normal com um rifle-ação-de-alavanca normal... ESPERA, O QUÊ!?\"
	Card description (ES-SP): \"...\"
	Card description (DE-DE): \"...\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(CardNameVariations.BANDIT, level, CardRarities.COMMON, 4, {"troop_bandit": 1}, blue_team)

class LRobot(Card):
	"""
	Card name: L-Robot;
	Card rarity: Rare;
	Card type: Troop;
	
	Card description (EN-US): \"A anti-nazist combat robot abandoned since 1945 (after his mission).\"
	Card description (PT-BR): \"Um robô de combate anti-nazista abandonado desde 1945 (depois de cumprir a missão).\"
	Card description (ES-SP): \"...\"
	Card description (DE-DE): \"...\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(CardNameVariations.L_ROBOT, level, CardRarities.RARE, 4, {"troop_l_robot": 1}, blue_team)

class Bombers(Card):
	"""
	Card name: Bombers;
	Card rarity: RARE;
	Card type: Troop;
	
	Card description (EN-US): \"Two kamikazes with no intelect. Run for your life!\"
	Card description (PT-BR): \"Dois kamikazes sem intelecto. Corra pela sua vida!\"
	Card description (ES-SP): \"...\"
	Card description (DE-DE): \"...\"
	"""
	
	def __init__(self, level, blue_team):
		"""
		Initialize the card creation.
		"""
		
		super().__init__(CardNameVariations.BOMBERS, level, CardRarities.RARE, 2, {"troop_bomber": 2}, blue_team)

def initialize_cards():
	register_card("card_gravedigger", Gravedigger)
	register_card("card_indians", Indians)
	register_card("card_pelican", Pelican)
	register_card("card_bomb", Bomb)
	register_card("card_wave", Wave)
	register_card("card_bandit", Bandit)
	register_card("card_l_robot", LRobot)
	register_card("card_bombers", Bombers)
