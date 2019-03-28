import base64

class get_binary:
	def __init__(self, what, number):
		self.what = what
		self.number = number
		self.array = []

	def return_byts(self):
		if self.what == '0':
			self.array = self.image()
		elif self.what == '1':
			self.array = self.striing();
		
		join_array = ''.join(self.array)
		self.array = []
		second_array = list(join_array)
		for element in second_array:
			self.array.append(int(element))
		return self.array;

	def image(self):
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
		return list('{0:08b}'.format(x, 'b') for x in bytess)


	def striing(self):
		return list('{0:08b}'.format(ord(x), 'b') for x in self.number)


