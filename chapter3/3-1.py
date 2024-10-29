money = True
if money:
    print("택시를")
    print("타고 가라")
else:
    print("걸어 가라")
#택시를 타고 가라  

'''
 [비교연산자]
 ------------------------
 x < y	    x가 y보다 작다.
 x > y	    x가 y보다 크다.
 x == y	x와 y가 같다.
 x != y	x와 y가 같지 않다.
 x >= y	x가 y보다 크거나 같다.
 x <= y	x가 y보다 작거나 같다.
'''
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
#걸어가라

'''
[ and, or, not ]
 ------------------------
 x or y	x와 y 둘 중 하나만 참이어도 참이다.
 x and y	x와 y 모두 참이어야 참이다.
 not x	x가 거짓이면 참이다.
'''

money = 2000
card = True 
if money >= 3000 or card:
     print("택시를 타고 가라")
else:
     print("걸어가라")    
#택시를 타고 가라

'''
[in, not in]    
   in	         not in
 --------------------------
 x in 리스트	x not in 리스트
 x in 튜플	    x not in 튜플
 x in 문자열	x not in 문자열
'''

'a' in ('a', 'b', 'c')
#True
'j' not in 'python'
#True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
 #택시를 타고 가라   

'''
 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
 이럴 때 사용하는 것이 바로 pass이다.
'''
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")
#pocket 리스트 안에 money 문자열이 있기 때문에 if 문 다음 문장인 pass가 수행되고 아무런 결괏값도 보여 주지 않는다.

'''
[다양한 조건을 판단하는 elif ]
주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
'''
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
#택시를 타고가라

# elif를 사용하면 다음과 같이 바꿀 수 있다.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라")
else:
     print("걸어가라")
#택시를 타고가라

# if 문을 한 줄로 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식
score = 100
if score >= 60:
    message = "success"
else:
    message = "failure"

#파이선 조건부 표현식 으로
message = "success" if score >= 60 else "failure"


'''
# 자료형에서 참과 거짓
------------------------
"python"    참
""          거짓
[1,2,3]     참
[]          거짓
()          거짓
{}          거짓
1           참
0           거짓
None        거짓
'''


