#!/usr/bin/python
import ftplib

def anoncheck(ip):
	try:
		ftp=ftplib.FTP(ip)
		ftp.login('anonymous','anonymous')
		print('\n[+] '+str(ip)+' : Anonymous login Successful')
		ftp.quit()
		return True
	except Exception as e:
		print("\n[-] Failed login.\n"+str(e))
		return False


anoncheck("62.129.198.51")
