def suma(a, b):
    binA = bin(int(a, 16))[2:]
    binB = bin(int(b, 16))[2:]
    return hex(int(binA, 2) ^ int(binB, 2))[2:]

# Test example
a = "FA"
b = "CA"
print("suma(a, b):", suma(a, b))


def xtime(a):
    binA = bin(int(a, 16))[2:]
    const = "1B"

    # Ensure the binary number has length 8
    binA = binA.zfill(8)

    if binA[0] == '1':
        binA = binA[1:]
        return suma(hex(int(binA, 2) << 1), const)
    else:
        return hex(int(binA, 2) << 1)[2:]

# Test example
a = "53"
print("xtime(a):", xtime(a))  # Expected output: "a6"

def iloczyn(a, b):
    result = "0"
    binA = bin(int(a, 16))[2:]

    length = len(binA) - 1
    for bit in binA:
        if bit == '1':
            tmp = b
            counter = length
            while counter != 0:
                tmp = xtime(tmp)
                counter -= 1
            result = suma(tmp, result)
        length -= 1
    return result

# Test example
a = "53"
b = "CA"
print("iloczyn(a, b):", iloczyn(a, b))  # Expected output: "01"

def odwrotnosc(a):
    b = a
    i = 13
    const = 1
    while i > 0:
        if i & const == 1:
            tmp = b
        else:
            tmp = a
        b = iloczyn(b, tmp)
        i -= 1
    return b

# Test example
a = "53"
print("odwrotnosc(a):", odwrotnosc(a))  # Expected output: "cd"