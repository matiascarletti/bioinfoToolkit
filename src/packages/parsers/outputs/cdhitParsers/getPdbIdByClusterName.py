#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Cdhit file output parser for obtein pdbId list by cluster name.
{License_info}
"""

# Futures
from __future__ import print_function
# […]

# Built-in/Generic Imports
import re
# […]

# Libs
# […]

# Own modules
# […]

__authors__ = ['Guillermo Benitez', 'Matías Carletti']
__copyright__ = 'Copyright 2021, bioinfoToolkit'
__credits__ = ['{credit_list}']
__license__ = '{license}'
__version__ = '{mayor}.{minor}.{rel}'
__maintainer__ = '{maintainer}'
__email__ = 'matias.carletti@gmail.com'
__status__ = '{dev_status}'


def getPdbIdByClusterNameDictFrom(cdhitOutFile):
	"""
	Purpose: get a cdhit dictionary from cdhit output \
	with clusterNames as keys and a pdbId list as values

	Parameters:
	- cdhitOutFile	a str path		to cdhit output file. \
		For example: "pdbFullCdHit.fasta.clstr"
	
	Returns:
	- cdhitDict		a dict parser	with clusterNames as keys and a pdbId List as values \
		For example: {"Cluster_0": [1trv, 2rms], "Cluster_1": ["9ooa, 5oop]}
	
	"""
	# leo el cluster y lo guardo en una lista (cada elemento es una línea del cluster)
	cdhitLinesList = open(cdhitOutFile, "r").readlines()

	# para cada linea uso split y genero listas por cada linea. Esto hace que me quede una lista de listas (cada elemento de la lista cdhit ahora es una lista, cuyos elementos son las palabras separadas por coma)
	for cdhitLineIndex in range(len(cdhitLinesList)):
		cdhitLinesList[cdhitLineIndex] = cdhitLinesList[cdhitLineIndex].split()

	# creo el diccionario donde se va a guardar todo
	cdhitDict = dict()

	# creo listas vacias para ir guardando las claves y los valores
	keys = []
	values = []


	# para cada elemento del rango de la longitud de la lista (si la lista es de 100 elementos estos sería range(100), es decir, de 0 a 99) me fijo si la longitud es igual a 2. Si es asi significa que es el nombre del cluster, entonces lo guardo en la lista claves (sumo el primer elemento que es la palabra Cluster al segundo, que es el numero de cluster. Uso [1:] para no agarrar el simbolo mayor >)
	# ademas agrego una lista vacía dentro de la lista valores
	# Si no es el nombre del cluster me fijo si tiene la palabra .ent y con regular expression me quedo con las partes que me interesan y se lo agrego a la lista vacía que agregue a la lista valores. Fijate que uso valores[-1] porque voy agregando cosas a la última lista agregada, cuando cambio de cluster agrego otra lista vacía y voy agregando cosas en esa.
	# si no tiene la palabra .ent, agrego la informacion sacandole los tres puntos y el signo mayor
	for i in range(len(cdhitLinesList)):
		if len(cdhitLinesList[i]) == 2:
			keys.append(cdhitLinesList[i][0][1:] + cdhitLinesList[i][1])
			values.append([])
		else:
			if ".ent" in cdhit[i][2]:
				values[-1].append(re.search(
											"pdb(.*).ent(.*).p(.*)", 
											cdhitLinesList[i][2]).group(1) + re.search("pdb(.*).ent(.*).p(.*)", 
											cdhitLinesList[i][2]).group(2)
											)
			else:
				values[-1].append(cdhitLinesList[i][2].replace("...","").replace(">",""))

	# Por ultimo le voy agregando al diccionario cada clave(cluster) con su respectivo valor(la lista de cadenas pdb)
	for i in range(len(keys)):
		cdhitDict[keys[i]] = values[i]
	
	return cdhitDict