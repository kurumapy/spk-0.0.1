from termcolor import colored
import socket
import sys

def fanc1():
	color_a = colored("[OPEN] ", 'green')
	color_d = colored("[+] ", 'blue')
	host = input(color_d + "Host --> ")
	port = int(input(color_d + "Port --> "))

	scan = socket.socket()
	
	color_b = colored("[CLOSED] ", 'red')
	color_c = colored("[!] ", 'yellow')
	
	try:
		scan.connect((host, port))
	except scan.error:
		print(color_b, port)
	else:
		print(color_a, port)
def fanc2():
	color_a = colored("[OPEN] ", 'green')
	color_b = colored("[CLOSED] ", 'red')
	color_c = colored("[!] ", 'yellow')
	color_d = colored("[+] ", 'blue')

	host = input(color_d + "Host --> ")
	port = [20, 21, 22, 23, 25, 110, 119, 143, 465, 995, 993, 587, 563, 42, 43, 53, 67, 69, 80, 1030, 8888, 1900, 443, 880, 53, 55, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
	
	for i in port:
		try:
			scan = socket.socket()
			scan.settimeout(0.5)
			scan.connect((host, i))
		except socket.error:
			print(end = '')
		else:
			print(color_a, i)


print("       ")
print(" ____  ____  _  __")
print("/ ___||  _ \| |/ /")
print("\___ \| |_) | ' / ")
print(" ___) |  __/| . \ ")
print("|____/|_|   |_|\_\ ")
print("\t by kuruma")


while True:
	print("           ")
	print("\t1. Scan a single port")
	print("\t2. Scan all ports\n")
	print("\t0. Exit")
	
	color_x = colored("[scan]", 'blue')

	text_a = input(color_x + "--> ")

	if text_a == "0":
		sys.exit()
	elif text_a == "1":
		fanc1()
	elif text_a == "2":
		fanc2()
	else:
		print(colored("Параметр введен не правильно!", 'red'))
