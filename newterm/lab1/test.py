from tree import *
from binary_tree import *

a = tree('A')
b = tree('B')
c = tree('C')
d = tree('D')
e = tree('E')
f = tree('F')
g = tree('G')
h = tree('H')
i = tree('I')
j = tree('J')
k = tree('K')

a.AddSuccessor(b)
a.AddSuccessor(c)
a.AddSuccessor(d)

b.AddSuccessor(e)
b.AddSuccessor(f)
b.AddSuccessor(g)

c.AddSuccessor(h)
c.AddSuccessor(i)

d.AddSuccessor(j)
d.AddSuccessor(k)
a.Print_DepthFirst()
print(a.Get_LevelOrder())
A = a.ConvertToBinaryTree()
A.Print_DepthFirst()
print(A.Get_LevelOrder())
A = A.ConvertToTree()
A.Print_DepthFirst()
