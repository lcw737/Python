import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
                       passwd='1234', db='sample_db', charset='utf8', port=3306)
curs = conn.cursor()


while True:
    print("1. 입력 2. 출력 3. 검색 4. 수정 5. 삭제 6. 종료 ")
    choice = input("메뉴를 선택하세요:")
    if choice == "1":
        print(f"{'입력기능':-^30}")
        sql = f"""INSERT INTO phonebooks (name, phone, addr)
          VALUES('{input('이름:')}','{input('전화번호:')}','{input('주소:')}')"""
        try:
            curs.execute(sql)
            conn.commit()
            print('입력완료!')
        except Exception as e:
            conn.rollback()
            print('쿼리 실행시 오류발생', e)

    elif choice == "2":
        print(f"{'출력기능':-^30}")
        try:
            sql = 'select * from phonebooks'
            curs.execute(sql)
            rows = curs.fetchall()
            print("번호\t이름\t전화번호\t주소")
            for row in rows:
                print('%s       %s   %s        %s' %
                      (row[0], row[1], row[2], row[3]))
        except Exception as e:
            print('쿼리 실행시 오류발생', e)

    elif choice == "3":
        print(f"{'검색기능':-^30}")
        try:
            sql = 'select * from phonebooks where name like "%{0}%" '\
                .format(input('이름을 입력하세요:'))
            curs.execute(sql)
            rows = curs.fetchall()
            print("번호\t이름\t전화번호\t주소")
            for row in rows:
                print('%s       %s   %s        %s' %
                      (row[0], row[1], row[2], row[3]))
        except Exception as e:
            print('쿼리 실행시 오류발생', e)

    elif choice == "4":
        print(f"{'수정기능':-^30}")
        sql = """update phonebooks
            set name = '{1}', phone='{2}' , addr='{3}'
              where name='{0}'""".format(input('수정할 이름:'), input('새로운 이름:'),
                                         input('수정할 번호:'), input('수정할 주소:'))
        try:
            curs.execute(sql)
            conn.commit()
            print('연락처가 수정되었습니다.')
        except Exception as e:
            conn.rollback()
            print('쿼리 실행시 오류발생', e)

    elif choice == "5":
        print(f"{'삭제기능':-^30}")
        iStr = input('삭제할이름:')

        sql = f"delete from phonebooks where name='{iStr}'"

        try:
            curs.execute(sql)
            conn.commit()
            print('정보가 삭제되었습니다.')
        except Exception as e:
            conn.rollback()
            print('쿼리 실행시 오류발생', e)

    elif choice == "6":
        print("프로그램을 종료합니다.")
        conn.close()
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택하세요.")
