# python program to check if x is a perfect square
   #A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
import math

def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x

def isFibonacci(n):
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

for i in range(1, 11):
	if (isFibonacci(i) == True):
		print(i, "is a Fibonacci Number")
	else:
		print(i, "is a not Fibonacci Number ")
