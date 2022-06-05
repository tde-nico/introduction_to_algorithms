from linked_list import *

def enqueue(head, tail, el):
	if (tail == None):
		tail = el
		head = el
	else:
		tail.next = el
		tail = el
	return head, tail

def dequeue (head, tail):
	if (head == None):
		raise Exception("Empty queue")
	e = head
	head = e.next
	if (head == None):
		tail = None
	return head, tail, e
