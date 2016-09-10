import psycopg2

conn = psycopg2.connect(host='localhost', 
                        dbname='claudejaira', 
                        password='552507C!ic')
cursor = conn.cursor()

sql = """CREATE TABLE COMPANY(
   id SERIAL PRIMARY KEY     NOT NULL,
   name           TEXT    NOT NULL,
   age            INT     NOT NULL,
   address        CHAR(50),
   salary         REAL
);"""

cursor.execute(sql)

conn.commit()

cursor.close()
conn.close()