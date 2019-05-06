import os
import io
from PIL import Image

class endcode:
	"""Convert bits to string or file"""
	def __init__(self, what, ansver):
		"""Get bits and packing them by 8 bits and convert to byte and store in list"""
		bytes_in_int = []
		count_low = 0
		for i in range(8,len(ansver)+2, 8):
			bytes_in_int.append(self.make_int(ansver[count_low:i]).to_bytes(1,'big'))
			count_low = i

		self.ansver = bytes_in_int
		self.what = what
		self.array = []
		self.array.append(ansver)

	def make_int(self, tabl):
		"""Creats from 8 bits integer"""
		sume = 0
		po = 0
		for i in reversed(range(len(tabl))):
			sume += tabl[i] * (2 ** po)
			po += 1

		return sume

	def return_string(self):
		"""Creats string or file"""
		if self.what == '0':
			self.array.append(self.image())
			print('otwórz plik result.png')
		else:
			self.array.append(self.string())

		return self.array;

	def image(self):
		"""Joins byts and writs them to png file"""
		word = b''.join(self.ansver)
		fh = open('result.png', "wb")
		fh.write(word)
		fh.close()
		return word

	def string(self):
		"""Decods byts to string"""
		word = ""
		for bit in self.ansver:
			word += bit.decode()

		return word
