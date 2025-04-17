def count_carnivore_dinosaur_eggs(egg_list)-> int:
    total_carnivore_eggs=0
    for eggs in egg_list:
        if eggs % 2 ==0:
            total_carnivore_eggs+=eggs
    return total_carnivore_eggs
eggs_list =[1,2,2,3,43,5,6,54,66,65]
#print(count_carnivore_dinosaur_eggs(eggs_list))






