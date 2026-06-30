from list_ import List
from super_heroes_data import superheroes
from queue_ import Queue
from copy import deepcopy


def heroes_to_list(superheroes):
    hero_list = List()
    for hero in superheroes:
        hero_list.append(hero)
    return hero_list


hero_list = heroes_to_list(superheroes)


def crit_name(hero):
    return hero['name']


hero_list.add_criterion('name', crit_name)

hero_list.sort_by_criterion('name')

print("________________________________________________")

print("Chars sorted by name:")
for hero in hero_list:
    print(hero['name'])

print("________________________________________________")

thing_pos = hero_list.search('The Thing', 'name')
if thing_pos is not None:
    print(f'The Thing is at pos: {thing_pos}')
else:
    print('The Thing not in list')

print("________________________________________________")

raccoon_pos = hero_list.search('Rocket Raccoon', 'name')
if raccoon_pos is not None:
    print(f'Rocket Raccoon is at pos: {raccoon_pos}')
else:
    print('Rocket Raccoon not in list')

print("________________________________________________")

print("Villains:")
for hero in hero_list:
    if hero.get('is_villain') == True:
        print(hero['name'])

print("________________________________________________")


def queue_villains(hero_list):
    vil_queue = Queue()
    for hero in hero_list:
        if hero.get('is_villain') == True:
            vil_queue.arrive(hero)
    return vil_queue


vil_queue = queue_villains(hero_list)


def vils_before_1980(vil_queue):
    while vil_queue.size() > 0:
        vil = vil_queue.attention()
        if vil.get('first_appearance') and int(vil['first_appearance']) < 1980:
            print(vil['name'])


print("Villains before 1980:")
vils_before_1980(vil_queue)

print("________________________________________________")


def heroes_start_Bl(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][:2] == 'Bl') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No heroes starting with Bl found")


print("Heroes starting with Bl:")
heroes_start_Bl(hero_list)

print()


def heroes_start_G(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][0] == 'G') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No heroes starting with G found")


print("Heroes starting with G:")
heroes_start_G(hero_list)

print()


def heroes_start_My(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][:2] == 'My') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No heroes starting with My found")


print("Heroes starting with My:")
heroes_start_My(hero_list)

print()


def heroes_start_W(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][0] == 'W') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No heroes starting with W found")


print("Heroes starting with W:")
heroes_start_W(hero_list)

print("________________________________________________")


def crit_real_name(hero):
    return hero.get('real_name') or ''


hero_list.add_criterion('real_name', crit_real_name)

hero_list.sort_by_criterion('real_name')

print("Chars sorted by real name:")
for hero in hero_list:
    print(hero['real_name'])

print("________________________________________________")


def crit_first_app(hero):
    return hero.get('first_appearance') or 0


hero_list.add_criterion('first_appearance', crit_first_app)

hero_list.sort_by_criterion('first_appearance')

print("Chars sorted by first appearance:")
for hero in hero_list:
    print(hero['name'])

print("________________________________________________")

print("Changing Ant Man's real name from Hank Pym to Scott Lang...")


def update_antman_name(hero_list):
    for hero in hero_list:
        if hero['name'] == "Ant Man":
            hero['real_name'] = "Scott Lang"


update_antman_name(hero_list)

for hero in hero_list:
    if hero['name'] == "Ant Man":
        print(f"{hero['name']}'s real name is {hero['real_name']}")

print("________________________________________________")

print("Chars with 'time-traveling' or 'suit' in bio:")


def show_time_travel_or_suit(hero_list):
    found = False
    for hero in hero_list:
        bio = hero.get('short_bio', '').lower()
        if 'time-traveling' in bio or 'suit' in bio:
            print(hero['name'])
            found = True
    if not found:
        print("No chars with 'time-traveling' or 'suit' in bio found.")


show_time_travel_or_suit(hero_list)

print("________________________________________________")

print("Removing Electro and Baron Zemo from list if present:")


def rm_chars(hero_list):
    found1 = False
    found2 = False
    aux = deepcopy(hero_list)
    for hero in aux:
        if hero['name'] == "Electro":
            print(f"Removing {hero['name']}.")
            print(f"{hero['name']} info: {hero}")
            hero_list.delete_value(hero['name'], 'name')
            found1 = True
        if hero['name'] == "Baron Zemo":
            print(f"Removing {hero['name']}.")
            print(f"{hero['name']} info: {hero}")
            hero_list.delete_value(hero['name'], 'name')
            found2 = True
    if not found1:
        print("Electro not found in list.")
    if not found2:
        print("Baron Zemo not found in list.")


rm_chars(hero_list)
