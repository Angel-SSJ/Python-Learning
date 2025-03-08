#SETS
# Sets are used to store multiple items in a single variable.
set1 = {'Roger', 'Syd'}
set2 = {'Luna'}
intersect = set1 | set2
print(intersect)
print('Roger' in set1 & set2)

set2 = {'Roger'}
intersect = set1 - set2
print(intersect)

Set1 = ["Roger", "Syd", "Roger"]
set2 = {"Roger"}
print(list(set1))
print(set1 - set2)