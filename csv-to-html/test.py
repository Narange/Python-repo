import random

def get_random_char():
	random_ascii = random.randint(33, 254)
	return str(chr(random_ascii))

for i in range(10):
	for j in range(i):
		print(get_random_char()*j)

