# input 사용하기
# Life is too short, you need python
a = input()
print(a) #Life is too short, you need pythona

#프롬프트를 띄워 사용자 입력받기
#input은 입력되는 모든 것을 문자열로 취급하기 때문에 number는 숫자가 아닌 문자열이라는 것에 주의하자.
number = input("숫자를 입력하세요: ")
print(number)

#큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")  # 1번 lifeistoo short

print("life"+"is"+"too short")  # 2번 lifeistoo short


#문자열 띄어쓰기는 쉼표로 한다
print("life", "is", "too short") #life is too short


#한 줄에 결괏값 출력하기
#end 매개변수의 초깃값은 줄바꿈(\n) 문자이다.
for i in range(10):
    print(i, end=' ') #0 1 2 3 4 5 6 7 8 9 


