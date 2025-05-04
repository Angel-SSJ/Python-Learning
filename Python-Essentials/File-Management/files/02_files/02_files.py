import os
path_archive= 'datos/ventas.csv'
'''this option is optimal if you want to check if the FILE exists'''
if os.path.isfile(path_archive):
    print('El archivo existe')

else:
    print('El archivo no existe :(')
    os.makedirs(os.path.dirname(path_archive), exist_ok=True)
    with open(path_archive, mode='w', encoding='utf-8') as file:
        file.write('Fue creado correctamente el archivo con os')


#
#'''This option is optimal if you want to check if the DIRECTORY exists'''
#print('El directorio existe') if os.path.isdir(path_archive) else print('El directorio no existe :(')

'''using pathlib'''
from pathlib import Path
path_archive_lib='pathlibdatos/ventas.csv'
folder_path = Path(path_archive_lib)
if folder_path.exists():
    print('El archivo existe')
else:
    print('El archivo no existe :(')
    Path(path_archive_lib).parent.mkdir(parents=True, exist_ok=True)
    Path(path_archive_lib).write_text('Este archvio fue creado con pathlib')


