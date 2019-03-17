#binarySearchTree

import random

class node:

	#function to initialise node
	def __init__(self, data):
	
		self.leftNode = None
		self.rightNode = None
		self.data = data
	
	#function to insert to node	
	def insert(self, data):
	
		if self.data:
			# insert to leftNode node
			if data < self.data:
				if self.leftNode is None:
					self.leftNode = node(data)
				else:
					self.leftNode.insert(data)
			# insert to rightNode node
			elif data > self.data:
				if self.rightNode is None:
					self.rightNode = node(data)
				else:
					self.rightNode.insert(data)
		# else create root Node if none exist
		else:
			self.data = data
			
	def findValue(self, valueNode):
		if valueNode < self.data:
			if self.leftNode is None:
				return str(valueNode) + ": Not Found"
			return self.leftNode.findValue(valueNode)
		elif valueNode > self.data:
			if self.rightNode is None:
				return str(valueNode) + ": Not Found"
			return self.rightNode.findValue(valueNode)
		else:
			print(str(self.data) + ": Was Found!")
	
	#function to print node	
	def printBinaryTree(self):
		if self.leftNode:
			self.leftNode.printBinaryTree()
		print(self.data)
		if self.rightNode:
			self.rightNode.printBinaryTree()
			
a = random.randint(0,500)
b = random.randint(0,500)
c = random.randint(0,500)
d = random.randint(0,500)
e = random.randint(0,500)
f = random.randint(0,500)
g = random.randint(0,500)
h = random.randint(0,500)
i = random.randint(0,500)
j = random.randint(0,500)
k = random.randint(0,500)
l = random.randint(0,500)
m = random.randint(0,500)
n = random.randint(0,500)
o = random.randint(0,500)
p = random.randint(0,500)
q = random.randint(0,500)
r = random.randint(0,500)
s = random.randint(0,500)
t = random.randint(0,500)
u = random.randint(0,500)
r = random.randint(0,500)
v = random.randint(0,500)
w = random.randint(0,500)
x = random.randint(0,500)
y = random.randint(0,500)
z = random.randint(0,500)

array = [b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,r,v,w,x,y,x]
			
root = node(a)

for i in range(len(array)):
	root.insert(array[i])

#print 1st tree	
#root.printBinaryTree()

#for i in range(0,1999):
#root.insert(random.randint(0,2000))

#root.printBinaryTree()

#will always be found	
print(root.findValue(h))

#maybe found
print(root.findValue(random.randint(0,500)))
print(root.findValue(random.randint(0,500)))
print(root.findValue(random.randint(0,500)))
print(root.findValue(random.randint(0,500)))
print(root.findValue(random.randint(0,500)))
print(root.findValue(random.randint(0,500)))






