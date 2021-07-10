from bs4 import BeautifulSoup
import json, requests
from insides.bcolors import bcolors
from googlesearch import search


def Psbdmp(mail,_verbose=None):
	if _verbose != None:
			print(f"{bcolors.WARNING} -- Scanning Pastebin Dumps...{bcolors.ENDC}\n")
			query = "pastebin.com " + mail
			for j in search(query, tld="co.in", num=6, stop=10, pause=2):
				print(j)
		
