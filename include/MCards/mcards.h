#ifndef MCARDS_INIT_HEADER
#define MCARDS_INIT_HEADER

#include <stdlib.h>

#define CARD_MAX_LEVEL       8 // Tropas, construções e feitiços são cartas! os heróis... bem, eles não...
#define HERO_MAX_LEVEL       9 // HERÓIS NÃO SÃO CARTAS! LEMBRE-SE DISSO

#define MAX_CARDS_PER_DECK   8 // Basicamente um Clash Royale haha!
#define MAX_HEROES_PER_DECK  1 // Balanceamento, já que teria que defender dois heróis ao mesmo tempo
#define CARDS_TO_RENDER      4 // Número de cartas para a mão principal
#define MAX_CHAR_PER_FIELD 256 // Número máximo de caracteres por cada array como nome, ID de classe... SEU CPF-

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
	
	char         i_Name[MAX_CHAR_PER_FIELD];
	char         i_ClassID[MAX_CHAR_PER_FIELD];
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
	char         i_Name[MAX_CHAR_PER_FIELD];
	char         i_ClassID[MAX_CHAR_PER_FIELD];
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

static inline mc_Card mc_CreateCardTroop(const char*  name,
                                         const char*  classID,
                                         unsigned int level,
                                         mc_LoreArch  loreArch,
                                         unsigned int cost,
                                         mc_Troop     troop,
                                         unsigned int amount) {
	mc_Card instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	strncpy(instance.i_ClassID, classID, sizeof(instance.i_ClassID));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_ClassID[sizeof(instance.i_ClassID) - 1] = '\0';
	instance.i_Level = level;
	instance.i_LArch = loreArch;
	instance.i_CDCost = cost;
	instance.i_Type = CARD_TROOP;
	instance.i_Troop = troop;
	
	return instance;
}

static inline mc_Card mc_CreateCardBuild(const char*  name,
                                         const char*  classID,
                                         unsigned int level,
                                         mc_LoreArch  loreArch,
                                         unsigned int cost,
                                         mc_Build     build) {
	mc_Card instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	strncpy(instance.i_ClassID, classID, sizeof(instance.i_ClassID));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_ClassID[sizeof(instance.i_ClassID) - 1] = '\0';
	instance.i_Level = level;
	instance.i_LArch = loreArch;
	instance.i_CDCost = cost;
	instance.i_Type = CARD_BUILD;
	instance.i_Build = build;
	
	return instance;
}

static inline mc_Card mc_CreateCardSpell(const char*  name,
                                         const char*  classID,
                                         unsigned int level,
                                         mc_LoreArch  loreArch,
                                         unsigned int cost,
                                         mc_Spell     spell) {
	mc_Card instance;
	
	strncpy(instance.i_Name, name, sizeof(instance.i_Name));
	strncpy(instance.i_ClassID, classID, sizeof(instance.i_ClassID));
	
	instance.i_Name[sizeof(instance.i_Name) - 1] = '\0';
	instance.i_ClassID[sizeof(instance.i_ClassID) - 1] = '\0';
	instance.i_Level = level;
	instance.i_LArch = loreArch;
	instance.i_CDCost = cost;
	instance.i_Type = CARD_SPELL;
	instance.i_Spell = spell;
	
	return instance;
}

// Heróis servem para o jogador defender (evite desperdicios)

static inline mc_Hero mc_CreateHero(const char*  name,
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

static inline mc_Troop mc_CreateTroop(unsigned int  health,
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

static inline mc_Build mc_CreateBuild(unsigned int  health,
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

static inline mc_Spell mc_CreateSpell(unsigned int  damage,
  					    mc_AttackType atType,
  					    float         range,
            			float         attackTime,
            			float         duration) {
	mc_Spell instance;
	
	instance.i_BaseDamage = damage;
	instance.i_Damage = damage;
	instance.i_AtType = atType;
	instance.i_ARange = range;
	instance.i_ATimer = attackTime;
	instance.i_Duration = duration;
	
	return instance;
}

// As cartas podem ser melhoradas a partir de recursos como diamantes (que se consegue em partidas on-line, TEM QUE SER ON-LINE)

static inline void mc_UpgradeCard(mc_Card* card) {
	if(card->i_Level >= CARD_MAX_LEVEL) {
		return;
	}
	
	(card->i_Level)++;
	
	if(card->i_Type == CARD_TROOP) {
		card->i_Troop.i_Health = (int)((card->i_Troop.i_BaseHealth) * (1.0f + 0.18f * (card->i_Level - 1)));
		card->i_Troop.i_Damage = (int)((card->i_Troop.i_BaseDamage) * (1.0f + 0.18f * (card->i_Level - 1)));
		
		printf("%s acaba de subir para nível %u! (%u de hp, %u de dm)\n", card->i_Name, card->i_Level, card->i_Troop.i_Health, card->i_Troop.i_Damage);
	}
	
	if(card->i_Type == CARD_BUILD) {
		card->i_Build.i_Health = (int)((card->i_Build.i_BaseHealth) * (1.0f + 0.18f * (card->i_Level - 1)));
		card->i_Build.i_Damage = (int)((card->i_Build.i_BaseDamage) * (1.0f + 0.18f * (card->i_Level - 1)));
		
		printf("%s acaba de subir para nível %u! (%u de hp, %u de dm)\n", card->i_Name, card->i_Level, card->i_Build.i_Health, card->i_Build.i_Damage);
	}
	
	if(card->i_Type == CARD_SPELL) {
		card->i_Spell.i_Damage = (int)((card->i_Spell.i_BaseDamage) * (1.0f + 0.18f * (card->i_Level - 1)));
		
		printf("%s acaba de subir para nível %u! (%u de dm)\n", card->i_Name, card->i_Level, card->i_Spell.i_Damage);
	}
}

static inline void mc_UpgradeHero(mc_Hero* hero) {
	if(hero->i_Level >= CARD_MAX_LEVEL) {
		return;
	}
	
	(hero->i_Level)++;
	
	hero->i_Health = (int)((hero->i_BaseHealth) * (1.0f + 0.18f * (hero->i_Level - 1)));
	hero->i_Damage = (int)((hero->i_BaseDamage) * (1.0f + 0.18f * (hero->i_Level - 1)));
	
	printf("%s acaba de subir para nível %u! (%u de hp, %u de dm)\n", hero->i_Name, hero->i_Level, hero->i_Health, hero->i_Damage);
}

// Campos globais

static sfRenderWindow* mc_GameWindow;
static sfFont* mc_GameTextualFont;

// Baralho do jogador

typedef struct {
	mc_Hero  d_SelectedHero;
	mc_Card  d_DeckCards[MAX_CARDS_PER_DECK];
	size_t   d_CardCount;
} mc_PlayerDeck;

/**
 * Cria um deck para o jogador com um herói e oito cartas exatamente
 */
static inline mc_PlayerDeck mc_CreatePlayerDeck(mc_Hero hero,
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
static inline void mc_ShufflePlayerDeck(mc_PlayerDeck* deck) {
	for(size_t i = deck->d_CardCount - 1; i > 0; i--) {
		size_t j = rand() % (i + 1);
		
		mc_Card temp = deck->d_DeckCards[i];
		
		deck->d_DeckCards[i] = deck->d_DeckCards[j];
		deck->d_DeckCards[j] = temp;
	}
}

#endif
