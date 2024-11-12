#sys 모듈 사용하기
# sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)
'''
위는 프로그램 실행 시 전달받은 인수를 for 문을 사용해 차례대로 하나씩 출력하는 예이다. 
sys 모듈의 argv는 프로그램 실행 시 전달된 인수를 의미한다. 
즉, 다음과 같이 입력했다면 argv[0]은 파일 이름 sys1.py가 되고 
argv[1]부터는 뒤에 따라오는 인수가 차례대로 argv의 요소가 된다.

python sys1.py aaa bbb ccc   이렇게 실행하면

출력결과는 다음과 같다.

aaa
bbb
ccc

'''

# sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
    
'''
sys2.py는 sys1.py와 동일한 함수를 사용하고 
이번에는 대문자로 변환된 인수를 출력하는 예이다.
C:\doit>python sys2.py life is too short, you need python 이렇게 실행하면

출력결과는 다음과 같다.

LIFE IS TOO SHORT, YOU NEED PYTHON
'''
