#!/usr/bin/python3
from time import sleep
import socket
import mechanize
import os
import requests
from colorama import  *

yll = Fore.YELLOW
bl = Fore.BLUE
rd = Fore.RED
wth = Fore.WHITE
dft = Fore.RESET
grn = Fore.GREEN
def sub_scan():
	subs = "subdomains.txt"
	print ()
	host = input(f"{yll}set the host without \"http(s)://\":{dft} ")
	print ("\n\n")
	file = open(subs)
	content = file.read()
	domains = content.splitlines()
	for sdomain in domains:

        	url = f"http://{sdomain}.{host}"

	try:
                requests.get(url)
	except requests.ConnectionError:
		 pass
	else:
           		f = open("lives.txt","a")
           		print (f"{Fore.GREEN}[+] host:{Fore.RED} {url} {Fore.YELLOW} SAVED!")
           		f.write(url + '\n')
           		f.close
def check_rsp():
	url = str(input("url: "))
	rsp = requests.get(url)
	if rsp.status_code == 200:
		print ("\nWeb Funcionando\n")
	elif  rsp.status_code == 404:
		print ("\nERROR 404\n")
	elif rsp.status_code == 403:
		print ("\nERROR 403\n")
	elif rsp.status.code == 500:
		print ("\nERROR 500\n")
	else:
		print ("\nLa Web No Funciona\n")
os.system("clear")


pts = (f"""
     options		        status
    ---------	               --------

+ check response		{grn}ACTIVE{dft}

+ IP Range			{rd}OFF{dft}

+ Port Scanner			{rd}OFF{dft}

+ Search keyword in web		{rd}OFF{dft}

+ Shell				{rd}OFF{dft}

+ Subdomain scanner		{grn}ACTIVE{dft}

+ CVE Exploiter			{rd}OFF{dft}

+ WordPress Exploit Scanner	{rd}OFF{dft}

+ Bug Scanner			{rd}OFF{dft}

[?] Use "cmds" to see the commands
""")
banner = (f"""{bl}.d8888. db    db d8888b. .d8888. d8888b. db       .d88b.  d888888b d888888b 
88'  YP `8b  d8' 88  `8D 88'  YP 88  `8D 88      .8P  Y8.   `88'   `~~88~~' 
`8bo.    `8bd8'  88   88 `8bo.   88oodD' 88      88    88    88       88    
{rd}  `Y8b.  .dPYb.  88   88   `Y8b. 88~~~   88      88    88    88       88    
db   8D .8P  Y8. 88  .8D db   8D 88      88booo. `8b  d8'   .88.      88    
`8888Y' YP    YP Y8888D' `8888Y' 88      Y88888P  `Y88P'  Y888888P    YP
\n\n{dft}""")
def english():
	os.system("clear")
	print (banner)
	while True:

		a = input(f"{yll}fxck{dft}{rd}@{dft}root:~# ")
		sleep(1)

		if a == "help":
			print (pts)
		elif a == "exit":
			break
		elif a == "chk_rsp":
			check_rsp()
		elif a == "banner":
			os.system("clear")
			print (banner)
		elif a == "sub_chk":
			sub_scan()
		else:
			print (f"\n{rd}OPCION NO VALIDA\n{dft}")
			sleep (1)
print (banner)


tls = f"""select the language\n\n
[{grn}√{dft}] eng

\n"""
print (tls)
while True:
	lg = input(">> ")


	if lg == "eng":
		sleep(1)
		english()
		break
	elif lg == "clear":
		sleep(1)
		os.system("clear")
		print (banner)
		print (tls)
	else:
		print (f"\n{rd}ERROR{dft}\n")

