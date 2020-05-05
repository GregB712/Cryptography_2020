import random

# Create a random message of "n" bits.
def create_m(n):
    message = []
    for i in range(n):
        bit = bool(random.getrandbits(1))
        if bit == True:
            message.append(1)
        else:
            message.append(0)
    
    return message #returns a list of bits

# Left rotation of a message by n.
def rotate(message, n):
    return message[n:] + message [:n] #returns a list of bits

# XOR function between a message and a key.
def xor(message, key):
    c = [0 for i in range(len(message))]
    for i in range(len(message)):
        temp = 0
        if (message[i] != key[i]):
            c[i] = 1
    
    return c #returns a list of bits

# Message Encryption
m0 = create_m(16) # original message
m6 = rotate(m0, 6)
m10 = rotate(m0, 10)

c0 = xor(m0, xor(m6,m10)) # c = m (+) (m<<6) (+) (m<<10)

print("Original Message: ")
print(m0)

print("Encrypted Message: ")
print(c0)

# Message Decryption
c2 = rotate(c0, 2)
c4 = rotate(c0, 4)
c12 = rotate(c0, 12)
c14 = rotate(c0, 14)
decr = xor(c0, xor(c2, xor(c4, xor(c12,c14)))) # d = c (+) (c<<2) (+) (c<<4) (+) (c<<12) (+) (c<<14)


print("Decrypted Message: ")
print(decr)

print("Original Message: ")
print(m0)