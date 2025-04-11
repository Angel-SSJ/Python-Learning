import array

numeros = array.array("i",[1,2,3,4])
nombres = array.array("u",['a','b','c','d','e','f','h',])

print(nombres[1])


vocales = ['hola','mundo','Esto es una prueba','xd',1,True, 3.5]


print(f"lenght nombres: {len(nombres)}")
print(nombres)

print(f"lenght numeros: {len(numeros)}")
print(numeros)


'''
Array -Efficient Arrays of numeric values  -https://docs.python.org/3/library/array.html

Type code         C Type           Python Type       Minimum size in bytes       Notes
'b'            signed char            int                      1                
'B'            unsigned char          int                      1
'u'            wchar_t          Unicode character              2                  (1)
'w'            Py_UCS4           Unicode character             4                   
'h'            signed short           int                      2                  
'H'            unsigned short         int                      2
'i'            signed int             int                      2
'I'            unsigned int           int                      2
'l'            signed long            int                      4
'L'            unsigned long          int                      4
'q'            signed long long       int                      8
'Q'            unsigned long long     int                      8
'f'            float                  float                    4
'd'            double                 float                    8
'''