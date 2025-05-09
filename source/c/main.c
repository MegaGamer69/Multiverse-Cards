#define CARD_MAX_LEVEL 9      // Tropas, construções e feitiços são cartas
#define HERO_MAX_LEVEL 9      // HERÓIS NÃO SÃO CARTAS!

#define MAX_CARDS_PER_DECK 8  // Basicamente um Clash Royale haha!
#define MAX_HEROES_PER_DECK 1 // Balanceamento, já que teria que defender dois heróis ao mesmo tempo

#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>

#include <MCards/graphics.h>
#include <MCards/mcards.h>

#include <SFML/Window.h>
#include <SFML/Graphics.h>
#include <SFML/System.h>

int main() {
	mc_Hero mc_HeroList[] = {
		mc_CreateHero("Pirata",          "pirate",      1900, 32, 5.5f, 1.4f),
		mc_CreateHero("Índio Bombado",   "mighty",      1960, 20, 3.5f, 0.5f),
		mc_CreateHero("Shugun Renegado", "shugun",      2000, 30, 4.0f, 1.8f),
		mc_CreateHero("Alquimista",      "chemical",    1890, 26, 7.0f, 1.0f),
		mc_CreateHero("Mateador",        "livestocker", 1780, 28, 5.5f, 1.1f),
	};
	
	mc_Troop mc_TroopList[] = {
		mc_CreateTroop("Coveira",               "gravedigger", 3, 400,  66,  ONLY_GROUND,           1.0f,  1.2f, 2.0f),
		mc_CreateTroop("Indígenas",             "indians",     2, 160,  40,  GROUND_AND_AIR,        4.0f,  1.0f, 2.0f),
		mc_CreateTroop("Pelicano",              "pelican",     5, 777,  78,  ONLY_HERO_OR_BUILDING, 0.1f,  2.4f, 1.2f),
		mc_CreateTroop("Bandido",               "bandit",      4, 282,  60,  GROUND_AND_AIR,        5.5f,  1.1f, 2.0f),
		mc_CreateTroop("L-Robot",               "lrobot",      5, 444,  98,  ONLY_GROUND,           0.5f,  1.6f, 2.5f),
		mc_CreateTroop("Capivaras",             "capybaras",   5, 360,  45,  ONLY_HERO_OR_BUILDING, 0.5f,  0.9f, 3.0f),
		mc_CreateTroop("Bombardeiros De Corda", "bomber",      3, 192,  55,  GROUND_AND_AIR,        1.2f,  1.1f, 1.5f),
		mc_CreateTroop("Esmagador",             "crusher",     7, 893,  122, ONLY_GROUND,           1.0f,  1.9f, 1.0f),
		mc_CreateTroop("Caçadora De Samurais",  "samhunter",   4, 390,  77,  ONLY_GROUND,           1.0f,  1.4f, 2.0f),
		mc_CreateTroop("Assassino Da Peste",    "plagekiller", 4, 400,  53,  ONLY_GROUND,           1.0f,  1.1f, 2.5f),
		mc_CreateTroop("Mosqueteiro Fantasma",  "ghostmusket", 3, 290,  59,  GROUND_AND_AIR,        4.0f,  1.3f, 2.0f),
		mc_CreateTroop("Mosquitos",             "mosquitoes",  2, 16,   12,  GROUND_AND_AIR,        0.5f,  1.5f, 1.5f),
		mc_CreateTroop("Ceifador",              "reaper",      6, 860,  84,  ONLY_GROUND,           1.5f,  1.5f, 2.0f),
		mc_CreateTroop("Freira",                "nun",         4, 397,  70,  GROUND_AND_AIR,        1.5f,  1.3f, 1.5f),
		mc_CreateTroop("H-Robot",               "hrobot",      8, 1000, 100, ONLY_HERO_OR_BUILDING, 0.5f,  2.0f, 1.2f),
		mc_CreateTroop("Atirador",              "sniper",      4, 300,  72,  GROUND_AND_AIR,        10.0f, 1.5f, 2.0f),
		mc_CreateTroop("Cavaleiro Dos Pampas",  "gaucho",      5, 566,  77,  GROUND_AND_AIR,        1.5f,  1.5f, 2.0f),
		mc_CreateTroop("Terópode Gigantesco",   "terophod",    8, 1100, 97,  ONLY_GROUND,           1.0f,  1.0f, 0.5f),
	};
	
	mc_Build mc_BuildList[] = {
		mc_CreateBuild("Bomba",          "bomb",   3, 80,  166, GROUND_AND_AIR, 1.0f, 1.0f),
		mc_CreateBuild("Canhão",         "cannon", 3, 520, 80,  ONLY_GROUND,    5.0f, 1.0f),
		mc_CreateBuild("Torreta",        "turret", 4, 420, 20,  GROUND_AND_AIR, 9.0f, 0.4f),
		mc_CreateBuild("Quartel Alemão", "german", 6, 598, 0,   ONLY_GROUND,    0.0f, 0.0f),
	};
	
	mc_Spell mc_SpellList[] = {
		mc_CreateSpell("Tempestades",         "storms", 5, 200, GROUND_AND_AIR, 3.0f, 1.0f, 3.0f),
		mc_CreateSpell("Onda Gigante",        "waves",  4, 100, ONLY_GROUND,    1.5f, 0.1f, 5.0f),
		mc_CreateSpell("Nevoeiro Assombrado", "fog",    6, 53,  GROUND_AND_AIR, 4.0f, 0.1f, 8.0f),
		mc_CreateSpell("Chuva De Flechas",    "arrows", 2, 90,  GROUND_AND_AIR, 2.5f, 1.0f, 1.0f),
	};
	
	mc_Card initialCards[8] = {
	    {.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[0]},
    	{.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[1]},
	    {.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[2]},
    	{.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[3]},
	    {.i_Type = CARD_SPELL, .i_Spell = mc_SpellList[0]},
    	{.i_Type = CARD_SPELL, .i_Spell = mc_SpellList[1]},
	    {.i_Type = CARD_BUILD, .i_Build = mc_BuildList[0]},
    	{.i_Type = CARD_BUILD, .i_Build = mc_BuildList[1]},
	};
	
	mc_PlayerDeck mc_MyDeck = mc_CreatePlayerDeck(mc_HeroList[0], initialCards, 8);
	
	sfVideoMode videoMode = {720, 1280, 32};
	
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
		
		sfRenderWindow_clear(mc_GameWindow, sfWhite);
		
		// Aqui vai renderizar a porra toda! EBA!!!!
		
		mc_DrawClientDeck(mc_GameWindow, &mc_MyDeck);
		
		sfRenderWindow_display(mc_GameWindow);
	}
	
	sfRenderWindow_destroy(mc_GameWindow);
	
	return 0;
}
