from get_binary import get_binary
from encode import endcode as en
from noise import nois
from koder_and_encoder import kode, enkode
from hamming import hammingCorrection, hammingCode

def main():
  # wybór metody kodowania
  koding_algorithm = input("Podaj '1' jeśli ma być trójkowy algorytm albo podaj '0' jeśli ma być algorytm hamminga ")
  while koding_algorithm.strip() != '0' and koding_algorithm.strip() != '1':
    koding_algorithm = input("Podaj ponownie")

  # wybór co ma być podawane do kodowania
  n = input("Podaj czy chcesz wersje z obrazkiem '0' czy ze stringiem '1' ")
  while n.strip() != '0' and n.strip() != '1':
  	n = input('zla odpowiedz ')


  # jeśli był podany obrazek prosimy o numer od 1-3 a jęsli string to prosimy o podanie słowa
  if n.strip() == '0':
  	drugie = input("podaj numer obrazka ")
  	while drugie.strip() != '1' and drugie.strip() != '2' and drugie.strip() != '3':
  		drugie = input('zla odpowiedz ')
  elif n.strip() == '1':
  	drugie = input("podaj słowo ")

  # wysyłamy dany do get_binary aby na zwrócił ciąg bitów
  incode = get_binary(n, drugie)
  byte = incode.return_byts()

  if byte == None:
  	print("cos poszło nie tak")
  	return

  # pytamy użytkownika co ile mają być pakowane bity, uwzględniając zę poakowanie występuje przed kodowaniem wiec w wypadku
  # potrajania to jeśli użytkownik poda 2 to paczki sygnałów bedą po kodowaniu zapakowane po 3*2 czyli 6
  byte_copy_first = byte
  size = int(input("podaj co ile ma być pakowany sygnał "))

  if koding_algorithm.strip() == '0':
    byte = hammingCode(byte, size)# miejsce na kodowanie drugim algorytmem
  elif koding_algorithm.strip() == '1':
    byte = kode(byte, size)
  else:
    print("Wystąpił bład przeraszamy")
    return

  # podajemy co jaki bit ma być nałożony szum i modyfikujemy nasz sygnał
  trzeci = int(input("podaj co jaki bit ma być szum "))
  byte = nois(byte, int (trzeci))
  
  # odkodujemy nasz sygnał
  if koding_algorithm.strip() == '0':
    byte = hammingCorrection(byte, size) # miejsce na odkowanie drugim algorytmem
  elif koding_algorithm.strip() == '1':
    byte = enkode(byte, size)

  # pokazujemy dane które uzyskaliśmy
  print('Original',byte_copy_first)
  print('Uncoded',byte)
  print('Długość pierwotnego', len(byte_copy_first))
  print('Długosć zmienionego', len(byte))
  print("Tyle liczb z sie zmieniło: ",difference(byte_copy_first ,byte))

  # prubujemy uzyskać zdjecie albo słowo z naszego ciągu bitów
  cos = en(n, byte);
  ansver = cos.return_string()


# metoda która zwraca różnice bitów dwóch tablic i wypisuje ile występuje tych różnic
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