__author__ = 'Michael E Miles'

# This is also another demonstration of formatting
for i in range(257):
    print("{0:>3} in binary is {0:>09b} in hex is {0:>03x} in Octal is {0:>03o}".format(i))

x = 0x20
y = 0x0a

print(x)
print(y)
print(x * y)

print(0b101010)
