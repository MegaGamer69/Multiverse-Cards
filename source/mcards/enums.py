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
