from enum import Enum

class TargetTypes(Enum):
	ONLY_GROUND_BUILDING_AND_HEROES = "Only ground, building and heroes"
	ONLY_AIR_BUILDING_AND_HEROES = "Only air, building and heroes"
	ANY = "Any"
	ONLY_BUILDING_AND_HEROES = "Only building and heroes"
