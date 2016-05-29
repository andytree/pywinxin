class User(object):
<<<<<<< HEAD
	"""员工的类，包括每个员工识别ID、部门、职位、电话号码、短号、座机号等"""
	def __init__(self, userId , departID , userName , departName , parentDepartName , positionName ,
		phoneNum , shortNum ,telNum):
		super(User, self).__init__()
		self.arg = arg
	#获取员工信息的拼接字段
	def getUserInfo():
		#部门ID不是0和1的，那么就是二级部室
		userInfo = ''
		if departID not in [0,1]:
			userInfo = u'欢迎使用联系人查询功能！\n姓名：' + self.userName + u'\n部门：' + self.parentDepartName +
			u'\n部室：' +  self.departName + u'\n职位：' + self.positionName +
			u'\n手机：' + self.phoneNum + u'\n短号：' + self.shortNum + u'\n座机号：' + self.telNum
		else :
			userInfo = u'欢迎使用联系人查询功能！\n姓名：' + self.userName + u'\n部门：' + self.departName +
			u'\n职位：' + self.positionName +
			u'\n手机：' + self.phoneNum + u'\n短号：' + self.shortNum + u'\n座机号：' + self.telNum
		return userInfo
=======
	"""员工的类，包括每个员工部门、职位、电话号码、短号、座机号等"""
	def __init__(self, userName , departName , positionName ,
		phoneNum , shortNum ,telNum):
		super(User, self).__init__()
		self.arg = arg
		
>>>>>>> f44d3ce7f269dfa6073014a640aaafdfa5a4fab7
