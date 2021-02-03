#connecting the database to the code
import sqlite3

conn = sqlite3.connect('DatabaseFYP.db')
c = conn.cursor()

c.execute("SELECT * FROM People")
conn.commit()
print(c.fetchone())
print(c.fetchall())


#c.execute("CREATE TABLE Random (name VARCHAR(20), colour VARCHAR(20))")
#conn.commit()

#c.execute("CREATE TABLE Admin (Email VARCHAR(35), AdminID INTEGER AUTO_INCREMENT PRIMARY KEY, AUsername VARCHAR(10), APassword VARCHAR(10)")
#conn.commit()
c.execute("SELECT * FROM Admin")
conn.commit()
print(c.fetchone())
print(c.fetchall())