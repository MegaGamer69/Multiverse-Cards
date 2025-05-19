#ifndef MCARDS_INIT_HEADER
#define MCARDS_INIT_HEADER

#include <stdlib.h>

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
	
	char         i_Name[128];
	char         i_ClassID[128];
	unsigned int i_Level;
	unsigned int i_BaseHealth;
	unsigned int i_BaseDamage;
	unsigned int i_Health;
	unsigned int i_Damage;
	float        i_ARange;
	float        i_ATimer;
} mc_Hero;

// Tropa

typedef struct {
	// Dados de atributos
	
	char          i_Name[128];
	char          i_ClassID[128];
	unsigned int  i_BaseHealth;
	unsigned int  i_BaseDamage;
	unsigned int  i_Health;
	unsigned int  i_Damage;
	mc_AttackType i_AtType;
	float         i_ARange;
	float         i_ATimer;
	float         i_MSpeed;
} mc_Troop;

// Construção

typedef struct {
	// Dados de atributos
	
	char          i_Name[128];
	char          i_ClassID[128];
	unsigned int  i_Level;
	unsigned int  i_CDCost;
	unsigned int  i_BaseHealth;
	unsigned int  i_BaseDamage;
	unsigned int  i_Health;
	unsigned int  i_Damage;
	mc_AttackType i_AtType;
	float         i_ARange;
	float         i_ATimer;
} mc_Build;

// Feitiço

typedef struct {
	// Dados de atributos
	
	char          i_Name[128];
	char          i_ClassID[128];
	unsigned int  i_BaseDamage;
	unsigned int  i_Damage;
	mc_AttackType i_AtType;
	float         i_ARange;
	float         i_ATimer;
	float         i_Duration;
} mc_Spell;

typedef enum {
	CARD_TROOP,
	CARD_SPELL,
	CARD_BUILD,
} mc_CardType;

typedef struct {
	char         i_ClassID[128];
	mc_CardType  i_Type;
	unsigned int i_Level;
	unsigned int i_CDCost;
	
	union {
		mc_Troop i_Troop;
		mc_Spell i_Spell;
		mc_Build i_Build;
	};
	
	mc_LoreArch  i_LArch;
} mc_Card;

mc_Card mc_CreateCard(const char*  name,
                      const char*  classID,
                      unsigned int level,
                      mc_LoreArch  loreArch,
                      unsigned int cost,
                      mc_Troop     troop,
                      mc_Build     build,
                      mc_Spell     spell) {
	mc_Card instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	strncpy(instance.i_ClassID, classID, sizeof(instance.i_ClassID));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_ClassID[sizeof(instance.i_ClassID) - 1] = '\0';
	instance.i_Level = level;
	instance.i_LArch = loreArch;
	instance.i_CDCost = cost;
	instance.i_Troop = troop;
	instance.i_Build = build;
	instance.i_Spell = spell;
	
	return instance;
}

// Heróis servem para o jogador defender (evite desperdicios)

mc_Hero mc_CreateHero(const char*  name,
                      const char*  classID,
                      unsigned int health,
  					  unsigned int damage,
                      float        range,
                      float        attackTime) {
	mc_Hero instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	strncpy(instance.i_ClassID, classID, sizeof(instance.i_ClassID));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_ClassID[sizeof(instance.i_ClassID) - 1] = '\0';
	instance.i_Level = 1;
	instance.i_BaseHealth = health;
	instance.i_BaseDamage = damage;
	instance.i_Health = health;
	instance.i_Damage = damage;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	
	return instance;
}

mc_Troop mc_CreateTroop(unsigned int  health,
  					    unsigned int  damage,
					    mc_AttackType atType,
					    float         range,
					    float         attackTime,
					    float         movSpeed) {
	mc_Troop instance;
	
	instance.i_BaseHealth = health;
	instance.i_BaseDamage = damage;
	instance.i_Health = health;
	instance.i_Damage = damage;
	instance.i_AtType = atType;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	instance.i_MSpeed = movSpeed;
	
	return instance;
}

mc_Build mc_CreateBuild(unsigned int  health,
  					    unsigned int  damage,
  					    mc_AttackType atType,
  					    float         range,
            			float         attackTime) {
	mc_Build instance;
	
	instance.i_BaseHealth = health;
	instance.i_BaseDamage = damage;
	instance.i_Health = health;
	instance.i_Damage = damage;
	instance.i_AtType = atType;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	
	return instance;
}

mc_Spell mc_CreateSpell(unsigned int  damage,
  					    mc_AttackType atType,
  					    float         range,
            			float         attackTime,
            			float         duration) {
	mc_Spell instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_BaseDamage = damage;
	instance.i_Damage = damage;
	instance.i_AtType = atType;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	instance.i_Duration = duration;
	
	return instance;
}

// As cartas podem ser melhoradas a partir de recursos como diamantes (que se consegue em partidas on-line, TEM QUE SER ON-LINE)

void mc_UpgradeCard(const char*   name,
                    unsigned int* level,
                    unsigned int* baseHealth,
                    unsigned int* baseDamage,
                    unsigned int* health,
                    unsigned int* damage) {
	if(*level >= CARD_MAX_LEVEL) {
		return;
	}
	
	(*level)++;
	
	*health = (int)((*baseHealth) * (1.0f + 0.35f * (*level - 1)));
	*damage = (int)((*baseDamage) * (1.0f + 0.25f * (*level - 1)));
}

void mc_UpgradeHero(const char*   name,
                    unsigned int* level,
                    unsigned int* baseHealth,
                    unsigned int* baseDamage,
                    unsigned int* health,
                    unsigned int* damage) {
	if(*level >= HERO_MAX_LEVEL) {
		return;
	}
	
	(*level)++;
	
	*health = (int)((*baseHealth) * (1.0f + 0.3f  * (*level - 1)));
	*damage = (int)((*baseDamage) * (1.0f + 0.35f * (*level - 1)));
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
	deck.d_SelectedHero = hero;
	
	return deck;
}

/**
 * Embaralhe o deck para dar imprevibilidades no mesmo
 */
void mc_ShufflePlayerDeck(mc_PlayerDeck* deck) {
	for(size_t i = deck->d_CardCount - 1; i > 0; i--) {
		size_t j = rand() % (i + 1);
		
		mc_Card temp = deck->d_DeckCards[i];
		
		deck->d_DeckCards[i] = deck->d_DeckCards[j];
		deck->d_DeckCards[j] = temp;
	}
}

#endif
