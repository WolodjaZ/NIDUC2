import random

def nois(bytes, how_offen):
	often = 0
	bite = []
	for byte_first in bytes:
		byte = []
		for b in byte_first:
			often = often+1
			if often == how_offen:
				data = random.randint(0,1)
				if (b+data) == 2:
					b = 0
				else:
					b += data
				often = 0
			byte.append(b)

		bite.append(byte)

	return bite
