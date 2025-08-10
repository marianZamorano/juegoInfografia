import random
from players import Warrior, Mage, Archer, Rogue
from actions import select_action, select_target

def setup_players():
    num_players = 0
    while num_players < 2 or num_players > 4:
        num_players = int(input("Ingresa número de jugadores (2-4): "))
    max_rounds = int(input("Ingresa número máximo de rondas: "))
    players = []
    class_choices = {'1': Warrior, '2': Mage, '3': Archer, '4': Rogue}
    for i in range(num_players):
        name = input(f"Jugador {i+1}, ingresa tu nombre: ")
        print("Elige clase:\n1. Guerrero\n2. Mago\n3. Arquero\n4. Terrorista")
        cls_id = input()
        while cls_id not in class_choices:
            cls_id = input("Inválido. Elige 1-4: ")
        char_class = class_choices[cls_id]
        players.append(char_class(name))
    return players, max_rounds

def display_status(players):
    print("\nEstado actual:")
    for p in players:
        print(f"{p.name} ({p.cls}): HP {p.hp}/{p.max_hp}, Ataque {p.attack}, Defensa {p.defense}, Crítico {p.crit_chance}")

def determine_winner(players, max_rounds, round_num):
    alive_players = [p for p in players if p.is_alive()]
    if len(alive_players) <= 1:
        if alive_players:
            print(f"\n¡{alive_players[0].name} gana!")
        else:
            print("\n¡Todos muertos! Empate!")
        return True
    if round_num >= max_rounds:
        if len(alive_players) > 1:
            winner = max(alive_players, key=lambda p: p.hp / p.max_hp)
            print(f"\nRondas máximas alcanzadas. ¡{winner.name} gana con mayor HP!")
        else:
            print(f"\n¡{alive_players[0].name} gana!")
        return True
    return False

def run_game():
    players, max_rounds = setup_players()
    turn_order = players[:]
    random.shuffle(turn_order)
    print("Orden de turnos:")
    for p in turn_order:
        print(p.name)
    round_num = 0
    while round_num < max_rounds:
        round_num += 1
        print(f"\nRonda {round_num}")
        for current in turn_order:
            if not current.is_alive():
                continue
            display_status(players)
            req_target, action_func = select_action(current, players)
            target = select_target(current, players) if req_target else None
            if target is None and req_target:
                break
            action_func(target)
            if determine_winner(players, max_rounds, round_num):
                return