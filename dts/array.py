import random
import copy

class Array:
	# variables
	__array = []
	__length = 0
	# functions
	
	# constructor
	def __init__(self,length=0,randfill=False,arr=[]):
		if(arr != []):
			self.__length = len(arr)
			self.__array = copy.deepcopy(arr)
		else:
			self.__length = length
			self.__array = [None] * length

		if(randfill):
			for i in range(length):
				self.__array[i] = random.randint(0,length)

	# __getitem__ operator
	def __getitem__(self,key):
		if key < 0 or key >= self.__length:
			raise NameError('Index out of bound')
		return copy.deepcopy(self.__array[key])

	# __setitem__ operator
	def __setitem__(self,key,item):
		if key < 0 or key >= self.__length:
			raise NameError('Index out of bound')
		self.__array[key] = copy.deepcopy(item)

	# Get the size of the array
	def length(self):
		return self.__length

	# Print array
	def print(self):
		for i in range(self.__length):
			print(str(self.__array[i])+" ",end="")
		print()

	def copy(self):
		return copy.deepcopy(self)
