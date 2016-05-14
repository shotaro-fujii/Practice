# coding: utf-8

class Excited_route:

	route_list = []

	def __init__(self, number):
		self.__number = number
		self.__route_list = Excited_route.route_list * self.__number * 3
		self.__route_list = Excited_route.route_list
	
	def set_route(self, gps_data):	
		self.__route_list.extend(gps_data) 
		if len(self.__route_list) - (3*self.__number) >=1:
			del self.__route_list[:(len(self.__route_list) - (3*self.__number))]

	

