import hashlib

with open('day4.txt', 'r') as f:
    key = f.read().strip()

i = 0

while True:
    h = hashlib.new('md5')
    h.update((key + str(i)).encode())
    if h.hexdigest().startswith('00000'):
        break
    i += 1

print('Part 1:', i)

i = 0

while True:
    h = hashlib.new('md5')
    h.update((key + str(i)).encode())
    if h.hexdigest().startswith('000000'):
        break
    i += 1

print('Part 2:', i)
