import random
# Creates a class object with a name, hp, damage
#The class has 3 methods that return the object's attributes

class pyRPG_Char(object):
    def __init__(self, character_name, character_hp, character_damage):
        self.__name = character_name
        self.__hp = int(character_hp)
        self.__damage = int(character_damage)
        self.__xp = 0
        self.__level = 1
        self.__PC = 0
        self.__healRate = 1.1
        self.__nextLevel = 100
        self.__win_potion = 0 # Used in fight() method

    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    def getDamage(self):
        return self.__damage

    def getExp(self):
        return self.__xp

    def getLevel(self):
        return self.__level

    def getNextLevel(self):
        return self.__nextLevel

    def getPotions(self):
        return self.__PC

    def getHealRate(self):
        return self.__heal

    def getScore(self):
        return self.__damage * self.__level * self.__PC * (.1*self.__xp)

    def fight(self, enemy):
        enemy_hp = enemy.getHP()
        while self.__hp > 0 and enemy_hp > 0:
            print('Your HP is ', self.__hp)
            print(enemy.getName(), "'s HP is ", enemy_hp)
            self.__hp -= enemy.getDamage()
            enemy_hp -= enemy.getDamage()
            #print('press ENTER to Continue')
        if self.__hp > 0:
            print('You won!!!')
            self.__xp += enemy.getXP()
            if random.randint(0,1) == 1:

                self.__PC += 1

    def levelUp(self):
        if self.__xp >= self.__nextLevel:
            self.__level +=1
            self.__hp *= 1.5
            self.__healRate *= 1.3
            self.__damage *= 1.3
            self.__nextLevel *= 2
            self.__xp -= self.__xp
            self.__nextLevel *= 2

    def usePotion(self):
        if self.__PC > 0:
            self.__PC -= 1
            self.__hp *= self.__healRate
            self.__hp = round(self.__hp,2)

class enemies(object):
    def __init__(self):

        self.__namelist = ['Cat', 'Bat', 'Wolf', 'Zombie', 'Garble', 'Baserker', 'Rat', 'Bat', 'Creeper']
        self.__name = self.__namelist[random.randint(0,len(self.__namelist)-1)]
        self.__hp = random.randint(1, 101)
        self.__damage = random.randint(0, 11)
        self.__xp = random.randint(0, 101)
        if self.__name == 'Creeper':
            self.__damage *= 2

    def getName(self):
        return self.__name

    def getHP(self):
        return self.__hp

    def getDamage(self):
        return self.__damage

    def getXP(self):
        return self.__xp

#The main function stores character into to lists and calls a the options function
def main():
    character_names = ["Tyler the Mage", "Ben the Archer", "Mrs. Henderson the Warlock", "Mr. Anderson the Warrior",
                       "Josh the Monk", "Nate the Priest"]
    character_hp = [60, 70, 80, 90, 100, 50]
    character_damage = [5, 4, 3, 2, 1, 6]
    options(character_names, character_hp, character_damage)


#This function creates a game loop that allows the user to pick two characters
# and compare the character stats or adventure .
def options(character_names, character_hp, character_damage):
    again = "y"
    menu = [1, 2]
    while again not in menu:
        print("1. Compare 2 characters\n2. Adventure\n3. Quit\n")
        again = input("What would you like to do: ")
        if again == "1":
            compareCharacter(character_names, character_hp, character_damage)
        if again == "2":
            #chosen_character = '~'
            #while chosen_character not in character_names:
            #    count = 0
            #    for character_name in character_names:
            #        count += 1
            #        print(str(count) + ". " + character_name)
            #    choice = int(input("\nChoose A Character: "))-1
            adventure(character_names, character_hp, character_damage)

#This function lets the user compare the stats for two characters
def compareCharacter(character_names, character_hp, character_damage):
    print("Pick 2 characters to compare.")
    count = 0
    for character_name in character_names:
        count += 1
        print(str(count) + ". " + character_name)
    #Let the user pick two characters and subtract 1 to get the index in the lists for those characters
    character1 = int(input("Character 1: ")) - 1
    character2 = int(input("Character 2: ")) - 1

    #Creates instances of the pyRPG class passing in (a name, a hp, a damage)
    character1 = pyRPG_Char(character_names[character1], character_hp[character1], character_damage[character1])
    character2 = pyRPG_Char(character_names[character2], character_hp[character2], character_damage[character2])
    if character1.getHp() > character2.getHp():
        print(character1.getName(), "has ", character1.getHp() - character2.getHp(), " more health than ",
              character2.getName())
    else:
        print(character2.getName(), "has ", character2.getHp() - character1.getHp(), " more health than ",
              character1.getName())
    if character1.getDamage() > character2.getDamage():
        print(character1.getName(), "has ", character1.getDamage() - character2.getDamage(), " more damage than ",
              character2.getName())
    else:
        print(character2.getName(), "has ", character2.getDamage() - character1.getDamage(), " more damage than ",
              character1.getName())


#This function allows the player to pick a character, heal, level up, and fight until the player's
#character runs out of hp
def adventure(character_names, character_hp, character_damage):
    decision_list = ["1", "2", "3"]
    count = 0
    for character_name in character_names:
        count += 1
        print(str(count) + ". " + character_name)
    player = int(input("Character: ")) - 1
    #Creates an instance of the pyRPG class passing in (a name, a hp, a damage)
    player = pyRPG_Char(character_names[player], character_hp[player], character_damage[player])
    while player.getHp() > 0:
        print("\n\nYou have ", player.getHp(), " hp.")
        print("You have ", player.getPotions(), " potions.")
        if player.getNextLevel() > player.getExp():
            morexp = player.getNextLevel() - player.getExp()
            print("You need ", morexp, " more xp to lvl up.\n")
        else:
            print('LEVEl UP NOW!!!')
        print("1. Heal")
        print("2. Level up")
        print("3. Continue through the dungeon")
        player_action = input("What would you like to do next? ")
        while player_action not in decision_list:
            player_action = input("What would you like to do next?")

        if player_action == "1":
            player.usePotion()
        if player_action == "2":
            player.levelUp()
        if player_action == "3":
            enemy = enemies()
            player.fight(enemy)
    print("Game Over! You scored ", player.getScore(), " with ", player.getName())


main()

