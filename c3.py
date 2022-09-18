from c1 import Character
class hil (Character):
    def __init__(self ,name,hp, damage, armor):
        Character.__init__(self, name,hp, damage, armor)

    def hil(self, hp, attack):
        if attack:
            hilp=self.damage*2
            hp+=hilp
            self.damage/2

