from c1 import Character
import random

class asasin (Character):
    def __init__(self ,name,hp, damage, armor):
        Character.__init__(self, name,hp, damage, armor)



def krit(damage):

    kt = random(1, 3)
    if kt==2:
        damage * 2
if asasin.attack:
    krit(damage=self.damage)
    self.damage/2

