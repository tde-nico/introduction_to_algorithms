'''
Si consideri una lista concatenata dove ogni nodo ha 2 campi
il campo key contenente un intero positivo ed il campo next con il puntatore al nodo
seguente (next vale None per l'ultimo nodo della lista)
Bisogna aggiornare i puntatori della lista in modo da creare una nuova lista priva dei
nodi con valore superiore a 10 e in cui i nodi rimanenti appaiono in ordine inverso rispetto
all' originale. Ad esempio per la lista di seguito a sinistra la funzione deve restituire la
lista di seguito a destra.

11 -> 10 -> 3 -> 7 -> 11 -> 12 -> 4 -> 15		4 -> 7 -> 3 -> 10

'''

class Node:
	def __init__(self, key=None, next=None):
		self.key = key
		self.next = next

def create_linked_list(array):
	linked = None
	for i in range(len(array), 0, -1):
		linked = Node(array[i-1], linked)
	return linked


def print_linked_list(lista):
	while lista != None:
		print(lista.key)
		lista = lista.next

def aggiorna(lista):
	while lista != None and lista.key > 10:
		lista = lista.next
	p = lista
	if p == None:
		return p
	while p.next != None:
		if p.next.key > 10:
			p.next = p.next.next
		else:
			p = p.next
	prev = None
	curr = lista
	next = lista.next
	while curr != None:
		curr.next = prev
		prev = curr
		curr = next
		if next != None:
			next = next.next
	lista = prev
	print_linked_list(lista) # print
	
	

linked = create_linked_list([11, 10, 3, 7, 11, 12, 4, 15])
aggiorna(linked)
