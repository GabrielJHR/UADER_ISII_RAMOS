import sys
print("Programa que muestra los numeros primos")
# prime number calculator: find all primes up to n
try:
    max = int(sys.argv[1])
    print("Numeros primos hasta", max)
except:
    max = int(input("¿Encuentra los numeros primos hasta? : "))
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
#-------------------------------------------------------------
# prime number calculator: find the first n primes
try:
    count = int(sys.argv[2])
    print(f"Estos son los primeros {sys.argv[2]} numeros primos.")
except:
    count = int(input("¿Cuantos numeros primos quieres encontrar?: "))
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
