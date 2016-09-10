import psycopg2
import sys
from util import Timer

conn = psycopg2.connect(host='localhost', 
                        dbname='claudejaira', 
                        password='552507C!ic')

cursor = conn.cursor()

sql = """INSERT INTO COMPANY (name, age, address, salary) 
        VALUES ('John Jack', 27, 'Clover street, 007, Broklyn', 10000 )"""

with Timer() as t:
    for i in range(10**7):
        cursor.execute(sql)

    conn.commit()
   


print('Elapsed {:f} seconds.'.format(t.secs))

cursor.close()
conn.close()
