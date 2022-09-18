import random
from c1 import Character
class hil (Character):
    def __init__(self ,name,hp, damage, armor):
        Character.__init__(self, name,hp, damage, armor)

    def hil(self):
        if attack:
            hilp=random.randint(1.100)
            if hilp>=70:
                hils=self.damage*2
                self.hp+=hils
                self.damage/2