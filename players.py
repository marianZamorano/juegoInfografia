from character import Character
import random

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.cls = "Guerrero"
        self.max_hp = 100
        self.hp = 100
        self.attack = 20
        self.defense = 10
        self.crit_chance = 0.1
        self.ability1_name = "Golpe Poderoso"
        self.ability2_name = "Defender"
        self.ab1_req = True
        self.ab2_req = False

    def ability1(self, target):
        damage = max(0, int(self.attack * 1.5) - target.defense)
        if random.random() < self.crit_chance:
            damage *= 2
            print("¡Crítico!")
        target.hp -= damage
        print(f"Golpe Poderoso por {damage}. {target.name} HP: {target.hp}")

    def ability2(self, target=None):
        self.defense += 5
        print(f"Defender: defensa ahora {self.defense}")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.cls = "Mago"
        self.max_hp = 80
        self.hp = 80
        self.attack = 15
        self.defense = 5
        self.crit_chance = 0.05
        self.ability1_name = "Bola de Fuego"
        self.ability2_name = "Curar"
        self.ab1_req = True
        self.ab2_req = False

    def ability1(self, target):
        damage = max(0, 30 - (target.defense // 2))
        if random.random() < self.crit_chance:
            damage *= 2
            print("¡Crítico!")
        target.hp -= damage
        print(f"Bola de Fuego causa {damage}. {target.name} HP: {target.hp}")

    def ability2(self, target=None):
        heal = 25
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + heal)
        print(f"Curado {self.hp - old_hp}. HP ahora {self.hp}")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.cls = "Arquero"
        self.max_hp = 90
        self.hp = 90
        self.attack = 18
        self.defense = 8
        self.crit_chance = 0.2
        self.ability1_name = "Disparo Preciso"
        self.ability2_name = "Esquivar"
        self.ab1_req = True
        self.ab2_req = False

    def ability1(self, target):
        crit = self.crit_chance + 0.2
        damage = max(0, self.attack - target.defense)
        if random.random() < crit:
            damage *= 2
            print("¡Golpe crítico!")
        target.hp -= damage
        print(f"Disparo Preciso causa {damage}. {target.name} HP: {target.hp}")

    def ability2(self, target=None):
        self.defense += 5
        print(f"Esquivar: defensa ahora {self.defense}")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name)
        self.cls = "Terrorista"
        self.max_hp = 85
        self.hp = 85
        self.attack = 22
        self.defense = 7
        self.crit_chance = 0.25
        self.ability1_name = "Puñalada Traposa"
        self.ability2_name = "Robar Ataque"
        self.ab1_req = True
        self.ab2_req = True

    def ability1(self, target):
        crit = self.crit_chance + 0.1
        damage = max(0, int(self.attack * 1.5) - target.defense)
        if random.random() < crit:
            damage *= 2
            print("¡Crítico!")
        target.hp -= damage
        print(f"Puñalada Traposa causa {damage}. {target.name} HP: {target.hp}")

    def ability2(self, target):
        steal = 5
        actual_steal = min(steal, target.attack)
        target.attack -= actual_steal
        self.attack += actual_steal
        print(f"Robó {actual_steal} de ataque de {target.name}. Tu ataque: {self.attack}, el suyo: {target.attack}")