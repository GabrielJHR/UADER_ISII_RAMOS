import sys
import datetime
print("Programma che visualizza i numeri primi")
# prime number calculator: find all primes up to n
try:
    max = int(sys.argv[1])
    print("Numeri primi fino a", max)
except:
    max = int(input("Trova i numeri primi fino a?: "))
primeList = []
#for loop for checking each number
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList)
print(datetime.datetime.now())
#-------------------------------------------------------------
# prime number calculator: find the first n primes
try:
    count = int(sys.argv[2])
    print(f"Questi sono i primi {sys.argv[2]} numeri primi.")
except:
    count = int(input("Quanti numeri primi vuoi trovare?: "))
primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)
print(datetime.datetime.now())
