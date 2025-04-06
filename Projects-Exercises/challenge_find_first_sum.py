nums = [4,5,6,2]
goal=9

def find_first_sum(nums, goal):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j] == goal):
                return [i,j]
    return None



#print(find_first_sum(nums,goal))



#------------------------------------------------------
def find_first_sum_dictionary(nums,goal):
    seen={}# diccionario para guardar le numero y su indice
    for index, value in enumerate(nums): # enumera los numeros, regresandote le indice y el valor0
        missing = goal - value
        if missing in seen: return [seen[missing], index]
        seen[value] = index # guardar el nuemro actual a los vistos, porque no hemos encontrado los valores correctos
    return None




print(find_first_sum_dictionary(nums,goal))