import random

def nois(bytes):
	"""Applying nois on signal"""
	bite = []
	for packet in bytes:
		byte = []
		for b in packet: # on each package applies nois
			often = random.randint(0,100) # statiticly on every 1/10 bit nois is applied
			if often > 90:
				data = random.randint(0,1) #applies random value on bit
				if (b+data) == 2:
					b = 0
				else:
					b += data
				often = 0
			byte.append(b)

		bite.append(byte)

	return bite

