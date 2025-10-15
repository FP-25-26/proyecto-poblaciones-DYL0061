from collections import namedtuple
import csv
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 
							   'pais, codigo, año, censo')




def lee_poblaciones(ruta_fichero):
	with open(ruta_fichero) as f:
		lector = csv.reader(f)

		l = []
		for pais, codigo, año, censo in lector:
			año = int(año)
			censo = int(censo)

			l.append(RegistroPoblacion(pais, codigo, año, censo))
	
	return l




def calcula_paises(poblaciones):
	l = []
	for i in poblaciones:
		l.append(i.pais)
	
	l = set(l)
	l = list(l)
	l.sort()
	return l




def filtra_por_pais(poblaciones, nombre_o_codigo):
	l = []
	for i in poblaciones:
		if i.pais == nombre_o_codigo or i.codigo == nombre_o_codigo:
			l.append((i.año, i.censo))
	return l




def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
	l = []
	for i in poblaciones:
		if i.pais in paises and i.año == anyo:
			l.append((i.pais, i.censo))
	return l





def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
	a = []
	c = []
	for i in poblaciones:
		if i.pais == nombre_o_codigo or i.codigo == nombre_o_codigo:
			c.append(i.censo)
			a.append(i.año)
	
	plt.title(f'curva de evolución de la población de {nombre_o_codigo}')
	plt.plot(a, c)
	plt.show()
	

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
	p = []
	h = []
	for i in poblaciones:
		if i.año == anyo and i.pais in paises:
			p.append(i.pais)
			h.append(i.censo)
	
	plt.title(f'Población en el año {anyo}')
	plt.bar(p, h)
	plt.show()
