import sys
import random

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

array = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,r,v,w,x,y,x]

for i in range(len(array)):
	minimum = i
	for j in range(i+1, len(array)):
		if array[minimum] > array[j]:
			minimum = j
			
	array[i], array[minimum] = array[minimum], array[i]
	
for i in range(len(array)):
	print("%d" %array[i])
