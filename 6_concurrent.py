#!/bin/python3

import os

def main():
	print("Process ID: ",os.getpid())
	print("Parent Process ID: ",os.getppid())
	pid = os.fork()
	if pid != 0:
		print("Original Process prints this. ")
		a=20
		b=3
		c = a+b
		print("Sum of a+b is : ",c)
	else:
		print("New process print this.")
		a=20
		b=3
		c=a*b
		print("Multiplication of a*b is : ",c)
		
main()
