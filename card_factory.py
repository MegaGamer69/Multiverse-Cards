from global_variables import *

from card import *
from unit import *

TYPES = ["Troop", "Building", "Spell"]
RARITIES = ["Common", "Rare", "Epic", "Exclusive"]
TARGET_TYPES = ["Only Ground, Building and Heroes", "Only Air and Heroes", "Any", "Only Buildings and Heroes"]

## Heroes ##

# From the Pirate Epoch.

class HeroPirate(Hero):
	def __init__(self, blue_side):
		super().__init__(1800, 73, 1.0, 0.5, 7.5, blue_side)

class HeroMightyIndian(Hero):
	def __init__(self, blue_side):
		super().__init__(1987, 25, 0.4, 0.3, 1.0, blue_side)

# From the Feudal Japan.

class HeroSamurai(Hero):
	def __init__(self, blue_side):
		super().__init__(1886, 105, 1.3, 1.0, 1.5, blue_side)

# From the House Nightmares.

class HeroAlchemist(Hero):
	def __init__(self, blue_side):
		super().__init__(1680, 66, 0.8, 0.6, 7.0, blue_side)

# From the Cambrian Time.

class HeroSurvivor(Hero):
	def __init__(self, blue_side):
		super().__init__(1790, 56, 0.7, 0.5, 2.0, blue_side)

## Cards ##

# From the Pirate Epoch.

class CardGravedigger(Card): # Do not mess with she, her big brother is the literal reaper.
	def __init__(self, blue_side):
		super().__init__("Gravedigger", 3, "gravedigger", [TroopGravedigger], TYPES[0], RARITIES[0], blue_side)

class CardIndians(Card): # Two indians that comes for the milk, do you have some milk?
	def __init__(self, blue_side):
		super().__init__("Indians", 3, "indians", [TroopIndians, TroopIndians], TYPES[0], RARITIES[0], blue_side)

class CardPelican(Card): # A maniac pelican with a big bomb in his mounth, caution!
	def __init__(self, blue_side):
		super().__init__("Pelican", 5, "pelican", [TroopPelican], TYPES[0], RARITIES[1], blue_side)

class CardRopeBombers(Card): # Two kamikazes with no intelect, but have a life, do not mess with them.
	def __init__(self, blue_side):
		super().__init__("Rope Bombers", 3, "rope_bombers", [TroopRopeBombers, TroopRopeBombers], TYPES[0], RARITIES[2], blue_side)

class CardLRobot(Card): # A anti-nazist combat robot that was abandoned since 1945, poor robot.
	def __init__(self, blue_side):
		super().__init__("L-Robot", 4, "l_robot", [TroopLRobot], TYPES[0], RARITIES[1], blue_side)

class CardBomb(Card): # LOOK THE BOMB-
	def __init__(self, blue_side):
		super().__init__("Bomb", 3, "bomb", [BuildingBomb], TYPES[1], RARITIES[1], blue_side)

class CardTsunami(Card): # No, that is not a Japan reference... IT IS SERIOUS!
	def __init__(self, blue_side):
		super().__init__("Tsunami", 4, "tsunami", [SpellTsunami], TYPES[2], RARITIES[2], blue_side)

class CardBandit(Card): # A normal bandit with a normal lever-action pistol... WAIT, WHAT!?
	def __init__(self, blue_side):
		super().__init__("Bandit", 4, "bandit", [TroopBandit], TYPES[0], RARITIES[1], blue_side)

class CardWhale(Card): # Oh... a giant cachalot whale... and mysteriously flying at every tuesday.
	def __init__(self, blue_side):
		super().__init__("Whale", 5, "whale", [SpellWhale], TYPES[2], RARITIES[1], blue_side)

class CardSeagulls(Card): # Stupid bird... STOP EATING MY SANDWISH!
	def __init__(self, blue_side):
		super().__init__("Seagulls", 2, "seagulls", [TroopSeagulls, TroopSeagulls, TroopSeagulls], TYPES[0], RARITIES[0], blue_side)

# From the Feudal Japan.

class CardCrusher(Card): # HOLY MOLY, IS THAT A WARRIOR USING A YOROI AND A GIANT SLEDGEHAMMER!?
	def __init__(self, blue_side):
		super().__init__("Crusher", 7, "crusher", [TroopCrusher], TYPES[0], RARITIES[2], blue_side)

class CardHeroHunter(Card): # That is not a normal female warrior... THAT IS A HERO HUNTER!
	def __init__(self, blue_side):
		super().__init__("Hero Hunter", 5, "hero_hunter", [TroopHeroHunter], TYPES[0], RARITIES[1], blue_side)

# From the House Nightmares.

class CardHallucination(Card): # OH MY GOD, IS THAT A RE8 BENEVIENTO HOUSE REFERENCE!?
	def __init__(self, blue_side):
		super().__init__("Hallucination", 5, "hallucination", [TroopHallucination], TYPES[0], RARITIES[2], blue_side)

class CardReaper(Card): # Gravedigger is the little sister, Reaper is the big brother.
	def __init__(self, blue_side):
		super().__init__("Reaper", 4, "reaper", [TroopReaper], TYPES[0], RARITIES[1], blue_side)

class CardElectricGenerator(Card): # A normal electric generator... or no.
	def __init__(self, blue_side):
		super().__init__("Electric Generator", 6, "electric_generator", [BuildingElectricGenerator], TYPES[1], RARITIES[1], blue_side)

class CardScaryFog(Card): # Whooooooooh! Look the power bill!
	def __init__(self, blue_side):
		super().__init__("Scary Fog", 4, "scary_fog", [SpellScaryFog], TYPES[2], RARITIES[2], blue_side)

# From the Cambrian Time.

class CardStrangeWorms(Card): # Using a DNA of Hallucigenia to generate a even more strange worms... cool!
	def __init__(self, blue_side):
		super().__init__("Strange Worms", 5, "strange_worms", [TroopStrangeWorms, TroopStrangeWorms, TroopStrangeWorms, TroopStrangeWorms], TYPES[0], RARITIES[0], blue_side)

class CardGiantTheropod(Card): # No, that is not a Tyrannosaurus rex.
	def __init__(self, blue_side):
		super().__init__("Giant Theropod", 8, "giant_theropod", [TroopGiantTheropod], TYPES[0], RARITIES[2], blue_side)

# From the Troubles in France.

class CardGunDealer(Card): # Look at this cool autistic dude! This boy is literally the Napoleao's best friend (he also killed the "ugly mustachioed" when heared a insult).
	def __init__(self, blue_side):
		super().__init__("Gun Dealer", 3, "gun_dealer", [TroopGunDealer], TYPES[0], RARITIES[1], blue_side)

# From the Second World War Events.

class CardHRobot(Card): # The ultimate anti-nazist combat robot, created by the Brazilians and now can play funk... unfortunately.
	def __init__(self, blue_side):
		super().__init__("H-Robot", 7, "h_robot", [TroopHRobot], TYPES[0], RARITIES[2], blue_side)

class CardNun(Card): # A beautyful nun with more intelect than Rope Bombers!
	def __init__(self, blue_side):
		super().__init__("Nun", 4, "nun", [TroopNun], TYPES[0], RARITIES[1], blue_side)

class CardGermanBunker(Card): # When the Nazist Empire downs, the German Bunker lets some space to the survivors. Let's pray respect for every 6 million victims? 
	def __init__(self, blue_side):
		super().__init__("German Bunker", 5, "german_bunker", [BuildingGermanBunker], TYPES[1], RARITIES[1], blue_side)

# From the Dark Plague Era.

class CardPlagueKiller(Card): # A literal serial killer using the plague medic clothes.
	def __init__(self, blue_side):
		super().__init__("Plague Killer", 4, "plague_killer", [TroopPlagueKiller], TYPES[0], RARITIES[2], blue_side)

class CardMosquitoes(Card): # The most dangerful monster at almost the entire world.
	def __init__(self, blue_side):
		super().__init__("Mosquitoes", 1, "mosquitoes", [TroopMosquitoes], TYPES[0], RARITIES[0], blue_side)

# From the Farroupilha War.

class CardPampaHorseman(Card): # Do not underrate him, you do not want to know the real power of his horse.
	def __init__(self, blue_side):
		super().__init__("Pampa Horseman", 4, "pampa_horseman", [TroopPampaHorseman], TYPES[0], RARITIES[1], blue_side)

## Troops ##

# From the Pirate Epoch.

class TroopGravedigger(Troop):
	def __init__(self, blue_side):
		super().__init__(650, 80, 1.2, 1.0, 2.0, 8.0, 1.5, False, TARGET_TYPES[0], blue_side)

class TroopIndians(Troop):
	def __init__(self, blue_side):
		super().__init__(200, 55, 1.0, 0.9, 2.5, 7.5, 5.0, False, TARGET_TYPES[2], blue_side)

class TroopPelican(Troop):
	def __init__(self, blue_side):
		super().__init__(800, 100, 2.0, 0.5, 1.5, 5.5, 0.5, True, TARGET_TYPES[3], blue_side)

		self.__explosion_damage_heroes = 96
		self.__explosion_damage_troops = 80
		self.__explosion_damage_builds = 128

class TroopRopeBombers(Troop):
	def __init__(self, blue_side):
		super().__init__(222, 0, 0.5, 0.5, 3.0, 6.5, 0.5, True, TARGET_TYPES[3], blue_side)
		
		self.__exploded = False
		self.__explosion_radius = 2.5
		self.__explosion_damage_heroes = 100
		self.__explosion_damage_troops = 90
		self.__explosion_damage_builds = 150
	
	def update(self, delta_time, all_enemies):
		if self._state == "Dead":
			return
		
		self._current_target = all_enemies[0]
		
		if self._current_target:
			distance = pygame.math.Vector2.distance_to(self._position, self._current_target.get_position())
			
			if distance <= self._attack_range * GRID_SIZE:
				if not self.__exploded:
					self._kamikaze(all_enemies)
			else:
				self._state = "Moving"
		
		if self._state == "Moving" and self._current_target and not self.__exploded:
			self._position = pygame.math.Vector2.move_towards(
				self._position,
				self._current_target.get_position(),
				self._tiles_per_second * delta_time * GRID_SIZE
			)
	
	def _kamikaze(self, all_enemies):
		self.__exploded = True
		self._state = "Attacking"
		
		enemies_in_radius = []
		
		for enemy in all_enemies:
			distance = pygame.math.Vector2.distance_to(self._position, enemy.get_position())
			
			if distance <= self.__explosion_radius * GRID_SIZE:
				enemies_in_radius.append(enemy)
		
		for enemy in enemies_in_radius:
			if isinstance(enemy, Hero):
				enemy.apply_damage(self.__explosion_damage_heroes)
			elif isinstance(enemy, Troop):
				enemy.apply_damage(self.__explosion_damage_troops)
			elif isinstance(enemy, Building):
				enemy.apply_damage(self.__explosion_damage_builds)
		
		print("The troop exploded!")
		
		self._hitpoints = 0
		self._state = "Dead"
		
		self._on_destroy()

class TroopLRobot(Troop):
	def __init__(self, blue_side):
		super().__init__(814, 128, 1.5, 1.1, 2.5, 6.0, 1.0, False, TARGET_TYPES[0], blue_side)

class TroopBandit(Troop):
	def __init__(self, blue_side):
		super().__init__(500, 89, 1.0, 1.2, 2.0, 8.0, 6.5, False, TARGET_TYPES[2], blue_side)

class TroopSeagulls(Troop):
	def __init__(self, blue_side):
		super().__init__(82, 41, 0.8, 0.9, 2.5, 4.5, 1.0, True, TARGET_TYPES[2], blue_side)

# From the Feudal Japan.

class TroopCrusher(Troop):
	def __init__(self, blue_side):
		super().__init__(1055, 128, 1.7, 1.3, 2.0, 7.0, 2.5, False, TARGET_TYPES[0], blue_side)

class TroopHeroHunter(Troop):
	def __init__(self, blue_side):
		super().__init__(766, 90, 1.3, 1.0, 2.0, 6.0, 1.5, False, TARGET_TYPES[0], blue_side)
		
		self.__heroes_damage = 100
		self.__dash_max_distance = 5.5
		self.__dash_min_distance = 3.5

# From the House Nightmares.

class TroopHallucination(Troop):
	def __init__(self, blue_side):
		super().__init__(888, 88, 1.3, 1.4, 2.0, 7.0, 1.0, False, TARGET_TYPES[0], blue_side)

		self.__clone_health = 444
		self.__clone_damage = 44

class TroopReaper(Troop):
	def __init__(self, blue_side):
		super().__init__(798, 95, 1.5, 1.2, 2.0, 5.5, 3.5, False, TARGET_TYPES[2], blue_side)

		self.__max_souls_to_collect = 4
		self.__explosion_damage = 80
		self.__damage_buff_per_soul = 7

# From the Cambrian Time.

class TroopStrangeWorms(Troop):
	def __init__(self, blue_side):
		super().__init__(655, 32, 1.3, 1.0, 1.0, 8.0, 4.0, False, TARGET_TYPES[0], blue_side)

class TroopGiantTheropod(Troop):
	def __init__(self, blue_side):
		super().__init__(1540, 120, 1.9, 1.7, 1.0, 7.0, 0.5, False, TARGET_TYPES[0], blue_side)

# From the Troubles in france.

class TroopGunDealer(Troop):
	def __init__(self, blue_side):
		super().__init__(400, 77, 1.0, 0.8, 2.0, 7.5, 5.5, False, TARGET_TYPES[2], blue_side)

# From the Second World War Events.

class TroopHRobot(Troop):
	def __init__(self, blue_side):
		super().__init__(1300, 155, 1.8, 1.6, 1.0, 8.0, 1.0, False, TARGET_TYPES[3], blue_side)

class TroopAngel(Troop):
	def __init__(self, blue_side):
		super().__init__(412, 64, 1.4, 1.3, 2.5, 8.0, 1.0, False, TARGET_TYPES[2], blue_side)
		
		self.__desapear_time_when_nun_dies = 2.5

class TroopNun(Troop):
	def __init__(self, blue_side):
		super().__init__(777, 70, 1.2, 0.7, 2.0, 8.0, 2.0, False, TARGET_TYPES[0], blue_side)
		
		self.__knockback_range = 2.5
		self.__needed_attacks_to_knockback = 4
		self.__angels_spawn_amount = 2
		self.__angels_spawn_time = 10.0
		self.__spawn_angels_times_limit = 5
		self.__angel_troop_reference = TroopAngel

# From the Dark Plague Era.

class TroopPlagueKiller(Troop):
	def __init__(self, blue_side):
		super().__init__(665, 70, 1.1, 1.0, 2.0, 6.5, 1.0, False, TARGET_TYPES[0], blue_side)

		self.__dash_damage = 97
		self.__dash_max_distance = 5.5
		self.__dash_min_distance = 3.0
		self.__invisibility_time = 7.5

class TroopMosquitoes(Troop):
	def __init__(self, blue_side):
		super().__init__(20, 20, 1.0, 1.0, 2.0, 7.5, 0.5, True, TARGET_TYPES[2], blue_side)

# From the Farroupilha War.

class TroopPampaHorseman(Troop):
	def __init__(self, blue_side):
		super().__init__(850, 95, 1.4, 1.0, 2.5, 8.5, 2.0, False, TARGET_TYPES[0], blue_side)

## Buildings ##

# From the Pirate Epoch.

class BuildingBomb(Building):
	def __init__(self):
		super().__init__(555, 0, 0.0, 0.0, 3.0, 10.0, TARGET_TYPES[2])

		self.__explosion_damage = 128

# From the House Nightmares.

class BuildingElectricGenerator(Building):
	def __init__(self):
		super().__init__(975, 0, 0.0, 0.0, 50.0, TARGET_TYPES[2])

		self.__generation_speed = 10.0
		self.__extra_energy_on_generate = 1
		self.__extra_energy_on_destroyed = 1

# From the Second World War Events.

class BuildingGermanBunker(Building):
	def __init__(self):
		super().__init__(867, 0, 0.0, 0.0, 0.0, 30.0, TARGET_TYPES[2])

## Spells ##

# From the Pirate Epoch.

class SpellTsunami(Spell):
	def __init__(self):
		super().__init__(29, 15, 5, 2.5, False)

class SpellWhale(Spell):
	def __init__(self):
		super().__init__(55, 30, 1, 2, True)

# from the House Nightmares.

class SpellScaryFog(Spell):
	def __init__(self):
		super().__init__(28, 30, 7, 3.5, True)

def get_all_cards():
	return [
		CardGravedigger,
		CardIndians,
		CardPelican,
		CardRopeBombers,
		CardLRobot,
		CardBomb,
		CardTsunami,
		CardBandit,
		CardWhale,
		CardSeagulls,
		CardCrusher,
		CardHeroHunter,
		CardHallucination,
		CardReaper,
		CardElectricGenerator,
		CardScaryFog,
		CardStrangeWorms,
		CardGunDealer,
		CardGiantTheropod,
		CardHRobot,
		CardPlagueKiller,
		CardPampaHorseman,
		CardNun,
	]
