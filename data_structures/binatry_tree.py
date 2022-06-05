class NodeBT:
	def __init__(self, key=None, left=None, right=None, parent=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent


def count_nodes(root):
	if (root != None):
		count_left = count_nodes(root.left)
		count_right = count_nodes(root.right)
		count = count_left + count_right + 1
		return count
	return 0


def search(root, el):
	if (root != None): 
		if root.key == el:
			return True
		else: 
			if search(root.left, el) == True:
				return True
			else: 
				return search(root.right, el)
	return False


def get_height(root):
	if (root == None):
		return -1
	if ((root.left == None) and (root.right==None)):
		return 0
	height = max(get_height(root.left), get_height(root.right))
	return height + 1

def count_at_level(root, level, current=0):
	if (root == None):
		return 0
	if (level == current):
		return 1
	count_left = count_at_level(root.left, level, current + 1)
	count_right = count_at_level(root.right, level, current + 1)
	return count_left + count_right



import random

def generate_random_binary_tree(max_son, max_key):
	if max_son == 0:
		return None
	tree = NodeBT(random.randint(1, max_key))
	max_son -= 1
	if max_son > 0:
		sons = random.randint(0, max_son)
		tree.left = generate_random_binary_tree(sons, max_key)
		tree.right = generate_random_binary_tree(max_son - sons, max_key)
	return tree
