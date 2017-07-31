import pymysql
import contextlib
#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='localhost', port=8701, user='root', passwd='', db='test',charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
    	yield cursor
    finally:
    	conn.commit()
    	cursor.close()
    	conn.close()

with mysql() as cursor:
	print(cursor)