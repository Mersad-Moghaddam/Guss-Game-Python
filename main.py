import os
import random


class Gamer:
    def __init__(self, name, Gid, score):
        self.guss = None
        self.name = name
        self.id = Gid
        self.score = score

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def setScore(self, score):
        self.score = score

    def setGuss(self, guss):
        self.guss = guss

    def getGuss(self):
        return self.guss

    def addScore(self, new_score):
        self.score += new_score

    def getscore(self):
        return f"Score is ={self.score}"

    def __str__(self):
        return f"Name = {self.name}\t\tID = {self.id}\t\tScore is ={self.score}"


os.system("clear")
name1 = input("Name of First Player : ")
id1 = int(input("ID of First Player : "))
name2 = input("Name of Second Player : ")
id2 = int(input("ID of Second Player : "))
Player1 = Gamer(name1, id1, 0)
Player2 = Gamer(name2, id2, 0)
os.system("clear")
number_participant = random.randint(1, 2)
# print(f"Game Number {number_participant} Start")
# print(number_participant)
key = 1
while key:
    for i in range(5):
        number_game = random.randint(1, 10)
        guss1 = int(input(" Guss Player1: "))
        Player1.setGuss(guss1)
        guss2 = int(input(" Guss Player2: "))
        Player2.setGuss(guss2)
        # print("Check 1")
        if number_game == guss1 and number_game == guss2:
            Player1.addScore(1)
            Player2.addScore(1)
            print("Equal")
        elif number_game == guss1:
            Player1.addScore(1)
            print("Player 1 Right Guss")
        elif number_game == guss2:
            Player2.addScore(1)
            print("Player 2 Right Guss")
        print(f"Number You've Guessed were : {number_game}")
    wait = input("Press Enter to See Result...")
    os.system("clear")
    print(Player1)
    print(Player2)
    if Player1.getscore() > Player2.getscore():
        print(f"Winner is {Player1.getName()}")
    if Player1.getscore() < Player2.getscore():
        print(f"Winner is --->{Player2.getName()}")
    else:
        print("The scores are equal!")
    wait = input("Press Enter to continue...")
    os.system("clear")
    key = int(input("Enter 0 to Exit / 1 to continue : "))
    Player1.setScore(0)
    Player2.setScore(0)
    os.system("clear")
