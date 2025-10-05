"""
Caminho do módulo: mcards.globals
"""

from enum import Enum

class CardNames(Enum):
	"""
	Contém os nomes traduzidos para diversos idiomas.
	"""
	
	GRAVEDIGGER = {
		"en_us": "Gravedigger",
		"pt_br": "Coveirinha",
	}
	
	INDIANS = {
		"en_us": "Indians",
		"pt_br": "Indígenas",
	}
	
	PELICAN = {
		"en_us": "Pelican",
		"pt_br": "Pelicano",
	}
	
	SEAGULLS = {
		"en_us": "Seagulls",
		"pt_br": "Gaivotas",
	}
	
	BANDIT = {
		"en_us": "Bandit",
		"pt_br": "Bandido",
	}
	
	L_ROBOT = {
		"en_us": "L-Robot",
		"pt_br": "Robô-L",
	}

class CardDescriptions(Enum):
	"""
	Contém os nomes traduzidos para diversos idiomas.
	"""
	
	GRAVEDIGGER = {
		"en_us": "A cute and young ingenuous girl... working as gravedigger.",
		"pt_br": "Uma garota jóvem ingênua e fofa... trabalhando de coveira.",
	}
	
	INDIANS = {
		"en_us": "Two indians that comes for the milk. Do you have some of milk?",
		"pt_br": "Dois indígenas que vieram pelo mingal. Tem um pouco de mingal aí?",
	}
	
	PELICAN = {
		"en_us": "A big maniac bird with a bomb in his mouth. When defeated, the bomb falls and explodes. Yay!",
		"pt_br": "Um grande pássaro maníaco com uma bomba na boca. Ao ser derrotado, a bomba cai e ascende. Eba!",
	}
	
	SEAGULLS = {
		"en_us": "Stupid birds... STOP EATING MY SANDWISH!",
		"pt_br": "Pássaros estúpidos... PAREM DE COMER MEU SANDUÍCHE!",
	}
	
	BANDIT = {
		"en_us": "A normal bandit with a normal lever-action pistol... WAIT, WHAT!?",
		"pt_br": "Um bandido normal com uma pistola de alavanca normal... ESPERA, O QUÊ!?",
	}
	
	L_ROBOT = {
		"en_us": "A anti-nazist combat robot, created by the United States. But got abandoned as trash.\n\nThere's some times that I fell bad.",
		"pt_br": "Um robô de combate anti-nazista, criado pelos Estados Unidos. Porém foi abandonado como lixo.\n\nÀs vezes eu tenho empatia.",
	}
	
	WHALE = {
		"en_us": "The giant Livyatan... mysteriously flying every Tuesday! When the Whale falls, causes a huge area-damage and go away.",
		"pt_br": "A imponente Livyatan... misteriosamente voando toda Terça-Feira! Qundo a Baleia cai, causa um imenso dano em área e voa para longe.",
	}

class TroopTargetType(Enum):
	"""
	Contém todos os tipos de alvo para cada tropa.
	"""
	
	ONLY_GBH = {
		"en_us": "Only ground, building and heroes",
		"pt_br": "Apenas terrestre, construções e heróis",
	}
	
	ONLY_BH = {
		"en_us": "Only building and heroes",
		"pt_br": "Apenas construções e heróis",
	}
	
	ANY = {
		"en_us": "Any one",
		"pt_br": "Qualquer um",
	}

class BuildingTargetType(Enum):
	"""
	Contém todos os tipos de alvo para cada construção.
	"""
	
	ONLY_GROUND = {
		"en_us": "Only ground",
		"pt_br": "Apenas terrestre",
	}
	
	ANY = {
		"en_us": "Ground and air",
		"pt_br": "Terrestre e aéreo",
	}

class SpellTargetType(Enum):
	"""
	Contém todos os tipos de alvo para cada feitiço.
	"""
	
	ONLY_GROUND = {
		"en_us": "Only ground",
		"pt_br": "Apenas terrestre",
	}
	
	ONLY_AIR = {
		"en_us": "Only air",
		"pt_br": "Apenas aéreo",
	}
	
	ANY = {
		"en_us": "Ground and air",
		"pt_br": "Terrestre e aéreo",
	}

class TroopMoveType(Enum):
	"""
	Contém os tipos de movimentação da tropa.
	"""
	
	AIR = {
		"en_us": "Air",
		"pt_br": "Aéreo",
	}
	
	GROUND = {
		"en_us": "Ground",
		"pt_br": "Terrestre",
	}

WINDOW_SIZE = (720, 1280)
TILE_SIZE = 500
