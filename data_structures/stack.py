from linked_list import *

def push(top, el):
	el.next= top
	top = el
	return top

def pop(top):
	if (top == None):
		raise Exception("Empty stack")
	el = top
	top = el.next
	el.next = None
	return el, top
