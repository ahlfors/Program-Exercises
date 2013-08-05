import sqlite3

con = sqlite3.connect('posts.db')
c = con.cursor()

c.execute('''
SELECT name FROM sqlite_master WHERE type='table'
''')

for one in c.fetchall():
    print (one)




c.close()



