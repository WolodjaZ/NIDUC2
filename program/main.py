from get_binary import get_binary
from encode import endcode as en
from noise import nois
from koder_and_encoder import kode, enkode

def main():

  n = input("Podaj czy chcesz wersje z obrazkiem '0' czy ze stringiem '1' ")
  while n.strip() != '0' and n.strip() != '1':
  	n = input('zla odpowiedz ')
  fh = open('result.png', "wb")
  fh.close()

  if n.strip() == '0':
  	drugie = input("podaj numer obrazka ")
  	while drugie.strip() != '1' and drugie.strip() != '2' and drugie.strip() != '3':
  		drugie = input('zla odpowiedz ')
  elif n.strip() == '1':
  	drugie = input("podaj słowo ")

  incode = get_binary(n, drugie)
  byte = incode.return_byts()

  if byte == None:
  	print("cos poszło nie tak")
  	return

  byte_copy_first = byte
  size = int(input("podaj co ile ma być pakowany sygnał "))

  byte = kode(byte, size)

  trzeci = int(input("podaj co jaki bit ma być szum "))
  byte = nois(byte, int (trzeci))
  
  byte = enkode(byte, size)

  print('Original',byte_copy_first)
  print('Uncoded',byte)
  print('Długość pierwotnego', len(byte_copy_first))
  print('Długosć zmienionego', len(byte))
  print("Tyle liczb z sie zmieniło: ",difference(byte_copy_first ,byte))
  cos = en(n, byte);
  ansver = cos.return_string()


  #print('Opowiedz:')
  #print(ansver[1])


def difference(first, second):
	count = 0
	if len(first) > len(second):
		for i in range(len(second)):
			if first[i] != second[i]:
				count += 1

		count += len(first) - len(second)
	elif len(first) < len(second):
		for i in range(len(first)):
			if first[i] != second[i]:
				count += 1

		count += len(second) - len(first)

	else:
		for i in range(len(first)):
			if first[i] != second[i]:
				count += 1

	return count

  
if __name__== "__main__":
  main()