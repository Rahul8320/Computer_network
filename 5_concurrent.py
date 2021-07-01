#!/bin/python3

import os

def main():
	print("Process ID: ",os.getpid())
	print("Parent Process ID: ",os.getppid())
	pid = os.fork()
	if pid != 0:
		print("Original Process prints this. ")
		print("The process id of child process is: ",pid)
	else:
		print("The new process prints this. ")
		print("Process ID: ", os.getpid())
		print("Parent Process ID: ", os.getppid())


main()
