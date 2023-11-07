/**
 * code by MegaGamer69(me)
 * credits to Supercell :)
**/

// include the SFML basics
#include "../SFML/Window.hpp"
#include "../SFML/System.hpp"
#include "../SFML/Graphics.hpp"

// include the CURL basics
#include "../CURL/curl.h"

// include the STD lib
#include <string>
#include <iostream>
#include <vector>

class Energy {
  public:
    Energy();
    
    int EnergyAmount;
    
    void UseEnergy(int Amount) {
        if(EnergyAmount > 0) {
            EnergyAmount -= Amount;
        }
    }
    
    void AddEnergy() {
        if(EnergyAmount < 10) {
            EnergyAmount++;
        }
    }
  private:
    float Timer;
};

class Card {
  public:
    Card();
    
    void setStatus(std::string Name, std::string Texture, int Health, int Damage, float AttackSpeed, float MoveSpeed, std::string Type, bool Flying, bool AtkAirAlso, int Mass, int Cost, bool AtkOnlyBuild, float AtkRange, int HealEffect) {
        CardName = Name;
        CardTexture = Texture;
        CardHealth = Health;
        CardDamage = Damage;
        CardAttackSpeed = AttackSpeed;
        CardMoveSpeed = MoveSpeed;
        CardType = Type;
        FlyingCard = Flying;
        CarxAtkAirAlso = AtkAirAlso;
        CardMass = Mass;
        CardCost = Cost;
        AtkOnlyBuildings = AtkOnlyBuild;
        CardAtkRange = AtkRange;
        CardHealEffect = HealEffect;
    }
    
    void Deploy() {
        EnergyInstancie.UseEnergy(CardCost);
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
    float CardAtkRange;
    int CardHealEffect;
    
    Energy EnergyInstancie;
    
    // amogus HAHA
    sf::Texture TextureLOL;
};

// trainers is the most important on game, if your trainer has been defeated, game over
class Trainer {
  public:
    Trainer();
    
    void setStatus(std::string Name, std::string Texture, int Health, int Damage, float AtkSpeed, float AtkRange) {
        TrainerName = Name;
        TexturePath = Texture;
        TrainerHealth = Health;
        TrainerDamage = Damage;
        TrainerAtkSpeed = AtkSpeed;
        TrainerAtkRange = AtkRange;
    }
    
    void ReceiveDamage(int Damage) {
        TrainerHealth -= Damage;
    }
    
    void CheckHP() {
        if(TrainerHealth <= 0) {
           std::cout << "Trainer has been defeated" <<std::endl;
        }
    }
    
  private:
    std::string TrainerName;
    std::string TexturePath;
    int TrainerHealth;
    int TrainerDamage;
    float TrainerAtkSpeed;
    float TrainerAtkRange;
};

int main() {
    // all the cards and trainers in game
    Trainer T1;
    T1.setStatus("Pirate", "../assets/images/trainer/trainer1.png", 720, 111, 1.8f, 1.5f);
    Trainer T2;
    T2.setStatus("Thief", "../assets/images/trainer/trainer2.png", 700, 120, 1.5f, 6.5f);
    Trainer T3;
    T3.setStatus("Master", "../assets/images/trainer/trainer3.png", 880, 80, 1.7f, 4);
    Card C1;
    C1.setStatus("Reaper", "../assets/images/card/card1.png", 444, 96, 1.2f, 2, "Troop", false, false, 70, 4, false, 1.25f, 0);
    Card C2;
    C2.setStatus("Indians", "../assets/images/cards/card2.png", 120, 50, 1, 2.1f, "Troop", false, true, 68, 2, false, 4.5f, 0);
    Card C3;
    C3.setStatus("Cannon", "../assets/images/cards/card3.png", 390, 70, 1.1f, 0, "Building", false, false, 600, 3, false, 4.75f, 0);
    Card C4;
    C4.setStatus("Pelican", "../assets/images/cards/card4.png", 600, 96, 2, 1.8f, "Troop", true, false, 100, 5, true, 1, 0);
    Card C5;
    C5.setStatus("Fireball", "../assets/images/cards/card5.png", 0, 150, 1.5f, 0, "Spell", true, true, 0, 4, false, 2.5f, 0);
    Card C6;
    C6.setStatus("Eletric Tower", "../assets/images/cards/card6.png", 300, 70, 1.1f, 0, "Building", false, true, 600, 4, false, 5.5f, 0);
    Card C7;
    C7.setStatus("Meteore", "../assets/images/cards/card7.png", 0, 300, 5, 0, "Spell", true, true, 0, 6, false, 4, 0);
    Card C8;
    C8.setStatus("Titan", "../assets/images/cards/card8.png", 1200, 90, 3, 1, "Troop", false, false, 1024, 8, true, 1, 0);
    Card C9;
    C9.setStatus("Samurai", "../assets/images/cards/card9.png", 960, 111, 1.7f, 2, "Troop", false, false, 128, 7, false, 1.25f, 0);
    Card C10;
    C10.setStatus("Bomb Man", "../assets/images/cards/card10.png", 222, 97, 1, 4, "Troop", false, false, 60, 3, true, 0.75f, 0);
    Card C11;
    C11.setStatus("Terrorist", "../assets/images/cards/card11.png", 660, 74, 1.1f, 2, "Troop", false, true, 70, 4, false, 1, 0);
    Card C12;
    C12.setStatus("Heal", "../assets/images/cards/card12.png", 0, 0, 1, 0, "Spell", false, false, 0, 3, false, 4, 50);
    
    sf::Window Display;
    Display.create(sf::VideoMode(720, 1280, 32), "Multiverse Cards");
    
    while(Display.isOpen()) {
        sf::Event Listener;
        
        while(Display.pollEvent(Listener)) {
            if(Listener.type == sf::Event::Closed) {
                Display.close();
            }
        }
        
        Display.display();
    }
    
    // create a deck
    std::vector<Card> Deck;
    std::vector<Trainer> PlayableTrainer;
    
    // add the cards in deck
    Deck.push_back(C1);
    Deck.push_back(C2);
    Deck.push_back(C3);
    Deck.push_back(C4);
    Deck.push_back(C5);
    Deck.push_back(C6);
    
    // add just one trainer
    PlayableTrainer.push_back(T1);
    
    return 0;
}