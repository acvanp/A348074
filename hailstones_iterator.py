import math
import csv
'''
def bitflip(n): 
	if n == 0 : return 1
	else: return (1 << int.bit_length(n)) - n - 1
'''
def bitflip(n): return (1 << int.bit_length(n)) - n - 1

shortcycle = []
longcycle = []

j = 3
w = ''
n = j
while w != j:
	if n%2 == 0:
		n = bitflip(n)
	else: 
		n = 3 * n + 1
	w = n
	shortcycle.append(n)
print(shortcycle)

j = 27
w = ''
n = j
while w != j:
	if n%2 == 0:
		n = bitflip(n)
	else: 
		n = 3 * n + 1
	w = n
	longcycle.append(n)
print(longcycle)

j = 6469
w = ''
n = j
bigstone = []
for i in range(10000):
	if n%2 == 0:
		n = bitflip(n)
	else: 
		n = 3 * n + 1
	bigstone.append(n)
print(bigstone)


j = 12335
w = ''
n = j
medstone1 = []
for i in range(10000):
	if n%2 == 0:
		n = bitflip(n)
	else: 
		n = 3 * n + 1
	medstone1.append(n)
print(medstone1)

j = 12851
w = ''
n = j
medstone2 = []
for i in range(10000):
	if n%2 == 0:
		n = bitflip(n)
	else: 
		n = 3 * n + 1
	medstone2.append(n)
print(medstone2)

with open("bigstones10kto20k.csv", "a", newline='') as csv_file:
	writer = csv.writer(csv_file)
	for j in range(10000,20001):
		n = j
		m = 0
		c = 0
		pos = c
		ll = {}
		m2 = 0
		while (n not in (shortcycle + longcycle + bigstone + medstone1 + medstone2)) and (n != m):
			if n > m:
				m = n
				maxpos = c
			if n == m2: break
			if c%1000000 == 0:
				m2 = n
				pos = c
				writer.writerow([j, c, n, maxpos, m])
			if n%2 == 0:
				n = bitflip(n)
			else: 
				n = 3 * n + 1
			print(j, c, round(math.log10(n), 0), maxpos, round(math.log10(m), 0))
			c += 1
		print(n, pos, c)
		ll[j] = [j, c, n, maxpos, m]
		writer.writerow([j, c, n, maxpos, m])
		
print(ll)

'''
with open("bigstones.csv", "w") as csv_file:
	writer = csv.writer(csv_file)
	for key, value in ll.items():
		writer.writerow([key, value])
		
'''
