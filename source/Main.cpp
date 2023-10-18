/**
 * code by MegaGamer69(me)
 * credits to Supercell :)
**/

// include the SFML basics
#include "../SFML/Window.hpp"
#include "../SFML/System.hpp"
#include "../SFML/Graphics.hpp"

// include the STD lib
#include <string>
#include <iostream>

class Card {
public:
    Card(std::string& Name, std::string& Texture, int Health, int Damage, float AttackSpeed, float MoveSpeed, std::string& Type, bool Flying, bool AtkInAirAlso, int Mass, int Cost, bool AtkOnlyBuild) :
    CardName(Name), CardTexture(Texture), CardHealth(Health), CardDamage(Damage), CardAttackSpeed(AttackSpeed), CardMoveSpeed(MoveSpeed), CardType(Type), FlyingCard(Flying), CardAtkAirAlso(AtkInAirAlso), CardMass(Mass), CardCost(Cost), AtkOnlyBuildings(AtkOnlyBuild) {
        // meh :/
    }
private:
    std::string CardName;
    std::string CardTexture;
    int CardHealth;
    int CardDamage;
    float CardAttackSpeed;
    float CardMoveSpeed;
    std::string CardType;
    bool FlyingCard;
    bool CardAtkAirAlso;
    int CardMass;
    int CardCost;
    bool AtkOnlyBuildings;
};

class Game {
public:
    Game() : Window(sf::VideoMode(720, 1280), "MultiverseCards") {
    	// nothing to see here :/
    }
    
    void Run() {
        while(Window.isOpen()) {
            sf::Event EventListener;
            while(Window.pollEvent(EventListener)) {
                if(EventListener.type == sf::Event::Closed) {
                    Window.close();
                }
            }
            
            Window.display();
        }
    }
private:
    sf::RenderWindow Window;
};

// trainers is the most important on game, if your trainer has been defeated, game over
class Trainer {
public:
    Trainer(std::string& Name, std::string& Texture, int Health, int Damage, float AtkSpeed) :
    TrainerName(Name), TexturePath(Texture), TrainerHealth(Health), TrainerDamage(Damage), TrainerAtkSpeed(AtkSpeed) {
        // nothing to see here :(
    }
private:
    std::string TrainerName;
    std::string TexturePath;
    int TrainerHealth;
    int TrainerDamage;
    float TrainerAtkSpeed;
};

void MainDeck() {
    // basic cards and trainers
    // spell cards are not vulnerable
    Trainer T1("Pirate", "../assets/images/trainer/trainer1.png", 720, 111, 1.8f);
    Card C1("Reaper", "../assets/images/card/card1.png", 444, 96, 1.2f, 2, "Troop", false, false, 70, 4, false);
    Card C2("Indians", "../assets/images/cards/card2.png", 120, 50, 1, 2.1f, "Troop", false, true, 68, 2, false);
    Card C3("Cannon", "../assets/images/cards/card3.png", 390, 70, 1.1f, 0, "Building", false, false, 600, 3, false);
    Card C4("Pelican", "../assets/images/cards/card4.png", 600, 96, 2, 1.8f, "Troop", true, false, 100, 5, true);
    Card C5("Fireball", "../assets/images/cards/card5.png", 0, 150, 3, 0, "Spell", true, false, 0, 4, false);
    Card C6("Eletric Tower", "../assets/images/cards/card6.png", 300, 70, 1.1f, 0, "Building", false, true, 600, 4, false);
}

int main() {
    Game MainGame;
    MainGame.Run();
    
    return 0;
}