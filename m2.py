from Lesson_1.Character import Character

class bers (Character):
    def __init__(self ,name,hp, damage, armor):
        Character.__init__(self, name,hp, damage, armor)

    def dem20(self):
        return (self.max_hp - self.hp) / self.max_hp* self.damege
