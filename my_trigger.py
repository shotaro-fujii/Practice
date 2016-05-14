# coding: utf-8
import random
import lap_db

class Excited_trigger:

	def __init__(self):
		self.__excite_level = 0
		self.__flag = [False, 0]

	def make_trigger(self):
		self.__excite_level = random.randint(0, 100)
		if self.__excite_level > 90:
			self.__flag = [True, self.__excite_level]			
		else:
			self.__flag = [False, self.__excite_level]
			
	def send_trigger(self):

		db = lap_db.Excite_DB()
		db.add_info(self.__flag)
