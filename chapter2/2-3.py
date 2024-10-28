a = [1, 3, 5, 7, 9]
print(a);
print(a[0]);
print(a[1]+a[3]);

a = [1, 2, 3, ['a', 'b', 'c']]

print(a[3])
print(a[-1][2])
#슬라이싱
a = [1, 2, 3, 4, 5]
b = a[::2]

print(b)

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

a = [1, 2, 3]
b = a*3

print(b)

print(len(b))

print(3*"hi")

a = [1,2,3]

del a[1]

print(a)

a = [1, 2, 3, 4, 5]

del a[2:]

print(a)

a = [1,4,5,3,2]

a.sort()

print(a)

a = ['a', 'c', 'b']
a.insert(0,'d')

print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a.remove(3)

a = [1, 2, 3]

print(a.pop())

print(a)

a = [1, 2, 3]

a.extend([4, 5])

print(a)

