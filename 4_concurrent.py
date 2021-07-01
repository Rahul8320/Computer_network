#!/bin/python3

import os

sum=0

def main():
	global sum
	pid = os.fork()
	if pid != 0:
		print("Original Process prints this .")
		print("The process id of child process is : ",pid)
	else:
		print("The new process prints this.")

main()
