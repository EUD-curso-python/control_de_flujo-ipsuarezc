import sys
import Modulo1.saludo as saludos

#print(sys.argv)
idioma = sys.argv[1]

if idioma == 'es':
   saludo = saludos.espanol()
elif idioma == 'en':
    saludo = saludos.ingles()
elif idioma == 'ge':
    saludo = saludos.aleman()
elif idioma == 'hw':
    saludo = saludos.hawai()
else:
    raise Exception('no sé')
print(saludos)