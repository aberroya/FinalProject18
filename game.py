import random

class Fighter:
    def __init__(self,name, hp, atk, defense, accuracy, attacks, weapon):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon

class Wizard(Fighter):
    def __init__(self,name, hp, atk, defense, accuracy, attacks, weapon, mana):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon
        self.mana = mana

class Berserker(Fighter):
    def __init__(self,name, hp, atk, defense, accuracy, attacks, weapon, rage_level):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.accuracy = accuracy
        self.attacks = attacks
        self.weapon = weapon
        self.rage_level = rage_level

class Paladin(Fighter):
    def __init__(self,name, hp, atk, defense, accuracy, attacks, weapon, blade_sharpness):
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

assailants = [phys, wah, dd]

 def showstatus (self):
    """display stats of opponent"""
    print (f"{self.name}:")
    print(f"- HP: {self.hp}")
    print (f" - Attack: {self.atk}")
    print (f" - Defense: {self.defense}")
    print (f" - Accuracy: {self.accuracy}")
    print (f" - Attacks: {self.attack}
    print (f" -

def fight(self):
    random.choice(assailants) = opp
    print ("you have encountered",opp,"!")
    FightChoice = input("Will you proceed to battle?")
    if FightChoice == yes:


