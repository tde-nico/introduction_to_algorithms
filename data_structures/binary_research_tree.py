import random
from binatry_tree import *


def generate_BRT_recoursive(node_number):
	if node_number == 0:
		return None
	node = NodeBT()
	son_value = random.randint(0, node_number)
	node.left = generate_BRT_recoursive(son_value)
	if node.left:
		node.left.parent = node
	node.right = generate_BRT_recoursive(node_number - 1 - son_value)
	if node.right:
		node.right.parent = node
	return node

def place_keys(root, keys):
	if root:
		place_keys(root.left, keys)
		root.key = keys.pop()
		place_keys(root.right, keys)

def generate_BRT(max_node_number):
	if max_node_number == 0:
		return None
	tree = generate_BRT_recoursive(max_node_number)
	keys = random.sample([i for i in range(5 * max_node_number)], max_node_number)
	keys.sort(reverse=True)
	place_keys(tree, keys)
	return tree

def search_BRT(root, key):
	if (root == None) or (root.key == key):
		return root
	if (key < root.key):
		return search_BRT(root.left, key)
	return search_BRT(root.right, key)

def insert_BRT(root, element):
	father, current = None, root
	node = NodeBT(element)
	while (current != None):
		father = current
		if node.key < current.key:
			current = current.left
		else:
			current = current.right
	if (father == None):
		root = node
	else:
		if (node.key < father.key):
			father.left = node
		else:
			father.right = node
	node.parent = father
	return root

