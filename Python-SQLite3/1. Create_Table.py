import sqlite3


conn = sqlite3.connect('posts.db')
c = conn.cursor()


#
# 前面的是列名 后面的是类型
#
c.execute('''CREATE TABLE post
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              author text,
              title text,
              content text)
             ''')



conn.commit()
conn.close()

