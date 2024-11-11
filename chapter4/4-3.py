'''
r	읽기 모드: 파일을 읽기만 할 때 사용한다.
w	쓰기 모드: 파일에 내용을 쓸 때 사용한다.
a	추가 모드: 파일의 마지막에 새로운 내용을 추가할 때 사용한다.
'''
#new file
f = open("새파일.txt", 'w')
f.close()

#new file 2
f = open("C:/doit/새파일.txt", 'w')
f.close()

'''
파일 경로와 슬래시(/)
파이썬 코드에서 파일 경로를 표시할 때 "C:/doit/새파일.txt"처럼 슬래시(/)를 사용할 수 있다. 
만약 역슬래시(\)를 사용한다면 "C:\\doit\\새파일.txt"처럼 역슬래시를 2개 사용하거나
r"C:\doit\새파일.txt"와 같이 문자열 앞에 r 문자(raw string)를 덧붙여 사용해야 한다. 
왜냐하면 "C:\note\test.txt"처럼 파일 경로에 \n과 같은 이스케이프 문자가 있을 경우, 줄바꿈 문자로 해석되어 의도했던 파일 경로와 달라지기 때문이다.
'''

# write_data.py
f = open("새파일.txt", 'w',encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()



# readline 함수 사용하기
f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()



#readlines 함수 사용하기
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

#read 함수 사용하기
#f.read()는 파일의 내용 전체를 문자열로 리턴한다.  예의 data는 파일의 전체 내용이다.
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

#파일 객체를 for 문과 함께 사용하기
# read_for.py
f = open("C:/doit/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

#파일에 새로운 내용 추가하기
'''
쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다. 
하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다. 
이런 경우에는 파일을 추가 모드('a')로 열면 된다.
'''
f = open("새파일.txt", 'a',encoding='utf-8')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with 문과 함께 사용하기, close를 자동처리
# 파일객체 f 는 로컬 스코프
with open("새파일.txt", 'w',encoding='utf-8') as f:
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)

with open("새파일.txt", 'a',encoding='utf-8') as f:
    for i in range(11, 20):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)

