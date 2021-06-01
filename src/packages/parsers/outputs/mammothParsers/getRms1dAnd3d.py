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

__authors__ = 'Matías Carletti'
__copyright__ = 'Copyright 2021, bioinfoToolkit'
__credits__ = ['{credit_list}']
__license__ = '{license}'
__version__ = '{mayor}.{minor}.{rel}'
__maintainer__ = '{maintainer}'
__email__ = 'matias.carletti@gmail.com'
__status__ = '{dev_status}'


def getRms1dAnd3dDictFrom_test(mammothOutFile):
	# """
	# Purpose: get a cdhit dictionary from cdhit output \
	# with clusterNames as keys and a pdbId list as values

	# Parameters:
	# - mammothOutFile	a str path		to cdhit output file. \
	# 	For example: "pdbFullCdHit.fasta.clstr"
	
	# Returns:
	# - mammothDict 		a dict parser	with clusterNames as keys and a pdbId List as values \
	# 	For example: {"Cluster_0": [1trv, 2rms], "Cluster_1": ["9ooa, 5oop]}
	
	# """
	# leo el cluster y lo guardo en una lista (cada elemento es una línea del cluster)
    mammothLinesList = open(mammothOutFile, "r").readlines()

	# para cada linea uso split y genero listas por cada linea. Esto hace que me quede una lista de listas (cada elemento de la lista cdhit ahora es una lista, cuyos elementos son las palabras separadas por coma)
    for mammothLineIndex in range(len(mammothLinesList)):
        mammothLinesList[mammothLineIndex] = mammothLinesList[mammothLineIndex].split()
	# creo el diccionario donde se va a guardar todo
    rms1dAnd2dDict = dict()

	# creo listas vacias para ir guardando las claves y los valores
    keys = []
    values = []


	# para cada elemento del rango de la longitud de la lista (si la lista es de 100 elementos estos sería range(100), es decir, de 0 a 99) me fijo si la longitud es igual a 2. Si es asi significa que es el nombre del cluster, entonces lo guardo en la lista claves (sumo el primer elemento que es la palabra Cluster al segundo, que es el numero de cluster. Uso [1:] para no agarrar el simbolo mayor >)
	# ademas agrego una lista vacía dentro de la lista valores
	# Si no es el nombre del cluster me fijo si tiene la palabra .ent y con regular expression me quedo con las partes que me interesan y se lo agrego a la lista vacía que agregue a la lista valores. Fijate que uso valores[-1] porque voy agregando cosas a la última lista agregada, cuando cambio de cluster agrego otra lista vacía y voy agregando cosas en esa.
	# si no tiene la palabra .ent, agrego la informacion sacandole los tres puntos y el signo mayor
	
	# genero un iterable con la function range: 
    for lineIndex in range(len(mammothLinesList)):
        # si la longitud de la linea es igual a dos
        if "RMS=" in mammothLinesList[lineIndex]:
            # print(mammothLinesList[lineIndex], len(mammothLinesList[lineIndex]))
            if len(mammothLinesList[lineIndex]) == 11:
                keys.append("rms1d")
                values.append(mammothLinesList[lineIndex][8])
            elif len(mammothLinesList[lineIndex]) == 9:
                keys.append("rms3d")
                values.append(mammothLinesList[lineIndex][-1])
            elif len(mammothLinesList[lineIndex]) == 8:
                keys.append("rmsLG")
                values.append(mammothLinesList[lineIndex][-1])
	# Por ultimo le voy agregando al diccionario cada clave(cluster) con su respectivo valor(la lista de cadenas pdb)
    for i in range(len(keys)):
        rms1dAnd2dDict[keys[i]] = values[i]
    rms1dAnd2dDict["pdbIds_comparison"] = mammothOutFile.split("/")[-1].replace(".log", "")
    return rms1dAnd2dDict

def getRms1dAnd3dDictFrom(mammothOutFile):
    # leo el cluster y lo guardo en una lista (cada elemento es una línea del cluster)
    mammothLinesList = open(mammothOutFile, "r").readlines()
    """
    @param myParam
    ! jp
    ? j
    """
    # TODO 
	# para cada linea uso split y genero listas por cada linea. Esto hace que me quede una lista de listas (cada elemento de la lista cdhit ahora es una lista, cuyos elementos son las palabras separadas por coma)
    
    # creo el diccionario donde se va a guardar todo
    rms1dAnd2dDict = dict()
    for mammothLineIndex in range(len(mammothLinesList)):
        # psi1d = re.search("PSI(1D) = (.*)", mammothLinesList[mammothLineIndex])
        # psi3d = re.search("PSI(3D) =", mammothLinesList[mammothLineIndex])
        # LG = re.search("Sstr(LG)=", mammothLinesList[mammothLineIndex])
        #rms = re.search("PSI(1D)(.*)(.*)NSUP=(.*)NORM=(.*)RMS=(.*)NSS=(.*)", mammothLinesList[mammothLineIndex]).group(1)
        # re.search("pdb(.*).ent(.*).p(.*)"
        if "RMS=" in mammothLinesList[mammothLineIndex] and \
            " PSI(1D) = " in mammothLinesList[mammothLineIndex]:
            rms1d = re.search("PSI(....)(..)(.*)(.*)NSUP=(.*)NORM=(.*)RMS=(.*)NSS=(.*)", 
                              mammothLinesList[mammothLineIndex]).group(7)
            rms1dAnd2dDict["rms1d"] = [rms1d.replace(" ", "")]
        elif "RMS=" in mammothLinesList[mammothLineIndex] and \
            " PSI(3D) = " in mammothLinesList[mammothLineIndex]:
            rms3d = re.search("PSI(....)(..)(.*)(.*)NSUP=(.*)NORM=(.*)RMS=(.*)", 
                              mammothLinesList[mammothLineIndex]).group(7)
            rms1dAnd2dDict["rms3d"] = [rms3d.replace(" ", "")]
        elif "RMS=" in mammothLinesList[mammothLineIndex] and \
            " Sstr(LG)= " in mammothLinesList[mammothLineIndex]:
            rmsLG = re.search("RMS=(.*)", 
                              mammothLinesList[mammothLineIndex]).group(1)
            rms1dAnd2dDict["rmsLG"] = [rmsLG.replace(" ", "")]
    rms1dAnd2dDict["pdbIds_comparison"] = [mammothOutFile.split("/")[-1].replace(".log", "")]
    return rms1dAnd2dDict

# mammothOutFile = "/home/matias/Projects/2020/RvDb_codnasHomologues/outputs/2020-06-23/mammoth/RV6/logs/Cluster_20103/5l7e_A-5l7e_B.log"
# rms1dAnd2dDict = getRms1dAnd3dDictFrom(mammothOutFile)
# print(rms1dAnd2dDict)