import os
import io
from PIL import Image

class endcode:
	def __init__(self, what, ansver):
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
		sume = 0
		po = 0
		for i in reversed(range(len(tabl))):
			sume += tabl[i] * (2 ** po)
			po += 1

		return sume

	def return_string(self):
		if self.what == '0':
			self.array.append(self.image())
			print('otwórz plik result.png')
		else:
			self.array.append(self.string())

		return self.array;

	def image(self):
		word = b''.join(self.ansver)
		fh = open('result.png', "wb")
		fh.write(word)
		fh.close()
		return word

	def string(self):
		word = ""
		for bit in self.ansver:
			word += bit.decode()

		return word
