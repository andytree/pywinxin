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

mdb = MySQLdb.connect(host = sae.const.MYSQL_HOST,port = int(sae.const.MYSQL_PORT),user = sae.const.MYSQL_USER,
	passwd = sae.const.MYSQL_PASS,db = sae.const.MYSQL_DB,charset = 'utf8')
cursor = mdb.cursor()
newuser = user.User()
data = ''
'''cursor.execute("select * from department ")
results = cursor.fetchall()
data = ''
for row in results:
	#data = data + "id = "+ str(row[0]) + "姓名 = "+ row[1].decode('utf-8') + "部门 = "+ str(row[2]) 
	data = data + u"中\n文\n" + str(row[0]) + str(row[2]) + row[1]
mdb.close()'''
#执行sql，返回结果集
def excecu(ssql):
	cursor.execute(ssql)
	print cursor
	return cursor.fetchall()
#获取用户的ID、姓名、部门id
def getID(uname):
	results = excecu("select id,user_name,depart_id from user where user_name='" + uname + "' or py_name='" + uname+"'")
	print type(results)
	if results == None:
		return True
	else : 
		newuser.userId ,newuser.userName ,newuser.departId = str(int(row[0][0])),row[0][1],str(int(row[0][2]))
		print newuser.departId
		return False

#获取用户部门和上级部门
def getDepartInfo():
	#一级部门，不需要查看上级部门
	if newuser.departId in [0,1]:
		results = cursor.execute("select depart_name from department where id = " + newuser.departId)
		for row in results:
			user.department = row[0]
	else :
		results = cursor.execute("select a.depart_name as '部室',b.depart_name as '部门' from department as a, department as b where b.id = a.parent_id and a.id = " + newuser.departId)
		#print results
		for row in results:
			user.department = row[0]
			user.parentdepartment = row[1]
			print user.department,user.parentdepartment
	return

#获取职位
def getPosition():
	results = cursor.execute("select p.position_name from position as p,user_pos as u where p.id = u.pos_id and u.user_id = " + str(newuser.userId))
	newuser.position = results[0][0]
	return

#获取手机、短号、座机号
def getPhone():
	results = cursor.execute("select p.phone_num,p.short_num,p.tel_num from phone as p where user_id = " + str(newuser.userId))
	newuser.tel,newuser.short,newuser.tel = results[0][0],results[0][1],results[0][2]
	return

#获取数据转对象，对象转字符串的数据
def getData(uname):
	isNone = getID(uname[1:])
	if isNone :
		data = '查无此人'
	else :
		getDepartInfo()
		getPosition()
		getPhone()
		data = newuser.getUserinfo()
	return data
