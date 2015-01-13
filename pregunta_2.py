#
#	Script para la tarea 1 de la admisión del DevLab
#	Ejecutar con versiones de python posteriores a la 3 pls
#	Solicita nombre del .txt donde está el Sowpods y retorna las letras sin repeticiones
#

archivo = input("Nombre del txt donde está el SOWPODS: ")
chivo = open(archivo, 'r')
abcdario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
linea = chivo.readline()

while(linea != ''):
	for i in range(0, len(linea)):
		if(i < len(linea) - 1):
			if(linea[i] == linea[i+1] and linea[i] in abcdario):
				abcdario.remove(linea[i])
	linea = chivo.readline()
chivo.close()
print("Letras sin repeticiones: ", abcdario)