import csv
import random
import string
from koder_and_encoder import kode, enkode
from get_binary import get_binary
from main import difference
from noise import nois
from hamming import hammingCorrection, hammingCode

def randomString(stringLength=16):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

algorithm = input("0 - algorytm trójkowy, 1 - kodowanie hamminga\n")
while algorithm.strip() != '0' and algorithm.strip() != '1':
    algorithm = input("Podaj ponownie.\n")

value = input("Podaj ilość iteracji: ")
while value <= "0" or not value.isdigit():
    value = input("Podaj ponownie.\n")

i = int(value)
goodCount = 0

with open('export.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['noOfPackets', 'good', 'broken'])

    for y in range(i):
        for x in range(1000):                       # default noOfPackets=1000
            
            packet = randomString()                 # default string lenght=16, 
                                                    # randomString(x), x - string lenght
            binObj = get_binary('1', packet)
            packetBin = binObj.return_byts()

            if algorithm == '0':
                encoded = kode(packetBin, 8)
            elif algorithm == '1':
                encoded = hammingCode(packetBin, 8)

            noise = nois(encoded)

            if algorithm == '0':
                decoded = enkode(noise, 8)
            elif algorithm == '1':
                decoded = hammingCorrection(noise, 8)

            
            if difference(packetBin, decoded) == 0:
                goodCount += 1

        writer.writerow([1000, str(goodCount), str(1000 - goodCount)])
        goodCount = 0