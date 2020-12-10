import sqlite3
import sys

print(sys.argv[1])
conn = sqlite3.connect(sys.argv[1])
cursor = conn.cursor()
cursor.execute('select * from pwdlist')
value = cursor.fetchall()
cursor.close()
print(type(value))
for tp in value:
    print(tp)


