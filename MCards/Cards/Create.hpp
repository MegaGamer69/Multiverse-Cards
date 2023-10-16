/**
 * code by MegaGamer69(me)
 * credits to Supercell :)
**/

#ifndef MCARDS_CARDS_CREATE_HPP
#define MCARDS_CARDS_CREATE_HPP

#include <../../SFML/Graphics.hpp>
#include <string>

namespace mc {
    class Create {
    public:
        Create(std::string Name, std::string Texture, int Health, int Damage, float AtkSpeed, float MovSpeed, int Mass, std::string Type) :
        CardName(Name), CardTexture(Texture), CardHP(Health), CardDMG(Damage), CardAtk(AtkSpeed), CardMov(MovSpeed), CardMass(Mass), CardType(Type) {
            if(!sf::Texture.loadFromTexture(CardTexture)) {
                // idk
            }
            
            if(CardHP == 0 && CardType != "Spell") {
                // spell cards are invulnerable
            }
        }
    }
}

#endif