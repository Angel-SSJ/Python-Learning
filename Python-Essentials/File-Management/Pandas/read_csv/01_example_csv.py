import pandas as pd
df=pd.read_
df = pd.read_csv('train.csv')


#print(df.head())

#print(df.tail(n=10))


#print(df.describe())

#print(df.describe(include=[int]))
#print(df.describe(exclude=[int]))

'''A menudo, a los profesionales les resulta fácil ver dichas estadísticas transponiéndolas con el .Tatributo.'''
#print(df.describe().T)


'''
Comprender datos

Este .info()método permite consultar rápidamente los tipos de datos, los valores faltantes y el tamaño de los datos de un DataFrame
    show_counts: proporciona algunos valores sobre el total de valores no faltantes en cada columna
    memory_usage: que muestra el uso total de memoria de los elementos del DataFrame
    verbose: imprime el resumen completo de [nombre del argumento .info()]
'''


print(df.info(show_counts=True,memory_usage=True, verbose=True))