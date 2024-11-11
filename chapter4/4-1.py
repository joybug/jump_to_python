#리턴값이 있는 함수
def add(a, b): 
    result = a + b 
    return result

a = add(3, 4)
print(a)

#리턴값이 없는 함수
def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

a = add(3,4)
prtint(a)

#매개변수 지정하여 호출
result = sub(a=7, b=3)  # a에 7, b에 3을 전달
print(result)

#입력값이 몇 개가 될지 모를 때
def add_many(*args): 
     result = 0 
     for i in args: 
         result = result + i   # *args에 입력받은 모든 값을 더한다.
     return result 

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args): 
     if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
         result = 1 
         for i in args: 
             result = result * i 
     return result 

# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
#{'a': 1}
print_kwargs(name='foo', age=3)
#{'age': 3, 'name': 'foo'}
   

#함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b): 
    return a+b, a*b

#매개변수에 초깃값 미리 설정하기
# default1.py
def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("박응용", 27)
 

# 매개변수로 (name, age, man=True)는 되지만, (name, man=True, age)는 안 된다는 것이다. 초기화하고 싶은 매개변수는 항상 뒤쪽에 놓아야 한다는 것을 잊지 말자.


#함수 안에서 선언한 변수의 효력 범위
# vartest.py
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)


# vartest_error.py
def vartest(a):
    a = a + 1

vartest(3)
print(a)

#함수 안에서 함수 밖의 변수를 변경하는 방법
# 1.return 사용하기

# vartest_return.py
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)

# 2. global 명령어 사용하기
# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)

#2. global 명령어 사용하기
# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)

# 람다 사용
add = lambda a, b: a+b
result = add(3, 4)
print(result)

