import sqlite3


conn = sqlite3.connect('posts.db')
c = conn.cursor()

#
# 增
#
c.execute("INSERT INTO post ('author','title','content') VALUES ('1c7','第一篇日志','早上好')")
conn.commit()

#
# 查
#
c.execute('SELECT * from post')
for one in c.fetchall():
    print(one)



conn.close()






























