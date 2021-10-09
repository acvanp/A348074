import math
import csv

'''
def bitflip(n): 
    if n==0: return 1
    else: return (1 << int.bit_length(n)) - n - 1
'''
#simplify bitflip for our purposes
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
n = j
bigstones = []
for i in range(100000):
	if n%2 == 0:
		n = bitflip(n)
	else: 
		n = 3 * n + 1
	bigstones.append(n)

bigconnections = []
for j in range(12469, 20000):
    n = j
    c = 0
    for i in range(10000):
        if n%2 == 0:
            n = bitflip(n)
        else: 
            n = 3 * n + 1
        if n in (longcycle + shortcycle): break
        if (n in bigstones):
            bigconnections.append([j,n,c])
            break
        c+=1
    print(j)
        
print(bigconnections)

j=6469
n = j
m = 0
c = 0
m2 = 0 # use this variable as a dragnet for any novel cycles that might arrise
ll = {}
with open("bigstones.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    while (n not in (shortcycle + longcycle)) and (n != m):
        if n > m:
            m = n
            maxpos = c
        if n == m2: break
        if c%1000000 == 0:
            m2 = n
            pos = c
            writer.writerow([j, c, n, m, maxpos])
        if n%2 == 0:
            n = bitflip(n)
        else: 
            n = 3 * n + 1
        print(j, round(math.log10(n), 0), c, round(math.log10(m), 0))
        #numbers are so large you must print the log10(n) 
        #if you with to track the hailstone trajectory in the console
        c += 1
    ll[j] = [j, c, n, m, maxpos]		
    print(ll)


def add1(n):
    return int('1' + bin(n)[2:], 2)

n = 6469
for i in range(20):
    n = bitflip(3*add1(n)+1)
    print(n)


n = 9914
for i in range(20):
    n = add1(n)
    print(n)