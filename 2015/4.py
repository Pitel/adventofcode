import hashlib

key = b'bgvyzdsv'
md5 = ''
i = 0

while not(md5.startswith('000000')):
	x = key + bytes(str(i), 'ascii')
	md5 = hashlib.md5(x).hexdigest()
	print(x, md5)
	i += 1
