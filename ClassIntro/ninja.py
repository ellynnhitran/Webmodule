class Ninja:
    #ham tao, constructor
    def __init__(self, n, s, d, h):
        self.name = n
        self.strength = s
        self.defence = d
        self.hp = h
    
    def print(self):
        print(self.name)
        print(self.strength)
        print(self.defence)
        print(self.hp)

    def attack(self, other):
        #self: attacker
        #other: defender
        hp_loss = self.strength - (other.defence/2)
        other.hp -= hp_loss #other.hp = other.hp - hp_loss

ninja1 = Ninja("Kakashi", 7, 9, 10) #n: object

ninja2 = Ninja("Itachi", 4, 10, 10)

ninja1.print()

print("* * "*10)

ninja1.print()

print("Kakashi is attacking Itachi")
ninja1.attack(ninja2)
ninja2.print()