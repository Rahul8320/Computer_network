#!/bin/python3
import os
sum=0

def main():
	global sum
	os.fork()
	for i in range(1,6):
		print("The value of i is ",i)
		sum+=i

	print("The sum is ",sum)

main()
