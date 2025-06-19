import pandas as pd

document = 'notas_alumnos_utf8_sig.csv'


class AnalysisDocument:

    def main_reading(self):
        # PRIMERAS 10 FILAS del DATAFRAME
        file = pd.read_csv(document)
        print(f'\n{file.head(10)}\n')

    def grades_analysis(self):

        # NOTA PROMEDIO GENERAL DE TODOS LOS ESTUDIANTES
        file = pd.read_csv(document)
        average_grade_per_student = file['nota'].mean()
        average = average_grade_per_student / 8
        print(f'\nNota promedio general de todos los alumnos: {average.round(2)}')

        # NOTA PROMEDIO POR MATERIA
        average_grade_per_subject = file.groupby('materia')['nota'].mean().reset_index()
        average_grade_per_subject['nota'] = (average_grade_per_subject['nota']* 0.10).round(2)
        average_grade_per_subject.columns = ['materia','nota']
        print(f'\nNota promedio por materia:\n{average_grade_per_subject.to_string(index=False)}')

        # NOTA PROMEDIO POR TRIMESTRE
        average_grade_per_quarter = file.groupby('trimestre')['nota'].mean().reset_index()
        average_grade_per_quarter['nota']=(average_grade_per_quarter['nota']*0.10).round(2)
        average_grade_per_quarter.columns = ['trimestre', 'nota']
        print(f'\nNota promedio por trimestre:')
        print(f"{'Trimestre':<12} {'Nota':>4}")
        for _, row in average_grade_per_quarter.iterrows():
            print(f"{int(row['trimestre']):<12} {row['nota']}")

        # ESTUDIANTE CON PROMEDIO MAS ALTO EN TOTAL
        average_students = file.groupby(['id_alumno', 'nombre'])['nota'].mean()
        top_student = average_students.idxmax()
        top_grade = (average_students.max()* 0.10).round(2)
        name = top_student[1]
        print(f'\nMejor estudiante:\n{name} con el promedio de {top_grade}')


        #MATERIA CON LA MAYOR CANTIDAD DE NOTAS INFERIORES A 60
        low_grades = file[file['nota'] < 60]
        count_low = low_grades['materia'].value_counts()
        subject_low = count_low.idxmax()
        count_total = count_low.max()

        print(f'\nMayor cantidad de notas inferiores a 60')
        print(f"{'Materia':<12} {'Cantidad':>4}")
        print(f"{subject_low:<12} {count_total:.2f}\n")
    
        
    def analysis_per_student(self):
        file = pd.read_csv(document)

        # ESTUDIANTES CON PROMEDIO GENERAL MAYOR O IGUAL A 90
        # promedio >=90
        print(f'Estudiantes con promedio general más alto\n')
        students_tops = file.groupby('nombre')['nota'].max().reset_index()
        print(f'{students_tops.to_string(index=False)}')


        # MATERIA MAS DIFICIL(MENOR PROMEDIO) PARA CADA ESTUDIANTE
        average_subject = file.groupby(['id_alumno', 'nombre', 'materia'])['nota'].mean()
        hard_sujects = average_subject.groupby(level=[0, 1]).idxmin()
        result = average_subject.loc[hard_sujects].reset_index()
        result.columns = ['id_alumno', 'nombre', 'materia', 'nota']
        print(f'\nMateria más dificil por alumno\n')
        print(f"{result[['nombre', 'materia', 'nota']].to_string(index=False, formatters={'nota': '{:.2f}'.format})}\n")


documentAnalysis = AnalysisDocument()

continuar = True

while continuar:
    print(
        'Tiene las siguientes opciones: \n1. Lectura de datos\n2. Análisis de notas\n3. Análisis por alumno\n 4. Deseo salir')
    option = int(input('Ingrese su opcion aqui: '))
    match option:
        case 1:
            documentAnalysis.main_reading()
        case 2:
            documentAnalysis.grades_analysis()
        case 3:
            documentAnalysis.analysis_per_student()
        case 4:
            continuar = False
        case _:
            print('Opcion no valida')
