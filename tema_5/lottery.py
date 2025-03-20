"""

- En este ejemplo vamos a ver cual han sido los nº que más han aparecido en los sorteos
- En esta ocasión, los datos son desde 1985-2012 y desde 2013-2018
- Los archivos apareceran de forma: 8/12/2018, 08, 09, 12, 19, 24, 41, 39, 4, 9759406. Esto es:
- FECHA sorteo\ los 6 nº ganadores\ complementarios\ reintegro\ joker
- Nostros nos vamos a quedar con los 6 primeros nºs de la combinación ganadora para cada una de las líneas
- Tener en cuenta que hay líneas en las que no aparecen nº

"""

import requests
import pylab as pl

#Nuevamente no nos vamos a descargar el fichero CSV sino que los vamos a extraer los datos directamente desde la url
url = 'https://docs.google.com/spreadsheet/pub?key=0AhqMeY8ZOrNKdFJnYkMzX3JzN2lkRlZZTXV2aldqS1E&single=true&gid=1&output=csv'

response = requests.get(url)
lineas = response.text.splitlines()

url = 'https://docs.google.com/spreadsheet/pub?key=0AhqMeY8ZOrNKdFJnYkMzX3JzN2lkRlZZTXV2aldqS1E&single=true&gid=0&output=csv'
response = requests.get(url)
lineas = lineas + response.text.splitlines() # a las líneas del primer fichero le unimos las del segundo fichero

# lo siguiente que vamos a hacer es tener un diccionario donde iremos contando cuntas veces aparece cada nº en la combinación ganadora
sdict = dict()
for l in lineas[1:]:
    lsorteo = l.split(',') #recorremos las lineas obviando las comas y esto nos da una lista
    for num in lsorteo[1:6]: #la lista que hemos obtenido la recorremos por numero a numero y nos quedamos del 1 al 6
        sdict[num] = sdict.get(num, 0) +1 # sdict contiene el nº de repeticiones para cada nº
        #llegados a este punto hemos creado un diccionario vamos a usar compresión de listas y sorted para tener algo ordenado por el nº de apariciones de cada nº0

tmp = list() #creamos una lista auxiliar con tuplas con el valor(nº de repeticiones) como primer componente
for k, v in sdict.items():
    tmp.append( (v, k) )
top6 = sorted(tmp, reverse=True)[:6]  #este top6 almacena los 6 nº que han aparecido más veces en los sorteos
print(top6) # aquí teneemos las tuplas del número en sí y del nº de repeteiciones

# a continuación vamos a preparar la gráfica. Etiquetas de las barras y valores de las repeticiones usando las tuplas anteriores:
top6_nums = [x[1] for x in top6] # saco una lista con el elemento nº 1 de la tupla que es el número en sí
print(top6_nums)

top6_repe = [int(x[0]) for x in top6] #aquí saco otra lista con el elemento 0 de la tupla que es el nº de repeticiones que ha tenido
print(top6_repe)

# Vamos ahora a la gráfica de barras:
pl.bar(range(6), top6_repe, align='center')
puntos = range(6)
pl.xticks(puntos, top6_nums)
pl.show()