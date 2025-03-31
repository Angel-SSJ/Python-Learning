import csv

with open('csv_examples') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count ==0:
            print(f'Column names are:{",".join(row)}')
            line_count+=1
        else:
            print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count+=1

    print(f'Number of lines: {line_count}')



# with open("Usuarios.csv", "r") as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(list(row))
#
