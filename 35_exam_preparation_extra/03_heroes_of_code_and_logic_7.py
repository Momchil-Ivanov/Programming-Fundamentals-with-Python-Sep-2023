number_of_heroes = int(input())

heroes_dict = {}

for x in range(0, number_of_heroes):
    hero_info = input().split()
    hero_name = hero_info[0]
    hero_hp = int(hero_info[1])
    hero_mp = int(hero_info[2])
    if hero_hp > 100:
        hero_hp = 100
    if hero_mp > 200:
        hero_mp = 200
    heroes_dict[hero_name] = {'hp': hero_hp, 'mp': hero_mp}

command = input()

while command != "End":
    command_to_list = command.split(" - ")
    current_command = command_to_list[0]
    current_hero_name = command_to_list[1]

    if current_command == "CastSpell":
        mp_needed = int(command_to_list[2])
        spell_name = command_to_list[3]
        if int(heroes_dict[current_hero_name]['mp']) >= mp_needed:
            heroes_dict[current_hero_name]['mp'] -= mp_needed
            print(f"{current_hero_name} has successfully cast {spell_name} and now has {heroes_dict[current_hero_name]['mp']} MP!")
        else:
            print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")
    elif current_command == "TakeDamage":
        damage = int(command_to_list[2])
        attacker = command_to_list[3]
        heroes_dict[current_hero_name]['hp'] -= damage
        if heroes_dict[current_hero_name]['hp'] > 0:
            print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[current_hero_name]['hp']} HP left!")
        else:
            print(f"{current_hero_name} has been killed by {attacker}!")
            del heroes_dict[current_hero_name]
    elif current_command == "Recharge":
        amount_mp = int(command_to_list[2])
        initial_mp =  heroes_dict[current_hero_name]['mp']
        heroes_dict[current_hero_name]['mp'] += amount_mp
        if heroes_dict[current_hero_name]['mp'] > 200:
            heroes_dict[current_hero_name]['mp'] = 200
        amount_recovered_mp = heroes_dict[current_hero_name]['mp'] - initial_mp
        print(f"{current_hero_name} recharged for {amount_recovered_mp} MP!")
    elif current_command == "Heal":
        amount_hp = int(command_to_list[2])
        initial_hp = heroes_dict[current_hero_name]['hp']
        heroes_dict[current_hero_name]['hp'] += amount_hp
        if heroes_dict[current_hero_name]['hp'] > 100:
            heroes_dict[current_hero_name]['hp'] = 100
        amount_recovered_hp = heroes_dict[current_hero_name]['hp'] - initial_hp
        print(f"{current_hero_name} healed for {amount_recovered_hp} HP!")
    command = input()

for hero, hero_stats in heroes_dict.items():
    print(f"{hero}")
    print(f"  HP: {hero_stats['hp']}")
    print(f"  MP: {hero_stats['mp']}")