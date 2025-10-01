# Module path: mcards.enums

from enum import Enum

class CardNameVariations(Enum):
	GRAVEDIGGER = {
		"en_us": "Gravedigger",
		"pt_br": "Coveirinha",
		"es_sp": "Sepulturero",
		"de_de": "Totengräber",
	}
	INDIANS = {
		"en_us": "Indians",
		"pt_br": "Indígenas",
		"es_sp": "Indios",
		"de_de": "Indianer",
	}
	PELICAN = {
		"en_us": "Pelican",
		"pt_br": "Pelicano",
		"es_sp": "Pelícano",
		"de_de": "Pelikan",
	}
	BOMB = {
		"en_us": "Bomb",
		"pt_br": "Bomba",
		"es_sp": "Bomba",
		"de_de": "Bombe",
	}
	WAVE = {
		"en_us": "Wave",
		"pt_br": "Onda",
		"es_sp": "Ola",
		"de_de": "Welle",
	}
	BANDIT = {
		"en_us": "Bandit",
		"pt_br": "Bandido",
		"es_sp": "Bandido",
		"de_de": "Bandit",
	}
	L_ROBOT = {
		"en_us": "L-Robot",
		"pt_br": "L-Robot",
		"es_sp": "L-Robot",
		"de_de": "L-Robot",
	}
	BOMBERS = {
		"en_us": "Bombers",
		"pt_br": "Bombas humana",
		"es_sp": "Bombarderos",
		"de_de": "Bombenschützen",
	}

class CardType(Enum):
	TROOP = "Troop"
	SPELL = "Spell"
	BUILDING = "Building"

class CardRarities(Enum):
	COMMON = "Common"
	RARE = "Rare"
	EPIC = "Epic"

class MovementType(Enum):
	GROUND = "Ground"
	AIR = "Air"

class TargetType(Enum):
	ONLY_GBH = "Only ground, building and heroes"
	ONLY_ABH = "Only air, building and heroes"
	ANY = "Any"
	ONLY_BH = "Only building and heroes"
