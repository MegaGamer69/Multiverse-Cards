#ifndef MCARDS_GRAPHICS_HEADER
#define MCARDS_GRAPHICS_HEADER

#include <stdio.h>
#include <string.h>
#include <SFML/Graphics.h>
#include <MCards/mcards.h>

#include <MCards/cards/gravedigger.h>
#include <MCards/cards/indians.h>
#include <MCards/cards/pelican.h>

#define MAX_CARD_TEXTURES 26

sfTexture* g_CardTextures[MAX_CARD_TEXTURES];
char g_TexturePaths[MAX_CARD_TEXTURES][256];
size_t g_CardTextureCount = 0;

const char* mc_GetTextureFromClassID(const char* classID) {
	static char buffer[256];
	
	snprintf(buffer, sizeof(buffer), "assets/cards/%s.png", classID);
	
	return buffer;
}

sfTexture* mc_LoadTexture(const char* path) {
	for(size_t i = 0; i < g_CardTextureCount; ++i) {
		if(strcmp(g_TexturePaths[i], path) == 0) {
			return g_CardTextures[i];
		}
	}
	
	sfTexture* newTexture = sfTexture_createFromFile(path, NULL);
	
	if(newTexture && g_CardTextureCount < MAX_CARD_TEXTURES) {
		strncpy(g_TexturePaths[g_CardTextureCount], path, sizeof(g_TexturePaths[0]) - 1);
		g_TexturePaths[g_CardTextureCount][sizeof(g_TexturePaths[0]) - 1] = '\0';
		
		g_CardTextures[g_CardTextureCount] = newTexture;
		g_CardTextureCount++;
	}
	
	return newTexture;
}

void mc_DrawCard(sfRenderWindow* window, mc_Card* card, sfVector2f pos) {
	sfTexture* texture = NULL;
	
	switch(card->i_Type) {
		case CARD_TROOP:
			texture = mc_LoadTexture(mc_GetTextureFromClassID(card->i_Troop.i_ClassID));
			
			break;
		case CARD_BUILD:
			texture = mc_LoadTexture(mc_GetTextureFromClassID(card->i_Build.i_ClassID));
			
			break;
		case CARD_SPELL:
			texture = mc_LoadTexture(mc_GetTextureFromClassID(card->i_Spell.i_ClassID));
			
			break;
	}
	
	sfRectangleShape* cardShape = sfRectangleShape_create();
	
	sfRectangleShape_setSize(cardShape, (sfVector2f){120, 171});
	sfRectangleShape_setPosition(cardShape, pos);
	
	if(texture) {
		sfRectangleShape_setTexture(cardShape, texture, sfTrue);
	} else {
		sfRectangleShape_setFillColor(cardShape, sfColor_fromRGB(255, 0, 0));
	}
	
	sfRenderWindow_drawRectangleShape(window, cardShape, NULL);
    sfRectangleShape_destroy(cardShape);
}

void mc_DrawClientDeck(sfRenderWindow* window, mc_PlayerDeck* deck) {
	for(size_t i = 0; i < 4; i++) {
		sfVector2f pos = {75 + (i * 140), 400};
		
		mc_DrawCard(window, &deck->d_DeckCards[i], pos);
	}
}

#endif
