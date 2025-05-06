#define CARD_MAX_LEVEL 9      // Tropas, construções e feitiços são cartas
#define HERO_MAX_LEVEL 9      // HERÓIS NÃO SÃO CARTAS!

#define MAX_CARDS_PER_DECK 8  // Basicamente um Clash Royale haha!
#define MAX_HEROES_PER_DECK 1 // Balanceamento, já que teria que defender dois heróis ao mesmo tempo

#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>

#include <SFML/Window.h>
#include <SFML/Graphics.h>
#include <SFML/System.h>

// Tipos de ataques

typedef enum {
	ONLY_GROUND,           // Ataca apenas unidades terrestres e ignora aéreas
	ONLY_AIR,              // Ataca apenas unidades aéreas e ignora terrestres
	ONLY_HERO_OR_BUILDING, // Ataca apenas construções ou heróis e ignora o resto
	GROUND_AND_AIR,        // Ataca tanto terrestres quanto aéreas
} mc_AttackType;

// Arcos da história

typedef enum {
	PIRATE_EPOCH,
	FEUDAL_JAPAN,
	DARK_PLAGUE_ERA,
	TROUBLES_IN_FRANCE,
	POST_TYRANNY_WORLD,
	GAUCHO_HISTORY,
	DINOSAURS_EPOCH,
} mc_LoreArch;

// Herói

typedef struct {
	// Dados de atributos
	
	char          i_Name[128];
	unsigned int  i_Level;
	int           i_BaseHealth;
	int           i_BaseDamage;
	int           i_Health;
	int           i_Damage;
	float         i_ARange;
	float         i_ATimer;
	mc_LoreArch   i_LArch;
} mc_Hero;

// Tropa

typedef struct {
	// Dados de atributos
	
	char          i_Name[128];
	unsigned int  i_Level;
	int           i_CDCost;
	int           i_BaseHealth;
	int           i_BaseDamage;
	int           i_Health;
	int           i_Damage;
	mc_AttackType i_AtType;
	float         i_ARange;
	float         i_ATimer;
	float         i_MSpeed;
	mc_LoreArch   i_LArch;
} mc_Troop;

// Construção

typedef struct {
	// Dados de atributos
	
	char          i_Name[128];
	unsigned int  i_Level;
	int           i_CDCost;
	int           i_BaseHealth;
	int           i_BaseDamage;
	int           i_Health;
	int           i_Damage;
	mc_AttackType i_AtType;
	float         i_ARange;
	float         i_ATimer;
	mc_LoreArch   i_LArch;
} mc_Build;

// Feitiço

typedef struct {
	// Dados de atributos
	
	char          i_Name[128];
	unsigned int  i_Level;
	int           i_CDCost;
	int           i_BaseDamage;
	int           i_Damage;
	mc_AttackType i_AtType;
	float         i_ARange;
	float         i_ATimer;
	float         i_Duration;
	mc_LoreArch   i_LArch;
} mc_Spell;

typedef enum {
	CARD_TROOP,
	CARD_SPELL,
	CARD_BUILD,
} mc_CardType;

typedef struct {
	mc_CardType i_Type;
	
	union {
		mc_Troop i_Troop;
		mc_Spell i_Spell;
		mc_Build i_Build;
	};
} mc_Card;

mc_Hero mc_CreateHero(const char* name,
                      unsigned int health,
                      unsigned int damage,
                      float range,
                      float attackTime,
                      mc_LoreArch lArch) {
	mc_Hero instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_Level = 1;
	instance.i_BaseHealth = health;
	instance.i_BaseDamage = damage;
	instance.i_Health = health;
	instance.i_Damage = damage;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	instance.i_LArch = lArch;
	
	return instance;
}

mc_Troop mc_CreateTroop(const char*   name,
					    unsigned int  cost,
					    unsigned int  health,
					    unsigned int  damage,
					    mc_AttackType atType,
					    float         range,
					    float         attackTime,
					    float         movSpeed,
					    mc_LoreArch   lArch) {
	mc_Troop instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_Level = 1;
	instance.i_CDCost = cost;
	instance.i_BaseHealth = health;
	instance.i_BaseDamage = damage;
	instance.i_Health = health;
	instance.i_Damage = damage;
	instance.i_AtType = atType;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	instance.i_MSpeed = movSpeed;
	instance.i_LArch = lArch;
	
	return instance;
}

mc_Build mc_CreateBuild(const char*   name,
					    unsigned int  cost,
					    unsigned int  health,
  					    unsigned int  damage,
  					    mc_AttackType atType,
  					    float         range,
            			float         attackTime,
            			mc_LoreArch   lArch) {
	mc_Build instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_Level = 1;
	instance.i_CDCost = cost;
	instance.i_BaseHealth = health;
	instance.i_BaseDamage = damage;
	instance.i_Health = health;
	instance.i_Damage = damage;
	instance.i_AtType = atType;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	instance.i_LArch = lArch;
	
	return instance;
}

mc_Spell mc_CreateSpell(const char*   name,
					    unsigned int  cost,
  					    unsigned int  damage,
  					    mc_AttackType atType,
  					    float         range,
            			float         attackTime,
            			float         duration,
            			mc_LoreArch   lArch) {
	mc_Spell instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_Level = 1;
	instance.i_CDCost = cost;
	instance.i_BaseDamage = damage;
	instance.i_Damage = damage;
	instance.i_AtType = atType;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	instance.i_Duration = duration;
	instance.i_LArch = lArch;
	
	return instance;
}

void mc_UpgradeCard(const char* name,
                    unsigned int* level,
                    int* baseHealth,
                    int* baseDamage,
                    int* health,
                    int* damage) {
	if(*level >= CARD_MAX_LEVEL) {
		return;
	}
	
	(*level)++;
	
	*health = (int)((*baseHealth) * (1.0f + 0.55f * (*level - 1)));
	*damage = (int)((*baseDamage) * (1.0f + 0.5f  * (*level - 1)));
}

void mc_UpgradeHero(const char*   name,
                    unsigned int* level,
                    int*          baseHealth,
                    int*          baseDamage,
                    int*          health,
                    int*          damage) {
	if(*level >= HERO_MAX_LEVEL) {
		return;
	}
	
	(*level)++;
	
	*health = (int)((*baseHealth) * (1.0f + 0.5f * (*level - 1)));
	*damage = (int)((*baseDamage) * (1.0f + 0.5f * (*level - 1)));
}

// Campos globais

sfRenderWindow* mc_GameWindow;
sfFont* mc_GameTextualFont;

// Baralho do jogador

typedef struct {
	mc_Hero  d_SelectedHero;
	mc_Card  d_DeckCards[MAX_CARDS_PER_DECK];
	size_t   d_CardCount;
} mc_PlayerDeck;

/**
 * Cria um deck para o jogador com um herói e oito cartas exatamente
 */
mc_PlayerDeck mc_CreatePlayerDeck(mc_Hero hero,
                                  mc_Card cards[],
                                  size_t  cardCount) {
	mc_PlayerDeck deck;
	
	assert(cardCount <= MAX_CARDS_PER_DECK);
	memcpy(deck.d_DeckCards, cards, sizeof(mc_Card) * cardCount);
	
	deck.d_CardCount = cardCount;
	
	memset(&deck, 0, sizeof(deck));
	
	deck.d_SelectedHero = hero;
	
	return deck;
}

/**
 * Inicializa o estado de jogo (lógicamente)
 */
void mc_Initialize() {
	mc_Hero heroes[] = {
		mc_CreateHero("Pirata",          1900, 60, 5.5f, 1.4f, PIRATE_EPOCH   ),
		mc_CreateHero("Índio Bombado",   1960, 20, 3.5f, 0.5f, PIRATE_EPOCH   ),
		mc_CreateHero("Shugun Renegado", 2000, 70, 4.0f, 1.8f, FEUDAL_JAPAN   ),
		mc_CreateHero("Alquimista",      1890, 32, 7.0f, 1.0f, DARK_PLAGUE_ERA),
		mc_CreateHero("Mateador",        1790, 44, 5.5f, 1.1f, GAUCHO_HISTORY ),
	};
	
	mc_Troop troops[] = {
		mc_CreateTroop("Coveira",              3, 430, 66,  ONLY_GROUND,           1.0f, 1.2f, 2.0f, PIRATE_EPOCH      ),
		mc_CreateTroop("Indígenas",            2, 160, 40,  GROUND_AND_AIR,        4.0f, 1.0f, 2.0f, PIRATE_EPOCH      ),
		mc_CreateTroop("Pelicano",             5, 777, 88,  ONLY_HERO_OR_BUILDING, 0.1f, 2.2f, 1.0f, PIRATE_EPOCH      ),
		mc_CreateTroop("Bandido",              4, 282, 60,  GROUND_AND_AIR,        5.5f, 1.1f, 2.0f, PIRATE_EPOCH      ),
		mc_CreateTroop("L-Robot",              5, 444, 98,  ONLY_GROUND,           0.5f, 1.6f, 2.5f, PIRATE_EPOCH      ),
		mc_CreateTroop("Capivaras",            5, 360, 45,  ONLY_HERO_OR_BUILDING, 0.5f, 0.9f, 3.0f, PIRATE_EPOCH      ),
		mc_CreateTroop("Esmagador",            7, 900, 122, ONLY_GROUND,           1.0f, 2.0f, 1.0f, FEUDAL_JAPAN      ),
		mc_CreateTroop("Caçadora De Samurais", 4, 390, 77,  ONLY_GROUND,           1.0f, 1.4f, 2.0f, FEUDAL_JAPAN      ),
		mc_CreateTroop("Assassino Da Peste",   4, 400, 53,  ONLY_GROUND,           1.0f, 1.1f, 2.5f, DARK_PLAGUE_ERA   ),
		mc_CreateTroop("Mosqueteiro Fantasma", 3, 290, 59,  GROUND_AND_AIR,        4.0f, 1.3f, 2.0f, DARK_PLAGUE_ERA   ),
		mc_CreateTroop("Freira",               4, 397, 70,  GROUND_AND_AIR,        1.5f, 1.3f, 1.5f, POST_TYRANNY_WORLD),
		mc_CreateTroop("Cavaleiro Dos Pampas", 5, 566, 77,  GROUND_AND_AIR,        1.5f, 1.5f, 2.0f, GAUCHO_HISTORY    ),
		mc_CreateTroop("Terópode Gigantesco",  8, 996, 97,  ONLY_GROUND,           1.0f, 1.0f, 0.5f, DINOSAURS_EPOCH   ),
	};
	
	mc_Build builds[] = {
		mc_CreateBuild("Bomba",           2, 80,  180, GROUND_AND_AIR, 1.0f, 1.0f,  PIRATE_EPOCH      ),
		mc_CreateBuild("Canhão",          3, 520, 80,  ONLY_GROUND,    5.0f, 1.0f,  TROUBLES_IN_FRANCE),
		mc_CreateBuild("Torreta",         4, 420, 20,  GROUND_AND_AIR, 9.0f, 0.4f,  POST_TYRANNY_WORLD),
		mc_CreateBuild("Quartel Alemão",  6, 555, 0,   ONLY_GROUND,    0.0f, 32.0f, POST_TYRANNY_WORLD),
	};
	
	mc_Spell spells[] = {
		mc_CreateSpell("Tempestades",         5, 222, GROUND_AND_AIR, 3.0f, 1.0f, 3.0f, PIRATE_EPOCH   ),
		mc_CreateSpell("Onda Gigante",        4, 100, ONLY_GROUND,    1.5f, 0.1f, 5.0f, PIRATE_EPOCH   ),
		mc_CreateSpell("Nevoeiro Assombrado", 6, 50,  GROUND_AND_AIR, 4.0f, 0.1f, 8.0f, DARK_PLAGUE_ERA),
		mc_CreateSpell("Chuva De Flechas",    3, 180, GROUND_AND_AIR, 2.5f, 1.0f, 1.0f, FEUDAL_JAPAN   ),
	};
	
	mc_Card initialCards[8] = {
	    {.i_Type = CARD_TROOP, .i_Troop = troops[0]},
    	{.i_Type = CARD_TROOP, .i_Troop = troops[1]},
	    {.i_Type = CARD_TROOP, .i_Troop = troops[2]},
    	{.i_Type = CARD_TROOP, .i_Troop = troops[3]},
	    {.i_Type = CARD_SPELL, .i_Spell = spells[0]},
    	{.i_Type = CARD_SPELL, .i_Spell = spells[1]},
	    {.i_Type = CARD_BUILD, .i_Build = builds[0]},
    	{.i_Type = CARD_BUILD, .i_Build = builds[1]},
	};
	
	mc_PlayerDeck myDeck = mc_CreatePlayerDeck(heroes[0], initialCards, 8);
}

int main() {
	mc_Initialize();
	
	sfVideoMode videoMode = {800, 600, 32};
	
	mc_GameWindow = sfRenderWindow_create(videoMode, "Multiverse Cards", sfResize | sfClose, NULL);
	
	if(!mc_GameWindow) {
		printf("A janela do jogo não inicializou, contate ao desenvolvedor para tirar suas dúvidas.");
		
		return 1;
	}
	
	while(sfRenderWindow_isOpen(mc_GameWindow)) {
		sfEvent windowEvent;
		
		while(sfRenderWindow_pollEvent(mc_GameWindow, &windowEvent)) {
			if(windowEvent.type == sfEvtClosed) {
				sfRenderWindow_close(mc_GameWindow);
			}
		}
		
		sfRenderWindow_clear(mc_GameWindow, sfBlack); // Limpa a cor de tela
		sfRenderWindow_display(mc_GameWindow); // Atualiza a tela do jogo
	}
	
	sfRenderWindow_destroy(mc_GameWindow);
	
	return 0;
}
