s1 = set("hello")
print(s1)
l1 = list(s1)
print(l1)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print( s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s2-s1)
print(s2.difference(s1))

#add
s1 = set([1, 2, 3])
s1.add(4)
s1.update([4, 5, 6])
print(s1)

#remove
s1.remove(4)
print(s1)


