# coding: utf-8
import my_route
import weather
import user_table

class Excite_DB:

	def __init__(self):
		self.__excite_data_list = []

	def add_info(self,trigger):
		self.trigger = trigger[0]
		self.excite_level = trigger[1]
		
		if self.trigger == True:
		
			route = my_route.Excited_route(3)
			weather_now = weather.Weather_info()
			user_now = user_table.User_info()
		
			self.__excite_data_list.append(self.excite_level)
			self.__excite_data_list.extend(route.route_list)
			self.__excite_data_list.extend(user_now.get_info())
			self.__excite_data_list.extend(weather_now.get_info())
		
			print self.__excite_data_list
			self.__excite_data_list = []



