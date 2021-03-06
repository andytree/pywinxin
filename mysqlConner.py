# -*- coding: utf-8 -*-
import sae.const
import MySQLdb
import user

"""sae.const.MYSQL_DB      # 数据库名
sae.const.MYSQL_USER    # 用户名
sae.const.MYSQL_PASS    # 密码
sae.const.MYSQL_HOST    # 主库域名（可读写）
sae.const.MYSQL_PORT    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int
sae.const.MYSQL_HOST_S  # 从库域名（只读）"""

newuser = user.User()
data = u''
'''cursor.execute("select * from department ")
results = cursor.fetchall()
data = ''
for row in results:
	#data = data + "id = "+ str(row[0]) + "姓名 = "+ row[1].decode('utf-8') + "部门 = "+ str(row[2]) 
	data = data + u"中\n文\n" + str(row[0]) + str(row[2]) + row[1]
mdb.close()'''

mdb = MySQLdb.connect(host = sae.const.MYSQL_HOST,port = int(sae.const.MYSQL_PORT),user = sae.const.MYSQL_USER,
	passwd = sae.const.MYSQL_PASS,db = sae.const.MYSQL_DB,charset = 'utf8')
cursor = mdb.cursor()
#打开数据库连接
'''def open():
	mdb = MySQLdb.connect(host = sae.const.MYSQL_HOST,port = int(sae.const.MYSQL_PORT),user = sae.const.MYSQL_USER,
	passwd = sae.const.MYSQL_PASS,db = sae.const.MYSQL_DB,charset = 'utf8')
	cursor = mdb.cursor()
	return

#关闭数据库连接'''
def close():
	cursor.close()
	mdb.close()
	return

#执行sql，返回结果集
def excecu(ssql):
	cursor.execute(ssql)
	return cursor.fetchall()
#获取用户的ID、姓名、部门id
def getID(uname):
	results = excecu("select id,user_name,depart_id from user where user_name='" + uname + "' or py_name='" + uname+"'")
	#print len(results)
	if len(results) == 0:
		return True
	else : 
		newuser.userId ,newuser.userName ,newuser.departId = str(int(results[0][0])),results[0][1],str(int(results[0][2]))
		return False

#获取用户部门和上级部门
def getDepartInfo():
	#一级部门，不需要查看上级部门
	if newuser.departId in ['0','1']:
		results = excecu("select depart_name from department where id = " + newuser.departId)
		#print results
		newuser.department = results[0][0]
	else :
		results = excecu("select a.depart_name as '部室',b.depart_name as '部门' from department as a, department as b where b.id = a.parent_id and a.id = " + newuser.departId)
		#print results[0][1]
		newuser.department = results[0][0]
		#print newuser.department
		newuser.parentdepartment = results[0][1]
		#print user.department,user.parentdepartment
	return

#获取职位
def getPosition():
	results = excecu("select p.position_name from position as p,user_pos as u where p.id = u.pos_id and u.user_id = " + newuser.userId)
	newuser.position = results[0][0]
	return

#获取手机、短号、座机号
def getPhone():
	results = excecu("select p.phone_num,p.short_num,p.tel_num from phone as p where user_id = " + newuser.userId)
	newuser.phone,newuser.short,newuser.tel = results[0][0],results[0][1],results[0][2]
	return

#获取数据转对象，对象转字符串的数据
def getData(uname):
   	mdb = MySQLdb.connect(host = sae.const.MYSQL_HOST,port = int(sae.const.MYSQL_PORT),user = sae.const.MYSQL_USER,
	passwd = sae.const.MYSQL_PASS,db = sae.const.MYSQL_DB,charset = 'utf8')
   	cursor = mdb.cursor()
	isNone = getID(uname[1:])
	if isNone :
		data = u'查无此人'
	else :
		getDepartInfo()
		getPosition()
		getPhone()
		data = newuser.getUserInfo()
	#close()
	return data
