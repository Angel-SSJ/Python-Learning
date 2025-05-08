
import time
import pandas as pd

csv_file='empleados.csv'

def average_salary_by_department(file):
    # Colors ANSI
    GREEN ='\033[92m'
    RESET='\033[0m'
    ORANGE = '\033[33;5;208m'

    df= pd.read_csv(file)
    average_salary=df.groupby('Departamento')['Salario'].mean().round(1)

    print('Salario promedio por departamento')
    for department,salary in average_salary.items():
        print(f'{ORANGE}{'':<2}{department:<12}{RESET} $ {GREEN}{salary}{RESET}')
    time.sleep(1)



def oldest_employee(file):
    # Colors ANSI

    RESET = '\033[0m'
    ORANGE = '\033[33;5;208m'

    df=pd.read_csv(file)
    oldest_employee=df.loc[df['Edad'].idxmax()]

    print(f'Usuario con mayor edad:')
    print(f'{ORANGE}{'':<2}Nombre: {RESET}{oldest_employee["Nombre"]}')
    print(f'{ORANGE}{'':<2}Edad: {RESET}{oldest_employee["Edad"]}')
    print(f'{ORANGE}{'':<2}Salario: {RESET}{oldest_employee["Salario"]}')
    print(f'{ORANGE}{'':<2}Departamento: {RESET}{oldest_employee["Departamento"]}')
    print(f'')
    time.sleep(1)

def employees_by_department(file):
    # Colors ANSI
    RESET = '\033[0m'
    ORANGE = '\033[33;5;208m'

    df=pd.read_csv(file)
    employees_by_department=(df.groupby('Departamento')['Nombre'].count())
    print('\nCantidad de empleados por departamento: ')
    for department,count in employees_by_department.items():
        print(f'{ORANGE}{'':<2}{department}: {RESET}{count}')
    time.sleep(1)


def summary_department_csv(file,name):
    #Colors ASCI
    RESET = '\033[0m'
    GREEN = '\033[36m'
    pf=pd.read_csv(file)

    summary_csv=pf.groupby('Departamento').agg(
        Total_Empleados=('Nombre', 'count'),
        Salario_Promedio=('Salario', 'mean')).reset_index().round(1)
    summary_csv.to_csv(name,index=False,encoding='utf-8')
    print(f' Archivo {name} {GREEN} guardado exitosamente.{RESET}')
    time.sleep(1)



flow=True
while flow:
    option=int(input('\nA continuación, se te presentan algunas opciones:\n'
                     '1- Ver el salario promedio por departamento\n'
                     '2- Ver el empleado con mayor edad\n'
                     '3- Ver el numero de empleados por departamento\n'
                     '4- exportar archivo csv con el resumen\n'
                     '5- No deseo continuar\n'
                     'Escoga la opción: '))
    match option:
        case 1:
            flow=True
            average_salary_by_department(csv_file)

        case 2:
            flow = True
            oldest_employee(csv_file)
        case 3:
            flow = True
            employees_by_department(csv_file)
        case 4:
            flow = True
            name=str(input(f'Inserte el nombre del archivo a exportar: '))
            name =f'{name}.csv'
            summary_department_csv(csv_file,name)
        case 5:
            flow = False
