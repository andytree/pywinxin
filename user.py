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
		#print self.department,self.position,self.parentdepartment
		if self.departId not in ['0','1']:
			userInfo = u'欢迎使用联系人查询功能！\n姓名：' + self.userName+ u'\n部门：'\
			+unicode(self.parentdepartment)+\
			u'\n部室：' + unicode(self.department) + u'\n职位：'+ unicode(self.position) +\
			u'\n手机：' + unicode(self.phone) + \
			u'\n短号：' + unicode(self.short) +u'\n座机号：' + unicode(self.tel)
		else :
			userInfo = u'欢迎使用联系人查询功能！\n姓名：' + self.userName+\
			u'\n部门：' + unicode(self.department) + u'\n职位：'+ unicode(self.position) +\
			u'\n手机：' + unicode(self.phone) + \
			u'\n短号：' + unicode(self.short) +u'\n座机号：' + unicode(self.tel)
		print userInfo
		return userInfo
		
		
