// Constantes de merda
#define CARD_MAX_LEVEL          9 // Tropas, construções e feitiços são cartas! os heróis... bem, eles não...
#define HERO_MAX_LEVEL         12 // HERÓIS NÃO SÃO CARTAS! LEMBRE-SE DISSO

#define MAX_CARDS_PER_DECK      8 // Basicamente um Clash Royale haha!
#define MAX_HEROES_PER_DECK     1 // Balanceamento, já que teria que defender dois heróis ao mesmo tempo
#define CARDS_TO_RENDER         4 // Número de cartas para a mão principal

#define CARD_WIDTH            120 // Tamanho de largura da carta
#define CARD_HEIGHT           171 // Tamango de altura da carta
#define DECK_POS_Y            400 // Posição de início do alinhamento vertical... OH YEAH
#define PLAY_AREA_MAX_Y       300 // O máximo que você pode posicionar sua carta!

// Pensa comigo: o compilador basicamente já tem esses cabeçalhos, POR QUE PRECISO INCLUIR-LAS MANUALMENTE?! (ironia)

#include <stddef.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>
#include <time.h>

// Inclusas diretamente em "<Raíz do projeto>/include/<blah blah blah...>/<cabeçalho>.h"

#include <MCards/graphics.h>
#include <MCards/mcards.h>
#include <SFML/Window.h>
#include <SFML/Graphics.h>
#include <SFML/System.h>

// O estado de alocação das unidades (tropas, feitiços, construções... HERÓ- brincadeira!)

typedef enum {
    DRAG_STATE_IDLE,
    DRAG_STATE_HOLDING,
    DRAG_STATE_DRAGGING
} mc_DragState;

static bool mc_IsDraggingCard = false;
static int mc_SelectedCardIndex = -1;

static sfVector2f mc_CardStartPosition;

static sfVector2i mc_MousePosition;

static sfVector2f mc_MouseGrabOffset;
static mc_DragState mc_CardDragState = DRAG_STATE_IDLE;

static mc_PlayerDeck mc_ClientDeck;

// Manipule a cacetada que vou dar na sua cabeça se falar que "Heróis são cartas"
// Digo... a entrada de usuário...

void mc_HandleInput(sfEvent windowEvent) {
	// Como dizia o interruptor: "eu alterno entre 0 e 1"
	
	switch(windowEvent.type) {
		case sfEvtClosed:
			sfRenderWindow_close(mc_GameWindow);
			
			break;
		case sfEvtMouseButtonPressed:
			if(windowEvent.mouseButton.button == sfMouseLeft) {
				mc_MousePosition = sfMouse_getPositionRenderWindow(mc_GameWindow);
				
				for(int i = 0; i < CARDS_TO_RENDER; i++) {
					sfFloatRect cardBounds = {
						75.0f + (i * 140),
						DECK_POS_Y,
						CARD_WIDTH,
						CARD_HEIGHT
					};
					
					if(sfFloatRect_contains(&cardBounds, mc_MousePosition.x, mc_MousePosition.y)) {
						mc_CardDragState = DRAG_STATE_HOLDING;
						
						mc_IsDraggingCard = true;
						mc_SelectedCardIndex = i;
						
						mc_MouseGrabOffset = (sfVector2f){
							mc_MousePosition.x - cardBounds.left,
							mc_MousePosition.y - cardBounds.top
						};
						
						break;
					}
				}
				
				break;
			}
			
			break;
		case sfEvtMouseMoved:
			if(mc_CardDragState == DRAG_STATE_HOLDING) {
				sfVector2i currentMousePosition = sfMouse_getPositionRenderWindow(mc_GameWindow);
				
				sfVector2i delta = {
					abs(mc_MousePosition.x - currentMousePosition.x),
					abs(mc_MousePosition.y - currentMousePosition.y)
				};
				
				if(delta.x > 5 || delta.y > 5) {
					mc_CardDragState = DRAG_STATE_DRAGGING;
				}
				
				break;
			}
			
			break;
		case sfEvtMouseButtonReleased:
			if(windowEvent.mouseButton.button == sfMouseLeft) {
				if(mc_CardDragState == DRAG_STATE_DRAGGING) {
					printf("Carta posicionada!\n");
				}
				
				mc_SelectedCardIndex = -1;
			}
			
			break;
	}
}

void mc_LoopUpdate() {
	mc_DrawClientDeck(mc_GameWindow, &mc_ClientDeck);
}

// Aqui, iremos fazer de tudo para prestar

int main() {
	srand((unsigned int)(time(NULL)));
	
	mc_Hero mc_HeroList[] = {
		mc_CreateHero("Pirata",          "pirate",      1900, 32, 5.5f, 1.4f),
		mc_CreateHero("Índio Bombado",   "mighty",      1960, 20, 3.5f, 0.7f),
		
		mc_CreateHero("Shugun Renegado", "shugun",      2000, 30, 4.0f, 1.8f),
		
		mc_CreateHero("Alquimista",      "chemical",    1890, 26, 7.0f, 1.0f),
		
		mc_CreateHero("Mateador",        "livestocker", 1780, 28, 5.5f, 1.1f),
		mc_CreateHero("Caçador",         "hunter",      1920, 23, 6.5f, 1.6f),
	};
	
	mc_Troop mc_TroopList[] = {
		mc_CreateTroop("Coveira",               "gravedigger", 3, 400,  66,  ONLY_GROUND,           1.0f,  1.2f, 2.0f),
		mc_CreateTroop("Indígenas",             "indians",     2, 160,  40,  GROUND_AND_AIR,        4.0f,  1.0f, 2.0f),
		mc_CreateTroop("Pelicano",              "pelican",     5, 777,  78,  ONLY_HERO_OR_BUILDING, 0.1f,  2.4f, 1.2f),
		mc_CreateTroop("Bandido",               "bandit",      4, 282,  60,  GROUND_AND_AIR,        5.5f,  1.1f, 2.0f),
		mc_CreateTroop("L-Robot",               "lrobot",      5, 444,  98,  ONLY_GROUND,           0.5f,  1.6f, 2.5f),
		mc_CreateTroop("Capivaras",             "capybaras",   5, 360,  45,  ONLY_HERO_OR_BUILDING, 0.5f,  0.9f, 3.0f),
		mc_CreateTroop("Bombardeiros De Corda", "bombers",     3, 192,  55,  GROUND_AND_AIR,        1.2f,  1.1f, 1.5f),
		
		mc_CreateTroop("Esmagador",             "crusher",     7, 893,  122, ONLY_GROUND,           1.0f,  1.9f, 1.0f),
		mc_CreateTroop("Caçadora De Samurais",  "samhunter",   4, 390,  77,  ONLY_GROUND,           1.0f,  1.4f, 2.0f),
		
		mc_CreateTroop("Assassino Da Peste",    "plagekiller", 4, 400,  53,  ONLY_GROUND,           1.0f,  1.1f, 2.5f),
		mc_CreateTroop("Mosqueteiro Fantasma",  "ghostmusket", 3, 290,  59,  GROUND_AND_AIR,        4.0f,  1.3f, 2.0f),
		mc_CreateTroop("Mosquitos",             "mosquitoes",  2, 16,   12,  GROUND_AND_AIR,        0.5f,  1.5f, 1.5f),
		mc_CreateTroop("Ceifador",              "reaper",      6, 860,  84,  ONLY_GROUND,           1.5f,  1.5f, 2.0f),
		
		mc_CreateTroop("Freira",                "nun",         4, 397,  70,  GROUND_AND_AIR,        1.5f,  1.3f, 1.5f),
		mc_CreateTroop("H-Robot",               "hrobot",      8, 950,  98,  ONLY_HERO_OR_BUILDING, 0.5f,  2.0f, 1.2f),
		mc_CreateTroop("Atirador",              "sniper",      4, 300,  72,  GROUND_AND_AIR,        10.0f, 1.5f, 2.0f),
		
		mc_CreateTroop("Cavaleiro Dos Pampas",  "gaucho",      5, 566,  77,  GROUND_AND_AIR,        1.5f,  1.5f, 2.0f),
		mc_CreateTroop("Guerreiro Farroupilha", "warrior",     4, 487,  67,  ONLY_GROUND,           1.5f,  1.3f, 2.0f),
		
		mc_CreateTroop("Terópode Gigantesco",   "terophod",    8, 1100, 87,  ONLY_GROUND,           1.0f,  1.3f, 1.0f),
	};
	
	mc_Build mc_BuildList[] = {
		mc_CreateBuild("Bomba",          "bomb",   3, 80,  166, GROUND_AND_AIR, 1.0f, 1.0f),
		
		mc_CreateBuild("Canhão",         "cannon", 3, 520, 80,  ONLY_GROUND,    5.0f, 1.0f),
		mc_CreateBuild("Torreta",        "turret", 4, 420, 20,  GROUND_AND_AIR, 9.0f, 0.4f),
		mc_CreateBuild("Quartel Alemão", "german", 6, 598, 0,   ONLY_GROUND,    0.0f, 0.0f),
	};
	
	mc_Spell mc_SpellList[] = {
		mc_CreateSpell("Tempestades",         "storms",       5, 200, GROUND_AND_AIR, 3.0f, 1.0f, 3.0f),
		mc_CreateSpell("Onda Gigante",        "waves",        4, 100, ONLY_GROUND,    1.5f, 0.1f, 5.0f),
		
		mc_CreateSpell("Nevoeiro Assombrado", "fog",          6, 53,  GROUND_AND_AIR, 4.0f, 0.1f, 8.0f),
		mc_CreateSpell("Marreta Do Caos",     "sledgehammer", 3, 106, ONLY_GROUND,    3.0f, 1.0f, 3.0f),
		
		mc_CreateSpell("Chuva De Flechas",    "arrows",       2, 100, GROUND_AND_AIR, 2.5f, 1.0f, 1.0f),
		
		mc_CreateSpell("Erupção Mortal",      "eruption",     6, 120, GROUND_AND_AIR, 2.0f, 0.5f, 2.0f),
	};
	
	mc_Card mc_InitialCards[8] = {
	    {.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[0]},
    	{.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[1]},
	    {.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[2]},
    	{.i_Type = CARD_TROOP, .i_Troop = mc_TroopList[3]},
	    {.i_Type = CARD_SPELL, .i_Spell = mc_SpellList[0]},
    	{.i_Type = CARD_SPELL, .i_Spell = mc_SpellList[1]},
	    {.i_Type = CARD_BUILD, .i_Build = mc_BuildList[0]},
    	{.i_Type = CARD_BUILD, .i_Build = mc_BuildList[1]},
	};
	
	mc_ClientDeck = mc_CreatePlayerDeck(mc_HeroList[0], mc_InitialCards, 8);
	
	mc_ShufflePlayerDeck(&mc_ClientDeck);
	
	sfVideoMode videoMode = {720, 1280, 32};
	
	mc_GameWindow = sfRenderWindow_create(videoMode, "Multiverse Cards", sfResize | sfClose, NULL);
	
	if(!mc_GameWindow) {
		printf("A janela do jogo não inicializou, contate ao desenvolvedor para tirar suas dúvidas.\n");
		
		return 1;
	}
	
	while(sfRenderWindow_isOpen(mc_GameWindow)) {
		sfEvent event;
		
		while(sfRenderWindow_pollEvent(mc_GameWindow, &event)) {
			mc_HandleInput(event);
		}
		
		sfRenderWindow_clear(mc_GameWindow, sfWhite);
		
		// Aqui vai atualizar a porra toda! EBA!!!!
		
		mc_LoopUpdate();
		
		sfRenderWindow_display(mc_GameWindow);
	}
	
	sfRenderWindow_destroy(mc_GameWindow);
	
	return 0;
}
