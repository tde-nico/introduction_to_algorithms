from binatry_tree import *

def left_rotation(root, node):
	to_switch = node.right
	node.right = to_switch.left
	if node.right != None:
		node.right.parent = node
	to_switch.left = node
	to_switch.parent = node.parent
	if node.parent==None:
		root = to_switch
	else:
		if node==node.parent.left:
			node.parent.left = to_switch
		else:
			node.parent.right = to_switch
	node.parent = to_switch
	return root

def right_rotation(root, node):
	to_switch = node.left
	node.left = to_switch.right
	if node.left != None:
		node.left.parent = node
	to_switch.right = node
	to_switch.parent = node.parent
	if node.parent==None:
		root = to_switch
	else:
		if node==node.parent.right:
			node.parent.right = to_switch
		else:
			node.parent.left = to_switch
	node.parent = to_switch
	return root