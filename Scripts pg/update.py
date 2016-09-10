import psycopg2
from util import Timer

conn = psycopg2.connect(host='localhost', 
                        dbname='claudejaira', 
                        password='552507C!ic')
cursor = conn.cursor()


sql = "UPDATE COMPANY SET SALARY=15000;"

with Timer() as t:
	cursor.execute(sql)
	conn.commit()

print('Elapsed {:f} seconds.'.format(t.secs))

cursor.close()
conn.close()