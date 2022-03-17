from os import system
from textwrap import dedent

class Hero:

    def __init__(self, name, stamina, intelligence, physical, day, money, job):
        self.name = name
        self.stamina = stamina
        self.intelligence = intelligence
        self.physical = physical
        self.day = day
        self.money = money
        self.job = job

    def lobby(self):
        return dedent(f"""
            1. Check Status
            2. Study
            3. Work Out
            4. Sleep
            5. Exit
        """)

    def getStatus(self):
        return dedent(f"""
            Status kamu :
            Name : {self.name},
            Stamina : {self.stamina},
            Intelligence : {self.intelligence},
            Physical : {self.physical},
            Day : {self.day}
        """)

    def study(self):
        if self.stamina > 10:
            self.intelligence += 5
            self.stamina -= 10
            return (f"\nKamu Belajar, Intelligence kamu naik menjadi {self.intelligence}, sisa stamina kamu {self.stamina}\n")
        else:
            return (f"\nKamu Kecapekan sebaiknya kamu tidur, sisa stamina kamu {self.stamina}\n")
            

    def workOut(self):
        if self.stamina > 10:
            self.physical += 5
            self.stamina -= 10
            return (f"\nKamu Olahraga, physical kamu naik menjadi {self.physical}, sisa stamina kamu {self.stamina}\n")
        else:
            return (f"\nKamu Kecapekan sebaiknya kamu tidur, sisa stamina kamu {self.stamina}\n")

    def sleep(self):
        self.stamina = 100
        self.day += 1
        return (f"\nKamu Tidur, stamina kamu menjadi {self.stamina}, Hari berganti menjadi {self.day}\n")


# Initialize Game
# Input player name
playerName = input("Input your name : ")
# create new player
player = Hero(playerName, 100, 0, 0, 1, 50000, "Pengangguran")
system('cls')

while True:
    print("~"*10 + "Daily Life Game" + "~"*10)
    print(player.lobby())

    choice = input("Masukkan pilihan kamu\t: ")

    try:
        if choice == "1":
            print(player.getStatus())
            system("pause")
            continue
        elif choice == "2":
            print(player.study())
            system("pause")
            continue
        elif choice == "3":
            print(player.workOut())
            system("pause")
            continue
        elif choice == "4":
            print(player.sleep())
            system("pause")
            continue
        elif choice == "5":
            break
        
        
    except:
        print("Input kamu salah!")
        continue


print(f"\nTerima kasih telah bermain {playerName}!\n")
system("pause")
