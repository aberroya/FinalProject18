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
        """ shows the special stat of the opponent Fighters!"""
        if choice == 'Paladin':
            print (f" The special stat for this Fighter is blade sharpness. Blade Sharpness: Unfortunately {self.blade_sharpness}")
        elif choice == 'Berserker':
            print (f" The special stat for this Fighter is S H E E R  R A G E. Rage: Unfortunately {self.rage_level}")
        elif choice == 'Wizard':
            print (f" The special stat for this Fighter is mana. Mana: Unfortunately {self.mana}")

    def showoppstatus (self):
        """display stats of opponent"""
        print (f"{self.name}:")
        print(f"- HP: {self.hp}")
        print (f" - ΛƬƬΛᄃK: {self.atk}")
        print (f" - DΣFΣПƧΣ: {self.defense}")
        print (f" - ΛᄃᄃЦЯΛᄃY: {self.accuracy}")
        print (f" - ΛƬƬΛᄃKƧ: {self.attacks}")
        print (f" - ЩΣΛPӨП: {self.weapon}")

    def fight (self,opp):
        """ epic fight scenes; basic subtraction of health points and the announcement of opponents!"""
        assailants = [Paladin, Berserker, Wizard]
        opp = random.choice(opponents)
        specialatk = random.choice(opp.attacks)
        opp.atk -= Player.defense
        oppdestruction = opp.atk
        print ("you have encountered",opp,"!")
        FightChoice = input("Will you proceed to battle?")
        if FightChoice == ('yes'):
            print()
            print ("You have encountered",opp,"! Good Luck. You Will Need Copious Amounts Of It.")
            print()
            print (opp,"has attempted to D E S T R O Y you with",specialatk,".")
            print()
            opp.hp -= Player.atk
            opp.showoppstatus()
            Player.hp -= oppdestruction
            winorlose(self)
        elif FightChoice == ('no'):
            print ('well this is awkward...youre going to play anyway.')
            opp = random.choice(assailants)
            print()
            print ("You have encountered",opp,"! Good Luck. You Will Need Copious Amounts Of It.")
            print()
            print (opp,"has attempted to D E S T R O Y you with",specialatk,".")
            print()
            opp.hp -= Player.atk
            opp.showoppstatus()
            opp.showspecial()
            Player.hp -= opp.atk
            winorlose(self)

class Player(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon):
        Fighter.__init__(self, name, hp, atk, defense, accuracy, attacks, weapon)


class Wizard(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon, mana):
        Fighter.__init__(self, name, hp, atk, defense, accuracy, attacks, weapon)
        self.mana = mana


class Berserker(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon, rage_level):
        Fighter.__init__(self, name, hp, atk, defense, accuracy, attacks, weapon)
        self.rage_level = rage_level

    def showoppstatus (self):
        """display stats of opponent"""
        print (f"{self.name}:")
        print(f"- HP: {self.hp}")
        print (f" - ΛƬƬΛᄃK: {self.atk}")
        print (f" - DΣFΣПƧΣ: {self.defense}")
        print (f" - ΛᄃᄃЦЯΛᄃY: {self.accuracy}")
        print (f" - ΛƬƬΛᄃKƧ: {self.attacks}")
        print (f" - ЩΣΛPӨП: {self.weapon}")


class Paladin(Fighter):
    def __init__(self, name, hp, atk, defense, accuracy, attacks, weapon, blade_sharpness):
        Fighter.__init__(self, name, hp, atk, defense, accuracy, attacks, weapon)
        self.blade_sharpness = blade_sharpness

    def showoppstatus (self):
        """display stats of opponent"""
        print (f"{self.name}:")
        print(f"- HP: {self.hp}")
        print (f" - ΛƬƬΛᄃK: {self.atk}")
        print (f" - DΣFΣПƧΣ: {self.defense}")
        print (f" - ΛᄃᄃЦЯΛᄃY: {self.accuracy}")
        print (f" - ΛƬƬΛᄃKƧ: {self.attacks}")
        print (f" - ЩΣΛPӨП: {self.weapon}")

### the stats of the opponents and the player

Player = Player('the girl reading this uwu',300,50,50,'hundred',['totally normal punch','student loans','osmosis'],'left toe')
Berserker = Berserker('Physics Himself',5000,200,50,'fifty',['test fail','centripetal force','free body kick'],'mega spring',100)
Paladin = Paladin('Waluigi',700,100,25,'seventyfive',['WAH','Luigi Disguise','M E G A  W A H'],'pointy tennis racket',80)
Wizard = Wizard('Danny DeVito',150,300,75,'twentyfive',['Confusion','Astonishment','Wonder'],'the scepter of truth',75)

### list of various win messages that are displayed when you win one fight
winmessages = ['You made it this far? Not for long. Proceed.', 'Turn your hacks off we know youre cheating if you survived that','VICTORY ROYALE! NEXT BATTLE, GAMER.']

class ItemDrops:
    def __init__(self, name, hp_add, atk_add, defense_add, attacks):
        self.name = name
        self.hp_add = hp_add
        self.atk_add = atk_add
        self.defense_add = defense_add
        self.attacks = attacks

    def winorlose(self):
        """ what happens when the Player's health drops below zero or stays above zero"""
        global HPBooster
        global DefBooster
        global AttackBooster
        if Player.hp <= 0:
            print ("You unfortunately did not make enough power moves to survive. GAME OVER :(")
        elif Player.hp > 0:
            print (random.choice(winmessages))
            if opp == Paladin:
                print()
                print ("You have S L I P P E D  O F F ",AttackBooster.name,"! congrats i guess")
                Player.atk += AttackBooster.atk_add
                print("atk +",AttackBooster.atk_add,"!!")
                print()
            elif opp == Wizard:
                print()
                print ("You have P U R L O I N E D ",HPBooster.name,"! wow! poor trash man :(")
                Player.hp += HPBooster.hp_add
                print ("hp +",HPBooster.hp_add,"!")
                print()
            elif opp == Berserker:
                print()
                print ("How did you defeat Physics Himself lol can you give me those cheat codes for real life buddy man")
                print()
                print ("Anyway,",DefBooster.name,"has been B E S T O W E D upon you.")
                Player.defense += DefBooster.defense_add
                print ("defense +",DefBooster.defense_add,"!")
                print()
            for n in range(2):
                showstatus(self)
                opp.fight(opp)

### defining the various boosts the Player can receive from defeating opponents
class AttackBooster(ItemDrops):
    def __init__(self, name, hp_add, atk_add, defense_add, attacks):
        self.name = name
        self.hp_add = hp_add
        self.atk_add = atk_add
        self.defense_add = defense_add
        self.attacks = attacks

class HPBooster(ItemDrops):
    def __init__(self, name, hp_add, atk_add, defense_add, attacks):
        self.name = name
        self.hp_add = hp_add
        self.atk_add = atk_add
        self.defense_add = defense_add
        self.attacks = attacks

class DefBooster(ItemDrops):
    def __init__(self, name, hp_add, atk_add, defense_add, attacks):
        self.name = name
        self.hp_add = hp_add
        self.atk_add = atk_add
        self.defense_add = defense_add
        self.attacks = attacks

AttackBooster = AttackBooster("Waluigi's Left Shoe!!!!!",0,50,0,['WAH KICK','MEGA WAH KICK','The Spirit Of Luigi'])
DefBooster = DefBooster("Physics Degree",0,0,30,['MAX MOMENTUM','9999 AMPS OF POWER','INSTAFAIL'])
HPBooster = HPBooster("Timeless Meme Essence",10,0,0,['Internet Control','Fan Club Hive Mind','Might of the Garbage Man'])


def showstatus(self):
    """ shows the player how many health points they have"""
    print()
    print (f"Your hp is at a low, low {Player.hp}")
    print()

def winorlose(self):
    """ what happens when the Player's health drops below zero or stays above zero"""
    global HPBooster
    global DefBooster
    global AttackBooster
    playatk = random.choice(Player.attacks)
    if Player.hp <= 0:
        print ("You unfortunately did not make enough power moves to survive. GAME OVER :(")
    elif Player.hp > 0:
        print (random.choice(winmessages))
        if opp == Paladin:
            print()
            print ("You have S L I P P E D  O F F ",AttackBooster.name,"! congrats i guess")
            Player.atk += AttackBooster.atk_add
            addedatk = random.choice(AttackBooster.attacks)
            print("atk +",AttackBooster.atk_add,"!!")
            print()
            print ("You will now attack with the force of",playatk,"and",addedatk,"!")
        elif opp == Wizard:
            print()
            print ("You have P U R L O I N E D ",HPBooster.name,"! wow! poor trash man :(")
            Player.hp += HPBooster.hp_add
            addedhp = random.choice(HPBooster.attacks)
            print ("hp +",HPBooster.hp_add,"!")
            print()
            print("Your HP has been boosted by",addedhp,"!")
        elif opp == Berserker:
            print()
            print ("How did you defeat Physics Himself lol can you give me those cheat codes for real life buddy man")
            print()
            print ("Anyway,",DefBooster.name,"has been B E S T O W E D upon you.")
            Player.defense += DefBooster.defense_add
            addeddef = random.choice(DefBooster.attacks)
            print ("defense +",DefBooster.defense_add,"!")
            print()
            print("Your defense has been boosted with the power of",addeddef,"!")
        showstatus(self)
        opp.fight(opp)


opponents = [Berserker, Paladin, Wizard]


print ("Welcome Young One, To The вαттℓє яσуαℓє σƒ тнє ¢єηтυяу. You will keep battling until you can no longer continue. After these trials you will evolve into a  𝙥𝙧𝙚𝙩𝙩𝙮 𝙢𝙚𝙙𝙞𝙤𝙘𝙧𝙚 𝙛𝙞𝙜𝙝𝙩𝙚𝙧 𝙞 𝙜𝙪𝙚𝙨𝙨")
print ()
playername = input("What Is The Name That Has Been Bestowed Upon You?")
print ()
print (f"{playername}, I Hope You Are Prepared For Battle.")
print()

### lets the player choose whose stats they want to see
choice = input("You have the choice to battle a ᏰᏋᏒᏕᏋᏒᏦᏋᏒ,  ℘ąƖąɖın, or ຟiຊคr໓. Which stats would you like to see?")
if choice == ('Paladin'):
    Paladin.showoppstatus()
    Paladin.showspecial()
elif choice == ('Berserker'):
    Berserker.showoppstatus()
    Berserker.showspecial()
elif choice == ('Wizard'):
    Wizard.showoppstatus()
    Wizard.showspecial()
else:
    choice = input("please choose your fighter.")
    if choice == ('Paladin'):
        Paladin.showoppstatus()
        Paladin.showspecial()
    elif choice == ('Berserker'):
        Berserker.showoppstatus()
        Berserker.showspecial()
    elif choice == ('Wizard'):
        Wizard.showoppstatus()
        Wizard.showspecial()
print()
print("No matter what you know, there will always be a surprise. You cannot choose who you fight in this realm, but you can gather knowledge as you progress.")
print()
opp = random.choice(opponents)
###the opponent is randomized anyway

opp.fight(opp)


