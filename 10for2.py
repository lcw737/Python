total = 0
# 1~100까지 반복
for i in range(1,101):
  # 3의 배수 확인
  if i % 3 ==0:
    # 누적해서 더함
    total += i
    # 3의 배수를 줄바꿈 없이 +로 연결해서 출력
    print(i, end='+')
print('\b', '=' , total)

print()
print('='*30)

'''
List Comprehension
: 대괄호 안에 for루프로 반복적인 표현식을 실행해서 리스트의 요소들을
  초기화하는 방법
형식]
  [ 표현식 for 요소 in 컬렉션 [if조건식]]
  if조건식은 경우에 따라 생략할 수 있다.
'''
# 0~9까지의 정수 중 3의 배수의 제곱으로 구성된 리스트를 초기화
list = [n**2 for n in range(10) if n%3==0]
print(list)

print()
print('='*30)

'''
퀴즈] 다음과 같은 메트릭스를 출력하는 프로그램을 for문으로 작성하시오.

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''

for i in range(4):
  for j in range(4):
    if i==j:
      # 행과 열이 동일할때 1출력. 줄바꿈 없이 공백으로 구분
      print('1', end=' ')
    else:
      print('0', end=' ')
  # 한 행을 모두 출력하면 줄바꿈한다.
  print()

print()
print('='*30)
  
'''
퀴즈] 다음과 같은 피라미드를 출력하는 프로그램을 for문으로 작성하시오.

*
**
***
****
*****
'''

for i in range(5):
  for j in range(0,i+1):
    print('*', end='')
  print()
  

# for i in range(1,6):
#   print('*' * i)