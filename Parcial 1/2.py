from list_ import List
from super_heroes_data import superheroes
from queue_ import Queue
from stack import Stack


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

print("Personajes ordenados por nombre:")
for hero in hero_list:
    print(hero['name'])

print("________________________________________________")

thing_pos = hero_list.search('The Thing', 'name')
if thing_pos is not None:
    print(f'The Thing está en la posición: {thing_pos}')
else:
    print('The Thing no está en la lista')

print("________________________________________________")

raccoon_pos = hero_list.search('Rocket Raccoon', 'name')
if raccoon_pos is not None:
    print(f'Rocket Raccoon está en la posición: {raccoon_pos}')
else:
    print('Rocket Raccoon no está en la lista')

print("________________________________________________")

print("Villanos:")
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


print("Villanos antes de 1980:")
vils_before_1980(vil_queue)

print("________________________________________________")


def heroes_start_Bl(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][:2] == 'Bl') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No se encontraron héroes que empiecen con Bl")


print("Héroes que empiezan con Bl:")
heroes_start_Bl(hero_list)

print()


def heroes_start_G(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][0] == 'G') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No se encontraron héroes que empiecen con G")


print("Héroes que empiezan con G:")
heroes_start_G(hero_list)

print()


def heroes_start_My(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][:2] == 'My') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No se encontraron héroes que empiecen con My")


print("Héroes que empiezan con My:")
heroes_start_My(hero_list)

print()


def heroes_start_W(hero_list):
    found = False
    for hero in hero_list:
        if (hero['name'][0] == 'W') and (hero['is_villain'] == False):
            print(hero['name'])
            found = True
    if not found:
        print("No se encontraron héroes que empiecen con W")


print("Héroes que empiezan con W:")
heroes_start_W(hero_list)

print("________________________________________________")


def crit_real_name(hero):
    return hero.get('real_name') or ''


hero_list.add_criterion('real_name', crit_real_name)

hero_list.sort_by_criterion('real_name')

print("Personajes ordenados por nombre real:")
for hero in hero_list:
    print(hero['real_name'])

print("________________________________________________")


def crit_first_app(hero):
    return hero.get('first_appearance') or 0


hero_list.add_criterion('first_appearance', crit_first_app)

hero_list.sort_by_criterion('first_appearance')

print("Personajes ordenados por año de primera aparición:")
for hero in hero_list:
    print(hero['name'])

print("________________________________________________")

print("Cambiando el nombre real de Ant Man de Hank Pym a Scott Lang...")


def update_antman_name(hero_list):
    for hero in hero_list:
        if hero['name'] == "Ant Man":
            hero['real_name'] = "Scott Lang"


update_antman_name(hero_list)

for hero in hero_list:
    if hero['name'] == "Ant Man":
        print(f"El nombre real de {hero['name']} es {hero['real_name']}")

print("________________________________________________")

print("Personajes cuya biografía incluye 'time-traveling' o 'suit':")


def show_time_travel_or_suit(hero_list):
    found = False
    for hero in hero_list:
        bio = hero.get('short_bio', '').lower()
        if 'time-traveling' in bio or 'suit' in bio:
            print(hero['name'])
            found = True
    if not found:
        print("No se encontraron personajes con 'time-traveling' o 'suit' en la biografía.")


show_time_travel_or_suit(hero_list)

print("________________________________________________")

print("Eliminando a Electro y Baron Zemo de la lista si están presentes:")


def rm_chars(hero_list, names):
    # Stack para guardar el historial de personajes eliminados
    removed_stack = Stack()

    for name in names:
        removed_hero = hero_list.delete_value(name, 'name')
        if removed_hero is not None:
            removed_stack.push(removed_hero)
        else:
            print(f"{name} no se encontró en la lista.")

    # Se muestran apilando/desapilando (LIFO): el último eliminado se muestra primero
    while removed_stack.size() > 0:
        hero = removed_stack.pop()
        print(f"Eliminando a {hero['name']}.")
        print(f"Información de {hero['name']}: {hero}")


rm_chars(hero_list, ["Electro", "Baron Zemo"])
