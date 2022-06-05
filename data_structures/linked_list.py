class Node:
	def __init__(self, key=None, next=None):
		self.key = key
		self.next = next


def create_linked_list(array):
	linked = None
	for i in range(len(array), 0, -1):
		linked = Node(array[i-1], linked)
	return linked


def search(linked, value):
	copy = linked
	while ((copy != None) and (copy.key != value)):
		copy = copy.next
	return copy


def insert_start(linked, node):
	if (node != None):
		node.next = linked
	linked = node 
	return linked


def insert(linked, node, point):
	if point != None:
		node.next = point.next
		point.next = node
		return linked
	else:
		return None


def delete(linked, node):
	if (node != None):
		if node == linked:
			linked = linked.next
			return linked
		p_corr = linked
		while (p_corr.next != node):
			p_corr = p_corr.next
		p_corr.next = node.next
	return linked


def delete_ricoursive(linked, node):
	if linked == node:
		linked = linked.next
	else:
		linked.next = delete_ricoursive(linked.next, node)
	return linked
