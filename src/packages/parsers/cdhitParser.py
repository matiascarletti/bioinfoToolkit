import re

cdhitFile = "pdbFullCdHit.fasta.clstr"

def getCdhitDictFrom(cdhitFile):
	"""
	Purpose: get a cdhit dict with clusterNames as keys and pdbIds
	"""
	# leo el cluster y lo guardo en una lista (cada elemento es una línea del cluster)
	cdhitLinesList = open(cdhitFile, "r").readlines()

	# para cada linea uso split y genero listas por cada linea. Esto hace que me quede una lista de listas (cada elemento de la lista cdhit ahora es una lista, cuyos elementos son las palabras separadas por coma)
	for cdhitLineIndex in range(len(cdhitLinesList)):
		cdhitLinesList[cdhitLineIndex] = cdcdhitLinesList[cdhitLineIndex].split()

	# creo el diccionario donde se va a guardar todo
	cdhitDict = dict()

	# creo listas vacias para ir guardando las claves y los valores
	keys = []
	values = []


	# para cada elemento del rango de la longitud de la lista (si la lista es de 100 elementos estos sería range(100), es decir, de 0 a 99) me fijo si la longitud es igual a 2. Si es asi significa que es el nombre del cluster, entonces lo guardo en la lista claves (sumo el primer elemento que es la palabra Cluster al segundo, que es el numero de cluster. Uso [1:] para no agarrar el simbolo mayor >)
	# ademas agrego una lista vacía dentro de la lista valores
	# Si no es el nombre del cluster me fijo si tiene la palabra .ent y con regular expression me quedo con las partes que me interesan y se lo agrego a la lista vacía que agregue a la lista valores. Fijate que uso valores[-1] porque voy agregando cosas a la última lista agregada, cuando cambio de cluster agrego otra lista vacía y voy agregando cosas en esa.
	# si no tiene la palabra .ent, agrego la informacion sacandole los tres puntos y el signo mayor
	for i in range(len(cdhit)):
		if len(cdhit[i]) == 2:
			keys.append(cdhit[i][0][1:]+cdhit[i][1])
			values.append([])
		else:
			if ".ent" in cdhit[i][2]:
				values[-1].append(re.search("pdb(.*).ent(.*).p(.*)", cdhit[i][2]).group(1) + re.search("pdb(.*).ent(.*).p(.*)", cdhit[i][2]).group(2))
			else:
				values[-1].append(cdhit[i][2].replace("...","").replace(">",""))

	# Por ultimo le voy agregando al diccionario cada clave(cluster) con su respectivo valor(la lista de cadenas pdb)
	for i in range(len(claves)):
		diccCdhit[claves[i]] = valores[i]