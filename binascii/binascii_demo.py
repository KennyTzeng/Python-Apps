import binascii

str = 'abc'
b_str = str.encode('ascii')
# b'abc'

print(type(str), str)
# <class 'str'> abc

print(type(b_str), b_str)
# <class 'bytes'> b'abc'
print(type(b'abc'), b'abc')
# <class 'bytes'> b'abc'

print(type(b_str.decode('ascii')), b_str.decode('ascii'))
# <class 'str'> abc

print(type(binascii.hexlify(b_str)), binascii.hexlify(b_str))
# <class 'bytes'> b'616263'
# accept bytes object, and return bytes object

print(type(binascii.hexlify(b_str).decode('ascii')), binascii.hexlify(b_str).decode('ascii'))
# <class 'str'> 616263
