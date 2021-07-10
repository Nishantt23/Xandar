from googlesearch import search
from insides.bcolors import bcolors
from bs4 import BeautifulSoup

def Googling(mail,_verbose=None):
	if _verbose != None: 
		print(f"{bcolors.WARNING} -- Searching...{bcolors.ENDC}\n")
		query = "pastebin " + mail
		for j in search(query, tld="co.in", num=10, stop=10, pause=2):
			print(j)
		
