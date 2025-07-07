import sqlite3

conn = sqlite3.connect('./saveFiles/biography.db')
curs = conn.cursor()
'''
시나리오] 이름이 '강감찬'인 레코드의 급여를 9999로 변경하시오.
'''
print('update')
curs.execute('update people set pay=? where name=?',(9999,'강감찬4'))


'''
시나리오] 급여가 1200인 레코드를 삭제하시오.
'''
print('delete')
curs.execute('delete from people where pay=?',(1200,))

conn.commit()