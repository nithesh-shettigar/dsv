# Author		: Deepak
# Date			: 31-7-2018
# Some solutions to sample 1 programs

import random

# 1.	Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

def exchange_values( val1, val2):
	val1, val2 = val2, val1
	return val1, val2

# 2.	Python Program to Check Whether a Number is Positive or Negative.
def isPositiveNumber(num):
	return num > -1

# 3.	Python Program to Print all Numbers in a Range Divisible by a Given Number.
# [ if range is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]

def divisibleNumbers(limits, num):
	num_list = []
	for number in range(1, limits + 1):		
		if number % num == 0:
			num_list.append(number)
	return num_list

# 4.	Python Program to Read Two Numbers and Print Their Quotient and Remainder
def quotient_reminder (num1, num2):
	return (num1//num2, num1 % num2)

# 5.	Python Program to Print Odd Numbers Within a Given Range.

def oddNumbers(limits):
	odd_list = []
	for num in range(limits):
		if num % 2 != 0:
			odd_list.append(num)
	return odd_list

# 28.	Write a program to generate 10 random numbers between 1 to 100
# such that there should one number between 1 to 10 one number between 11 to 20 etc.

def randomNumbers():	
	num_list = []
	start = 1
	step = 10
	while len(num_list) < 10:
		num_list.append(random.randint(start, step))
		start = step + 1
		step += 10
	return num_list

def testRandom(numbers):
	start = 0
	end = 10
	for idx in range(len (numbers)):
		assert (start < numbers[idx] <= end)
		start = end
		end = end + 10


