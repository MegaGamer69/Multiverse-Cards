from enum import Enum

class CardNameVariations(Enum):
	GRAVEDIGGER = {
		"en_us": "Gravedigger",
		"pt_br": "Coveirinha",
		"es_sp": "Sepulturero",
		"de_de": "Totengräber",
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
	ONLY_GROUND_BUILDING_AND_HEROES = "Only ground, building and heroes"
	ONLY_AIR_BUILDING_AND_HEROES = "Only air, building and heroes"
	ANY = "Any"
	ONLY_BUILDING_AND_HEROES = "Only building and heroes"
