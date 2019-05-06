import base64

class get_binary:
	"""Converts string or photo file to bits list"""
	def __init__(self, what, number):
		self.what = what # 0 it is a photo 2 is a string
		self.number = number #number of photo
		self.array = []

	def return_byts(self):
		"""Gets bits string and converts them to bits"""
		if self.what == '0':
			self.array = self.image()
		elif self.what == '1':
			self.array = self.striing();
		
		join_array = ''.join(self.array) #joins string list
		self.array = []
		second_array = list(join_array)
		for element in second_array: # appends converted bit to list
			self.array.append(int(element))
		return self.array;

	def image(self):
		"""Get bits form the picture"""
		# Choosing which picture to convert
		if self.number == "1":
			img = 'image/img1.png'
		elif self.number == "2":
			img = 'image/img2.png'
		elif self.number == "3":
			img = 'image/img3.png'
		else:
			return None

		image = open(img, "rb")
		read = image.read()
		bytess = bytearray(read)
		return list('{0:08b}'.format(x, 'b') for x in bytess) #convert byts to bits


	def striing(self):
		"""Convert string to bits"""
		return list('{0:08b}'.format(ord(x), 'b') for x in self.number) #convert string to bits


