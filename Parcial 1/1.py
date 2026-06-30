from list_ import List
from super_heroes_data import superheroes


def heroes_to_list(superheroes):
    hero_list = List()
    for hero in superheroes:
        hero_list.append(hero)
    return hero_list


hero_list = heroes_to_list(superheroes)


def find_captain_america(hero_list, index=0):
    if index >= len(hero_list):
        print('Captain America is not in the list')
        return False
    if hero_list[index]['name'] == 'Captain America':
        print('Captain America is in the list')
        return True
    return find_captain_america(hero_list, index + 1)


find_captain_america(hero_list, 0)

print("--------------------------------------------------")
def list_heroes(hero_list, index=0):
    if index >= len(hero_list):
        return
    print(hero_list[index]['name'])
    list_heroes(hero_list, index + 1)


list_heroes(hero_list)
