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
#include <vector>

using namespace sf;

class Card {
  public:
    Card(const std::string Name, const std::string Texture, int Health, int Damage, float AttackSpeed, float MoveSpeed, const std::string Type, bool Flying, bool AtkInAirAlso, int Mass, int Cost, bool AtkOnlyBuild) :
    CardName(Name), CardTexture(Texture), CardHealth(Health), CardDamage(Damage), CardAttackSpeed(AttackSpeed), CardMoveSpeed(MoveSpeed), CardType(Type), FlyingCard(Flying), CardAtkAirAlso(AtkInAirAlso), CardMass(Mass), CardCost(Cost), AtkOnlyBuildings(AtkOnlyBuild) {
        if(!TextureLOL.loadFromFile(CardTexture)) {
            std::cout << "A" << std::endl;
        } else {
            std::cout << "B" << std::endl;
        }
    }
  private:
    const std::string CardName;
    const std::string CardTexture;
    int CardHealth;
    int CardDamage;
    float CardAttackSpeed;
    float CardMoveSpeed;
    const std::string CardType;
    bool FlyingCard;
    bool CardAtkAirAlso;
    int CardMass;
    int CardCost;
    bool AtkOnlyBuildings;
    
    // amogus HAHA
    Texture TextureLOL;
};

// trainers is the most important on game, if your trainer has been defeated, game over
class Trainer {
  public:
    Trainer(const std::string Name, const std::string Texture, int Health, int Damage, float AtkSpeed) :
    TrainerName(Name), TexturePath(Texture), TrainerHealth(Health), TrainerDamage(Damage), TrainerAtkSpeed(AtkSpeed) {
        
    }
    
    void ReceiveDamage(int Damage) {
        TrainerHealth -= Damage;
    }
    
    void CheckHP() {
        if(TrainerHealth <= 0) {
            std::cout << "Trainer has been defeated" << std::endl;
        }
    }
    
  private:
    const std::string TrainerName;
    const std::string TexturePath;
    int TrainerHealth;
    int TrainerDamage;
    float TrainerAtkSpeed;
};

class Game {
  public:
    Game() : Display(VideoMode(720, 1280), "MultiverseCards") {
    	// nothing to see here :/
    }
    
    void Run() {
        while(Display.isOpen()) {
            Event EventListener;
            
            while(Display.pollEvent(EventListener)) {
                if(EventListener.type == Event::Closed) {
                    Display.close();
                }
            }
            
            Display.display();
        }
    }
  private:
    RenderWindow Display;
};

int main() {
    Game MainGame;
    MainGame.Run();
    
    // all the cards and trainers in game
    Trainer T1("Pirate", "../assets/images/trainer/trainer1.png", 720, 111, 1.8f);
    Trainer T2("Thief", "../assets/images/trainer/trainer2.png", 700, 120, 1.5f);
    Card C1("Reaper", "../assets/images/card/card1.png", 444, 96, 1.2f, 2, "Troop", false, false, 70, 4, false);
    Card C2("Indians", "../assets/images/cards/card2.png", 120, 50, 1, 2.1f, "Troop", false, true, 68, 2, false);
    Card C3("Cannon", "../assets/images/cards/card3.png", 390, 70, 1.1f, 0, "Building", false, false, 600, 3, false);
    Card C4("Pelican", "../assets/images/cards/card4.png", 600, 96, 2, 1.8f, "Troop", true, false, 100, 5, true);
    Card C5("Fireball", "../assets/images/cards/card5.png", 0, 150, 1.5f, 0, "Spell", true, true, 0, 4, false);
    Card C6("Eletric Tower", "../assets/images/cards/card6.png", 300, 70, 1.1f, 0, "Building", false, true, 600, 4, false);
    Card C7("Meteore", "../assets/images/cards/card7.png", 0, 300, 5, 0, "Spell", true, true, 0, 6, false);
    Card C8("Titan", "../assets/images/cards/card8.png", 1200, 90, 3, 1, "Troop", false, false, 1024, 8, true);
    Card C9("Samurai", "../assets/images/cards/card9.png", 960, 111, 1.7f, 2, "Troop", false, false, 814, 7, false);
    
    // create a deck
    std::vector<Card> Deck;
    
    // add the cards in deck
    Deck.push_back(T1);
    Deck.push_back(C1);
    Deck.push_back(C2);
    Deck.push_back(C3);
    Deck.push_back(C4);
    Deck.push_back(C5);
    Deck.push_back(C6);
    
    return 0;
}