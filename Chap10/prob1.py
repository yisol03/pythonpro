class Player:
    def blast(self, enemy):
        print ("The player blasts an enemy.")
        enemy.die()

class Alien:
    def die(self):
        print ("Good-bye, cruel universe.")

hero = Player()
invader = Alien()
hero.blast(invader)
