#Ввести число, вывести все его делители.
n = int(input("Введите целое число: "))
i = 1
while i <= n:
	if n % i == 0:
		print (i)
	i = i+1