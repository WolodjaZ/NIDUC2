import random

def nois(bytes):
	bite = []
	for packet in bytes:
		byte = []
		for b in packet:
			often = random.randint(0,100)
			if often > 90:
				data = random.randint(0,1)
				if (b+data) == 2:
					b = 0
				else:
					b += data
				often = 0
			byte.append(b)

		bite.append(byte)

	return bite

