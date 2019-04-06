# funkcja sprawdzająca ilość bitów parzystości potrzebnych do wygenerowania kodu Hamminga
# zwraca liczbę bitów parzystości które trzeba dodać do zadanego ciągu bitów

def noOfParityBits(noOfBits):
    i = 0
    while 2.**i <= noOfBits + 1:
        i += 1

    return i


# funkcja zwracająca ilość bitów parzystości

def noOfParityBitsInCode(noOfBits):
    i = 0
    while 2.**i <= noOfBits:
        i += 1

    return i

# funkcja dodająca bity (0) do podanej tablicy

def appendParityBits(data):
    n = noOfParityBits(len(data)) # liczba potrzebnych bitów parzystości
    i = 0
    parityBitIndex = 0
    dataBitIndex = 0
    list1 = list()

    while i < n + len(data):
        if i == (2.**parityBitIndex -1):
            list1.insert(i, 0)
            parityBitIndex += 1

        else:
            list1.insert(i, data[dataBitIndex])
            dataBitIndex += 1

        i += 1

    return list1

# funkcja genereująca bity parzystości według kodu Hamminga

def hammingCode(data):
    n = noOfParityBits(len(data))
    list1 = appendParityBits(data)
    i = 0
    parityBitIndex = 1

    while i < n:
        parityBitIndex = 2.**i
        j = 1
        total = 0

        while j*parityBitIndex - 1 < len(list1):
            if j*parityBitIndex - 1 == len(list1) - 1:
                lower_index = j*parityBitIndex - 1
                temp = list1[int(lower_index):len(list1)]

            elif (j+1) * parityBitIndex - 1 >= len(list1):
                lower_index = j * parityBitIndex - 1
                temp = list1[int(lower_index):len(list1)]

            elif (j+1) * parityBitIndex - 1 < len(list1) - 1:
                lower_index = (j*parityBitIndex) - 1
                upper_index = (j+1) * parityBitIndex - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)
            j += 2

        if total % 2 > 0:
            list1[int(parityBitIndex) - 1] = 1

        i += 1

    return list1


# funkcja wykrywająca i naprawiająca błedy w kodzie Hamminga

def hammingCorrection(data):
    n = noOfParityBitsInCode(len(data))
    i = 0
    list1 = list(data)
    print(list1)
    errorBitIndex = 0

    while i < n:
        parityBitIndex = 2.**i
        #currentParityBit = list1[int(parityBitIndex-1)]
        j = 1
        total = 0

        while j*parityBitIndex - 1 < len(list1):
            if j*parityBitIndex - 1 == len(list1):
                lower_index = j * parityBitIndex - 1
                temp = list1[int(lower_index):len(list1)]

            elif (j+1)*parityBitIndex - 1 >= len(list1):
                lower_index = j * parityBitIndex - 1
                temp = list1[int(lower_index):len(list1)]

            elif (j+1) * parityBitIndex - 1 <= len(list1) - 1:
                lower_index = (j*parityBitIndex) - 1
                upper_index = (j+1) * parityBitIndex - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)
            temp = []
            j += 2

        if total % 2 > 0:
            print("Error bit index: ", parityBitIndex)
            errorBitIndex += parityBitIndex

        i += 1

    if errorBitIndex >= 1:
        print("Error in ",errorBitIndex," bit after correction data is ")
        if list1[int(errorBitIndex-1)] == '0' or list1[int(errorBitIndex-1)] == 0:
            list1[int(errorBitIndex-1)] = 1

        else:
            list1[int(errorBitIndex-1)] = 0
    else:
        print("No error")


    list2 = list()
    i = 0
    j = 0
    k = 0

    while i < len(list1):
        if i != ((2**k)-1):
            temp = list1[int(i)]
            list2.append(temp)
            j += 1

        else:
            k += 1

        i += 1

    return list2
















