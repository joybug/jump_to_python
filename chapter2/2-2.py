a= "I eat %d apples." % 3
print(a)
a= "I eat %s apples." % "five"
print(a)
number = 3
day = "three"
a= "I eat %s apples." % number
print(a)

a= "I eat %s apples." % 5
print(a)

a= "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

a="%0.4f" % 3.42134234
print(a)

a="I eat {0} apples".format(3)
print(a)

a= "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)

a= "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(a)

a="{0:>10}".format("hi")
print(a)
a="{0:<10}".format("hi")
print(a)
a="{0:^10}".format("hi")
print(a)    

a="{0:*>10}".format("hi")
print(a)
a="{0:*<10}".format("hi")
print(a)
a="{0:*^10}".format("hi")
print(a)    

name = '홍길동'
age = 30
a= f"{name}님은 {age}살입니다."
print(a)


a="hobby"
print(a.count('b'))
