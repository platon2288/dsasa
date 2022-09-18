from c1 import Character
from c2 import bers


player1 = Character(name='Vasya', hp=100, damage=10, armor=0)
player2 = bers(name='Petya', hp=200, damage=7, armor=0)
print(player1)
print(player2)

while player1.hp==0 or player2.hp==0:
    player1.attack(player2)
    player2.attack(player1)
    print(player1)
    print(player2)
    print()