import csv

with open("Usuarios.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(list(row))

