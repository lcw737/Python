'''
퀴즈1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''
kor = int(input('국어점수:'))
eng = int(input('영어점수:'))
math = int(input('수학점수:'))

avg = (kor + eng + math) / 3
print("평균점수는 :", avg)

if avg >= 90:
    print("A학점입니다.")
elif avg >= 80:
    print("B학점입니다.")
elif avg >= 70:
    print("C학점입니다.")
elif avg >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")
    
'''
퀴즈2] 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 패스워드를 입력받아 일치하는지 확인하는 프로그램을 작성하시오. 여기서 패스워드는 1234로 가정합니다. 
'''
user_info = ['hello', 'java', 'python', 'omg']
passwd = '1234'
i_id = input('아이디를 입력하세요 : ')
i_pw = input('비밀번호를 입력하세요 : ')

if i_id in user_info:
  if i_pw == passwd:
    print(i_id,'님 환영합니다.',sep='')
  else:
    print('비밀번호가 틀렸습니다.')
else:
  print('존재하지 않는 계정입니다.')
