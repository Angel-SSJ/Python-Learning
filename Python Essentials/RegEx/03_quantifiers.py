###
# 03-Quantifiers
# Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caraecteres se deben encontrar en una cadena.
###

import re

# *: puede aparecer 0 o más veces
text ='aaaba'
pattern='a*'
matches=re.findall(pattern,text)
print(matches) #return ['aaa', '', 'a', '']

# +: puede aparacer una o mas veces
text='dddaa cacc'
pattern='a+'
matches=re.findall(pattern,text)
print(matches) #return ['aaa', 'a']


# ?: puede aparecer 0 o 1 vez
text='aaabaccagfb'
pattern='a?b'
matches=re.findall(pattern,text)
print(matches) #return ['ab']

text='aaabaccagfb'
pattern='a?.[b-zB-Z]'
matches=re.findall(pattern,text)
print(matches) #return ['ab']


# Contando Ocurrencias en Regex

# {n}: Exactamente n veces
text = 'aaaaaaa aa aaaa'
pattern='a{3}'
matches = re.findall(pattern,text)
print(matches)

# {n, m}: Entre n y m veces
text = 'aagfadgdaaagfdafd'
pattern='a{2,3}'
matches = re.findall(pattern,text)
print(matches) #return ['aa', 'aaa']



