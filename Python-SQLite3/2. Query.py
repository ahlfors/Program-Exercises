import sqlite3

con = sqlite3.connect('posts.db')



c = con.cursor()    
c.execute('SELECT * from post')
for one in c.fetchall():
    print(one)
    


con.close()
