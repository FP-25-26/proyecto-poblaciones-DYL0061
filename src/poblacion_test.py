from poblacion import *

ruta_fichero = 'data\population.csv'
poblaciones = lee_poblaciones(ruta_fichero)


def lee_poblaciones_test(ruta_fichero):
	l = lee_poblaciones(ruta_fichero)
	print('Las tres primeras:')
	for i in (0, 1, 2):
		print(l[i])


def calcula_paises_test(poblaciones):

	l = calcula_paises(poblaciones)
	print('Los 5 primeros son:')
	for i in range(5):
		print(l[i])


def filtra_por_pais_test(poblaciones, nombre_o_codigo):
	l = filtra_por_pais(poblaciones, nombre_o_codigo)
	for i in l:
		print(i)


def filtra_por_paises_y_anyo_test(poblaciones, anyo, paises):
	l = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
	print(l)



def muestra_evolucion_poblacion_test(poblaciones, nombre_o_codigo):
	muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)



def muestra_comparativa_paises_anyo_test(poblaciones, anyo, paises):
	muestra_comparativa_paises_anyo(poblaciones, anyo, paises)



#lee_poblaciones_test(ruta_fichero)
#calcula_paises_test(poblaciones)
#filtra_por_pais_test(poblaciones, 'Zimbabwe')
#filtra_por_paises_y_anyo_test(poblaciones, 2000, ['Zimbabwe', 'Europe & Central Asia (IDA & IBRD countries)'])
#muestra_evolucion_poblacion_test(poblaciones, 'Zimbabwe')
muestra_comparativa_paises_anyo_test(poblaciones, 2000, ['Europe & Central Asia', 'European Union', 'Fragile and conflict affected situations'])