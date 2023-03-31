import sqlite3

conn = sqlite3.connect('company.db')
print("Connected")

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
       VALUES (1,'Andrew','Allan',21,30000.07, 'Manager')");

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
       VALUES (2,'Martha','Khalid',34,35000.07, 'Secretary')");

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
       VALUES (3,'Saumu','Hanisi',67,34000.07, 'Client')");

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
       VALUES (4,'Brendah','eMobilis',27,30600.07, 'Student')");

conn.commit()
print("Successfully inserted values in Company1 table")

conn.close()