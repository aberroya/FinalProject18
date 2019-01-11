import random

class Fighter:
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon

    def __str__(self):
        return self.name

    __repr__ = __str__

    def showspecial (self):
        if choice == 'Paladin':
            print (f" The special stat for this Fighter is blade sharpness. Blade Sharpness: Unfortunately {self.blade_sharpness}")
        elif choice == 'Berserker':
            print (f" The special stat for this Fighter is S H E E R  R A G E. Rage: Unfortunately {self.rage_level}")
        elif choice == 'Wizard':
            print (f" The special stat for this Fighter is mana. Mana: Unfortunately {self.mana}")

    def fight (self):
        assailants = [Paladin, Berserker, Wizard]
        opp = random.choice(assailants)
        print ("you have encountered",opp,"!")
        FightChoice = input("Will you proceed to battle?")
        if FightChoice == ('yes'):
            print ("You have encountered",opp,"! Good Luck. You Will Need Copious Amounts Of It.")
            opp.hp -= player.atk
            showoppstatus()
            playerhealth -= opp.atk
            winorlose()

class Wizard(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon, mana):
        Fighter.__init__(self, name, hp, atk, defense, accuracy, attacks, weapon)
        self.mana = mana

    def showoppstatus (self):
        """display stats of opponent"""
        print (f"{self.name}:")
        print(f"- HP: {self.hp}")
        print (f" - Attack: {self.atk}")
        print (f" - Defense: {self.defense}")
        print (f" - Accuracy: {self.accuracy}")
        print (f" - Attacks: {self.attacks}")
        print (f" - Weapon: {self.weapon}")


class Berserker(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon, rage_level):
        Fighter.__init__(self, name, hp, atk, defense, accuracy, attacks, weapon)
        self.rage_level = rage_level

    def showoppstatus (self):
        """display stats of opponent"""
        print (f"{self.name}:")
        print(f"- HP: {self.hp}")
        print (f" - Attack: {self.atk}")
        print (f" - Defense: {self.defense}")
        print (f" - Accuracy: {self.accuracy}")
        print (f" - Attacks: {self.attacks}")
        print (f" - Weapon: {self.weapon}")


class Paladin(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon, blade_sharpness):
        Fighter.__init__(self, name, hp, atk, defense, accuracy, attacks, weapon)
        self.blade_sharpness = blade_sharpness

    def showoppstatus (self):
        """display stats of opponent"""
        print (f"{self.name}:")
        print(f"- HP: {self.hp}")
        print (f" - Attack: {self.atk}")
        print (f" - Defense: {self.defense}")
        print (f" - Accuracy: {self.accuracy}")
        print (f" - Attacks: {self.attacks}")
        print (f" - Weapon: {self.weapon}")


Berserker = Berserker('Physics Himself','5000','500','50','50',['test fail','centripetal force','free body kick'],'mega spring','100')
Paladin = Paladin('Waluigi','700','100','25','75',['WAH','Luigi Disguise','M E G A  W A H'],'pointy tennis racket','80')
Wizard = Wizard('Danny DeVito','250','300','75','25',['Confusion','Astonishment','Wonder'],'the scepter of truth','75')

winmessages: ['You made it this far? Not for long. Proceed.', 'Turn your hacks off we know youre cheating if you survived that','VICTORY ROYALE! NEXT BATTLE, GAMER.']




def showstatus(self):
    print (f"Your hp is at a low, low {playerhealth}")

def winorlose(self):
    if playerhealth <= 0:
        print ("You unfortunately did not make enough power moves to survive. GAME OVER :(")
    elif playerhealth > 0:
        print (random.choice(winmessages))
        showstatus()
        fight()

def fight (self):
    assailants = [phys, wah, dd]
    opp = random.choice(assailants)
    print ("you have encountered",opp,"!")
    print()
    FightChoice = input("Will you proceed to battle?")
    print()
    if FightChoice == yes:
        print ("You have encountered",opp,"! Good Luck. You Will Need Copious Amounts Of It.")
        opp.hp -= player.atk
        showoppstatus()
        playerhealth -= opp.atk
        winorlose()

opponents = [Berserker, Paladin, Wizard]


print ("Welcome Young One, To The Battle Royale Of The Century.")
print ()
playername = input("What Is The Name That Has Been Bestowed Upon You?")
print ()
playerhealth = 500
print (f"{playername}, I Hope You Are Prepared For Battle.")
print()
choice = input("You have the choice to battle a Berserker, Paladin, or Wizard. Which stats would you like to see?")
if choice == ('Paladin'):
    Paladin.showoppstatus()
elif choice == ('Berserker'):
    Berserker.showoppstatus()
elif choice == ('Wizard'):
    Wizard.showoppstatus()

opp = random.choice(opponents)
if opp == Paladin:
    Paladin.showoppstatus()
elif opp == Berserker:
    Berserker.showoppstatus()
elif choice == Wizard:
    Wizard.showoppstatus()
opp.fight()


