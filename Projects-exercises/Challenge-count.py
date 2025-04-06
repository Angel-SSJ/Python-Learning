def check_is_balanced(un_texto):

    r_counter = un_texto.count('R')
    j_counter = un_texto.count('J')

    print(f'La latra R aparece {r_counter} veces\nLa letra J aparece {j_counter} veces')
    return r_counter == j_counter


def check_is_balanced_two(un_texto):
    r_counter, j_counter =0,0
    for i in range(0,len(un_texto)):
        if un_texto[i] == 'R':
            r_counter +=1
        if un_texto[i]=='J':
            j_counter+=1
    print(f'La latra R aparece {r_counter} veces\nLa letra J aparece {j_counter} veces')
    return r_counter == j_counter


#print(check_is_balanced('JRJRRJJRJRJJRRRJ'))
#print(check_is_balanced_two('JRJRRJJRJRJJRRRJ'))

#------------------------------------------------------------------------------------------------------------------------------------------------------
