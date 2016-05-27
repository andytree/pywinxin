# -*- coding: utf-8 -*-
import sae.const
import MySQLdb
"""sae.const.MYSQL_DB      # 数据库名
sae.const.MYSQL_USER    # 用户名
sae.const.MYSQL_PASS    # 密码
sae.const.MYSQL_HOST    # 主库域名（可读写）
sae.const.MYSQL_PORT    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int
sae.const.MYSQL_HOST_S  # 从库域名（只读）"""

mdb = MySQLdb.connect(host = sae.const.MYSQL_HOST,port = int(sae.const.MYSQL_PORT),user = sae.const.MYSQL_USER,
	passwd = sae.const.MYSQL_PASS,db = sae.const.MYSQL_DB,charset = 'utf8')
cursor = mdb.cursor()
cursor.execute("select * from user ")
results = cursor.fetchall()
data = ''
for row in results:
	data = data + "id = "+ str(row[0]) + "姓名 = "+ row[1].decode('utf-8') + "部门 = "+ str(row[2]) 

mdb.close()