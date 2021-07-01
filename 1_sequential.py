#!/bin/pythopn3

sum=0

def fun():
	global sum
	for i in range(1,6):
		print("The value of i is ", i)
		sum+=i

	print("The sum is ",sum)


fun()
