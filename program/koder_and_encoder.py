
def kode(bytes, size):
	"""Applies algotrith triplling bits and packing them by size"""
	pises_of_bytes = []
	count_high = 0
	count_lower = 0
	for _ in bytes: # packing bits 
		if size == (count_high-count_lower):
			pises_of_bytes.append(bytes[count_lower:count_high])
			count_lower = count_high

		count_high  += 1
	if count_lower != count_high: #packing rest of bits
		pises_of_bytes.append(bytes[count_lower:count_high])

	byte = []
	for byte_t in pises_of_bytes: #trippling every bits in package
		koded_byte = []
		for byter in byte_t:
			for _ in range(3):
				koded_byte.append(byter)

		byte.append(koded_byte)


	return byte


def enkode(bytes, size):
	"""unpacking bits and decides what bit was in the package"""
	byte_array = []
	for byte_t in bytes: 
		unkoded_byte = []
		count = 0

		for num in range(3, len(byte_t)+1, 3): # sume three bits
			sume = sum(byte_t[count:num])
			if sume > 1: #if sume bigger then 1 it was probably 1
				unkoded_byte.append(1)
			else: # other way it was 0
				unkoded_byte.append(0)
			count = num

		byte_array.append(unkoded_byte) #appends packages

	second_byte_array = []
	for bytess in byte_array: # unpacking bits and converting them from string to integer
		for byte in bytess:
			second_byte_array.append(int(byte)) 

	return second_byte_array
