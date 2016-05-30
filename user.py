# -*- coding: utf-8 -*-
import os
import sys

class User(object):
	"""员工的类，包括每个员工识别ID、部门、职位、电话号码、短号、座机号等"""
	def __init__(self ):
		pass

	#'''userId , departId , userName , department , parentdepartment , position , phone ,short ,tel'''
	#获取员工信息的拼接字段
	def getUserInfo(self):
		#部门ID不是0和1的，那么就是二级部室
		userInfo = u'xxx'
		print self.department,self.position
		if self.departId not in ['0','1']:
			userInfo = u'欢迎使用联系人查询功能！\n姓名：' + self.userName
			+ '\n部门：' + unicode(self.parentdepartment ,self)
			'''+
			u'\n部室：' +  self.department + u'\n职位：'+ self.position +
			u'\n手机：' + self.phone + 
			u'\n短号：' + self.short +u'\n机号：' + self.tel'''
		else :
			'''userInfo = u'欢迎使用联系人查询功能！\n姓名：' + self.userName
			+ u'\n部门：' + self.department +
			u'\n职位：' + self.position +
			u'\n手机：' + self.phone + 
			u'\n短号：' + self.short +u'\n机号：'  + self.tel'''
		print userInfo
		return userInfo
		
		
