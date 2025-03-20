"""
En este ejemplo vamos a ver la evolución del EURIBOR representado en una gráfica con las librerías:
requests, pylab, matplotlib, calendar, locate
"""

import requests
import pylab as pl
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'es_ES') #eso nos devuelve los nombres de los meses en español
#para recabar información vamos a hacer el siguiente import:
#esto es como si lo hiciéramos desde nuestro navegador pero lo hacemos desde aquí en su lugar

#lo siguiente que vamos a hacer es indicar la dirección dentro de la variable "url". Para hacer una petición "get" de información (protocolo html)
url = 'https://raw.githubusercontent.com/dgarridouma/python-course/main/EURIBOR_2017.csv'
response = requests.get(url) #en la variable "response" queda almacenada la respuesta. Es como si hubiéramos descargado el fichero csv
data = response.text.splitlines() #si queremos tener nuestro texto dividido en líneas y obtener una lista de strings. El método text nos devuelve el texto del csv
#print(data)
for linea in data[1:]:
    palabras_linea = linea.split(',')

# creamos una lista de floats con los valores de la linea
# descartamos el primer y último valor de la lista por contener
# el nombre del indicador y la media del año respectivamente

valores =[float(x) for x in palabras_linea[1:len(palabras_linea)-1]] #cada nº lo convertimos en flotante y lo almacenamos en la lista de "valores" para cada una de las líneas
print(valores) # [-0.095, -0.106, -0.11, -0.119, -0.127, -0.149, -0.154, -0.156, -0.168, -0.18, -0.189, -0.19]


# a continuación vamos a representar 12 valores en el eje x
# luego vamos a darle unos atributos. Market es para representar una especie de puntitos
# luego el label, esto es, la etiqueta que nos viene dado el euribor a 1 semana.. etc
pl.plot(range(1, 13), valores, marker = 'o', label = palabras_linea[0])


# Detalles para la gráfica y darle foramto:

pl.title("Evolución del EURIBOR 2017") # título de la gráfica
pl.xlabel("Mes") # eje x recibe el título mes
pl.ylabel("Valor indicador") # eje y recibe el título de valores
pl.xticks(range(13),[x[:3] for x in list(calendar.month_name)])# valores que va a mostarar en el eje x para cada uno de los puntos. 
# nota: Usamos calendar para sacar los nombres de cada mes, en este caso estamos sacando las letras de los nombres de cada mes.
pl.grid(True) # para que aparezca una cuadrícula
pl.legend() # para que aparezca una leyenda
pl.show() # con este comando mostramos la gráfica
