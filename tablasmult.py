#!/urs/bin/python3

# Tablas de multiplicar del 1 al 10.

for indice1 in range(1,11):
	print "Tabla del "+ str(indice1)
	print "-----------"

	for indice2 in range(1,11):
		print(str(indice1)+" por "+ str(indice2)+" es "+str(indice1*indice2))
