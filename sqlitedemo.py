import sqlite3
conn = sqlite3.connect('C:\codes\db.db3')
cursor = conn.cursor()
cursor.execute('select * from pwdlist')
value = cursor.fetchall()
cursor.close()
print(type(value))
for tp in value:
    print(tp)


