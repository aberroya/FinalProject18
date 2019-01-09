import random

class Fighter:
    def __init__(self,name, hp, atk, defense, accuracy, attacks, weapon):
        self.name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon

class Wizard(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon, mana):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon
        self.mana = mana

class Berserker(Fighter):
    def __init__(self,name, hp, atk, defense, accuracy, attacks, weapon, rage_level):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon
        self.rage_level = rage_level

class Paladin(Fighter):
    def __init__(self,name, hp, atk, defense, accuracy, attacks, weapon, blade_sharpness):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon
        self.blade_sharpness = blade_sharpness


phys = Berserker('Physics Himself','5000','500','50','50',['test fail','centripetal force','free body kick'],'mega spring','100')
wah = Paladin('Waluigi','700','100','25','75',['WAH','Luigi Disguise','M E G A  W A H'],'pointy tennis racket','80')
dd = Wizard('Danny DeVito','250','300','75','25',['Confusion','Astonishment','Wonder'],'the scepter of truth','75')


def showstatus (self):
    """display stats of opponent"""
    print (f"{self.name}:")
    print(f"- HP: {self.hp}")
    print (f" - Attack: {self.atk}")
    print (f" - Defense: {self.defense}")
    print (f" - Accuracy: {self.accuracy}")
    print (f" - Attacks: {self.attack}")
    print (f" - Weapon: {self.weapon}")

def showspecial (self):
    if choice == 'Paladin':
        print (f" The special stat for this Fighter is blade sharpness. Blade Sharpness: Unfortunately {self.blade_sharpness}")
    elif choice == 'Berserker':
        print (f" The special stat for this Fighter is S H E E R  R A G E. Rage: Unfortunately {self.rage_level}")
    elif choice == 'Wizard':
        print (f" The special stat for this Fighter is mana. Mana: Unfortunately {self.mana}")


def fight (self):
    assailants = [phys, wah, dd]
    opp = random.choice(assailants)
    print ("you have encountered",opp,"!")
    FightChoice = input("Will you proceed to battle?")


print ("Welcome Young One, To The Battle Royale Of The Century.")
playername = input("What Is The Name That Has Been Bestowed Upon You?")
print (f"{playername}, I Hope You Are Prepared For Battle.")
choice = input("You have the choice to battle a Berserker, Paladin, or Wizard. Which stats would you like to see?")
showstatus(choice)
showspecial(choice)

