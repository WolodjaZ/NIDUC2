
def kode(bytes, size):
	pises_of_bytes = []
	count_high = 0
	count_lower = 0
	for _ in bytes:
		if size == (count_high-count_lower):
			pises_of_bytes.append(bytes[count_lower:count_high])
			count_lower = count_high

		count_high  += 1
	if count_lower != count_high: 
		pises_of_bytes.append(bytes[count_lower:count_high])

	byte = []
	for byte_t in pises_of_bytes:
		koded_byte = []
		for byter in byte_t:
			for _ in range(3):
				koded_byte.append(byter)

		byte.append(koded_byte)


	return byte


def enkode(bytes, size):
	byte_array = []
	for byte_t in bytes:
		unkoded_byte = []
		count = 0

		for num in range(3, len(byte_t)+1, 3):
			sume = sum(byte_t[count:num])
			if sume > 1:
				unkoded_byte.append(1)
			else:
				unkoded_byte.append(0)
			count = num

		byte_array.append(unkoded_byte)

	second_byte_array = []
	for bytess in byte_array:
		for byte in bytess:
			second_byte_array.append(int(byte))

	return second_byte_array
