import os

dk=open("dict.txt","r").read().split('\n')

scmd="curl -k --ntlm -u \"YourUsername:"

ecmd="\" https://yoursite.com"
for s in dk:

	mcmd=s
	print scmd+mcmd+ecmd+" -o "+mcmd+".html"
	os.system(scmd+mcmd+ecmd+" -o "+mcmd+".html")
