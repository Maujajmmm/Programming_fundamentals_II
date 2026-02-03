import random
class character:
    def __init__(self):
        self.type = random.choice(["air_bender", "earth_bender", "fire_bender", "water_bender","avatar","nonbender"])
        if self.type == "air_bender":
            self.attack = random.randint(8,12)
            self.defense = random.randint(3,6)
            self.health = random.randint(1,100)
            self.speed = random.randint(80,99)
        if self.type == "earth_bender":
            self.attack = random.randint( 12,15)
            self.defense = random.randint(5,8)
            self.health = random.randint(1,100)
            self.speed = random.randint(50, 75)
        if self. type == "fire_bender":
            self.attack = random.randint(11,14)
            self.defense = random.randint(4,6)
            self.health = random.randint(1,100)
            self.speed =  random.randint(60,85)
        if self.type == "water_bender":
            self.attack = random.randint(10,15)
            self.defense = random.randint(5,7)
            self.health = random.randint(1,100)
            self.speed = random.randint(70,89)
        if self.type == "avatar":
            self.attack = random.randint(15,20)
            self.defense = random.randint(7,10)
            self.health = random.randint(1,100)
            self.speed = random.randint(90,99)
        if self.type == "nonbender":
            self.attack = random.randint(1, 5)
            self.defense = random.randint(1, 3)
            self.health = random.randint(1,100)
            self.speed = random.randint(30, 50)
        self.level = 1
        self.attack = random.randint(10, 20)
        self.defence = random.randint(5,10)
        self.health = random.randint(1,100)
        self.experience = 0
        self.speed = random.randint(1,99)
    def level_up(self):
        self.level += 1
        self.attack += 2
        self.defence += 1.5
        self.health += 3
        self.experience += 10



