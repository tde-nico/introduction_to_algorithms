'''
Sia A un array di n interi Con la coppia ordinata (i.j), 0 <= i <= j < n, rappresentiamo
suo sottoarray che parte dall'elemento in posizione i e termina con l'elemento in posizione j,
definiamo valore di un sottoarray come la somma dei suoi elementi.
Progettare un algoritmo che, dato un array A di interi positivi ed un intero positivo s
restituisce la coppia ordinata che rappresenta il sottoarray di A più a sinistra che ha
valores Se un tale sottoarray non esiste, la funzione deve restituire None.

es:
	A = [1,3,5,2,9,3,3,1,6]
	s = 7
	risultato: (2,3) considerando che le coppie da destra a sinistra sono (2,3), (5,7), (7,8)

	A = [1,3,5,2,9,3,3,1,6]
	s = 21
	risultato: None

'''

def ricerca(A, s):
	i, j = 0, 0
	n = len(A)
	while i < n and j < n:
		somma = 0
		indice_somma = i
		while indice_somma <= j:
			somma += A[indice_somma]
			indice_somma += 1
		if somma == s:
			return (i, j)
		elif somma < s:
			j += 1
		else:
			i += 1
	return None


def ricerca_2(A, s):
	i, j = 0, 0
	n = len(A)
	somma = A[0]
	while i < n and j < n:
		if somma == s:
			return (i, j)
		elif somma < s:
			j += 1
			if j < n:
				somma += A[j]
		else:
			somma -= A[i]
			i += 1
	return None


def ricerca_print(A, s):
	i, j = 0, 0
	n = len(A)
	while i < n and j < n:
		somma = 0
		indice_somma = i
		while indice_somma <= j:
			somma += A[indice_somma]
			indice_somma += 1
		if somma == s:
			print(i, j)
			j += 1
		elif somma < s:
			j += 1
		else:
			i += 1


def ricerca_2_print(A, s):
	i, j = 0, 0
	n = len(A)
	somma = A[0]
	while i < n and j < n:
		if somma <= s:
			if somma == s:
				print(i, j)
			j += 1
			if j < n:
				somma += A[j]
		else:
			somma -= A[i]
			i += 1


A = [1, 3, 5, 2, 9, 3, 3, 1, 6]
print(ricerca(A, 7))
print(ricerca(A, 21))
