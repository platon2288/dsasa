from c1 import Character
from c2 import Berserk
from c3 import hil

p1 = Berserk(name='Berserk', hp=100, damage=8, armor=0)
p2 = Paladin(name='Paladin', hp=100, damage=10, armor=0)

while p1.hp > 0 and p2.hp > 0:
    print(p1)
    print(p2)
    p1.attack(p2)
    p2.attack(p1)
    print()
