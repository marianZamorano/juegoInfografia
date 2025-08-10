from character import Character

def select_action(current, players):
    print(f"\nTurno de {current.name}.")
    print("Acciones:\n1: Ataque Básico\n2: " + current.ability1_name + "\n3: " + current.ability2_name)
    action = input("Elige acción (1-3): ")
    while action not in ['1', '2', '3']:
        action = input("Inválido. Elige 1-3: ")
    if action == '1':
        return True, current.basic_attack
    elif action == '2':
        return current.ab1_req, current.ability1
    return current.ab2_req, current.ability2

def select_target(current, players):
    alive_enemies = [p for p in players if p != current and p.is_alive()]
    if not alive_enemies:
        print("No hay más enemigos.")
        return None
    print("Selecciona objetivo:")
    for idx, enemy in enumerate(alive_enemies, 1):
        print(f"{idx}: {enemy.name} HP {enemy.hp}")
    t_choice = int(input("Elige: "))
    while t_choice < 1 or t_choice > len(alive_enemies):
        t_choice = int(input("Inválido: "))
    return alive_enemies[t_choice - 1]