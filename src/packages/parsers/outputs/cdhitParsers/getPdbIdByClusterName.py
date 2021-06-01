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
	pdbIdByClusterNameDict = dict()

	# creo listas vacias para ir guardando las claves y los valores
	keys = []
	values = []


	# para cada elemento del rango de la longitud de la lista (si la lista es de 100 elementos estos sería range(100), es decir, de 0 a 99) me fijo si la longitud es igual a 2. Si es asi significa que es el nombre del cluster, entonces lo guardo en la lista claves (sumo el primer elemento que es la palabra Cluster al segundo, que es el numero de cluster. Uso [1:] para no agarrar el simbolo mayor >)
	# ademas agrego una lista vacía dentro de la lista valores
	# Si no es el nombre del cluster me fijo si tiene la palabra .ent y con regular expression me quedo con las partes que me interesan y se lo agrego a la lista vacía que agregue a la lista valores. Fijate que uso valores[-1] porque voy agregando cosas a la última lista agregada, cuando cambio de cluster agrego otra lista vacía y voy agregando cosas en esa.
	# si no tiene la palabra .ent, agrego la informacion sacandole los tres puntos y el signo mayor
	
	# genero un iterable con la function range: 
	for lineIndex in range(len(cdhitLinesList)):
		# si la longitud de la linea es igual a dos
		if len(cdhitLinesList[lineIndex]) == 2:
			clusterWord		= cdhitLinesList[lineIndex][0][1:] # primer elemento de la linea
			clusterNumber	= cdhitLinesList[lineIndex][1] # segundo elemento de la linea
			clusterName		= clusterWord + "_" + clusterNumber
			keys.append(clusterName)
			values.append([])
		else:
			if ".ent" in cdhitLinesList[lineIndex][2]:
				# añado al ultimo elemento de la lista cada pdbId
				pdbChainIdGroup1 = re.search("pdb(.*).ent(.*).p(.*)", cdhitLinesList[lineIndex][2]).group(1)
				pdbChainIdGroup2 = re.search("pdb(.*).ent(.*).p(.*)", cdhitLinesList[lineIndex][2]).group(2)
				pdbChainIdGroup3 = re.search("pdb(.*).ent(.*).p(.*)", cdhitLinesList[lineIndex][2]).group(3)
				values[-1].append(
								pdbChainIdGroup1
								+ pdbChainIdGroup2
								)
			else:
				# añado al ultimo elemento de la lista cada pdbId
				pdbChainId = cdhitLinesList[lineIndex][2].replace("...","").replace(">","")
				values[-1].append(
								pdbChainId
								)

	# Por ultimo le voy agregando al diccionario cada clave(cluster) con su respectivo valor(la lista de cadenas pdb)
	for i in range(len(keys)):
		pdbIdByClusterNameDict[keys[i]] = values[i]
	
	return pdbIdByClusterNameDict

cdhitOutFile = "/home/matias/Projects/2020/Codnas_pdbDbMfastaClustering/outputs/2020-10-09/cd-hit/seqClusters/pdbDbRxsNmrs.fasta.clstr"
pdbIdByClusterNameDict = getPdbIdByClusterNameDictFrom(cdhitOutFile)