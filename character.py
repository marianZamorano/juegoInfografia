import random

class Character:
    def __init__(self, name):
        self.name = name
        self.cls = "Personaje"
        self.max_hp = 100
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.crit_chance = 0.1
        self.ability1_name = "Ninguna"
        self.ability2_name = "Ninguna"
        self.ab1_req = True
        self.ab2_req = False

    def is_alive(self):
        return self.hp > 0

    def basic_attack(self, target):
        damage = max(0, self.attack - target.defense)
        if random.random() < self.crit_chance:
            damage *= 2
            print(f"¡{self.name} golpe crítico!")
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} ataca a {target.name} por {damage} de daño. {target.name} HP: {target.hp}")