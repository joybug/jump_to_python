a = [1,2,3]
b = a

a[1]  = 4
print(b)
print(a is b)

a = [1,2,3]
b = a[:]

a[1] = 4
print(b)
print(a is b)

a,b = ('python', 'life')
print(a)
print(b)

#치환
a,b = b,a
print(a)
print(b)

