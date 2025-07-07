# 모듈 임포트
import pymysql

# 삭제를 위한 함수 선언
def delete_record():
  # MariaDB에 연결하기(포트는 3306이 기본이므로 생략가능)
  conn = pymysql.connect(host='localhost', user='sample_user', port=3306,
                          password='1234', db='sample_db', charset='utf8')
  # 커서 생성
  curs = conn.cursor()
  # 무한루프로 구성
  while True:
    # exit를 입력하는 경우 프로그램 종료
    iStr= input('삭제할일련변호(종료하려면 "exit"입력):')
    # 대문자를 입력하더라도 하나의 조건으로 판단하기 위해 소문자변경
    if iStr.lower() == 'exit':
      print('프로그램을 종료합니다.')
      break
    
    # f-string으로 쿼리문 작성
    sql = f"delete from board where num='{iStr}'"
    
    try:
  # 쿼리문 실행
      curs.execute(sql)
      # MariaDB에 변경사항을 적용
      conn.commit()
      print('1개의 레코드가 삭제됨')
    except Exception as e:
      # 오류가 발생되면 롤백 처리
      conn.rollback()
      print('쿼리 실행시 오류발생', e)
  conn.close()

# 함수 호출하기
delete_record()