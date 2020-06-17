import pymysql
"""
练习 :   创建一个数据库 dict
        创建一个表 words
        将单词本中的单词插入表中
        id     word     mean
"""

db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     passwd = "123456",
                     database = "dict",
                     charset = "utf8"
                     )

cur = db.cursor()

f = open("dict.txt")

for line in f:
    tmp = line.split(' ')
    word = tmp[0]
    mean = ' '.join(tmp[1:]).strip()
    # tup = [word,mean]
    # cur.execute("insert into words (word,mean) values(%s,%s);",tup)

    cur.execute("insert into words (word,mean) values('%s','%s')"%(word,mean))

    db.commit()

cur.close()
db.close()






