#Exercise5

'''
Design the algorithm corresponding to a program, which:
Create a two-dimensional table of length 5x5 and name ‘diagonal’.
Load the table so that the components belonging to 
the diagonal of the matrix take the value 1 and the rest the value 0.
Shows the contents of the table on the screen.
'''

#@CarlosAntonio

matriz = []
for indice_fila in range(0,5):
	fila = []
	for indice_col in range(0,5): 
		# Si estoy en alguna diagonal inicializo a 1
		if indice_fila == indice_col or indice_fila == 4 - indice_col:
			fila.append(1)
		#No estoy en diagonal, inicializo a 0
		else:
			fila.append(0)
	matriz.append(fila)
# Recorro para mostrar tabla
for fila in matriz:
	for elemento in fila:
		print(elemento," ",end="")
	print()
