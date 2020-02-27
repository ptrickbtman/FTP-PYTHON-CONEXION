import whois 
import os
import nmap
import re
import dns.resolver

nm = nmap.PortScanner()
print("")
def main():
    ip = raw_input('web site or ip:  ')

    ip2 =re.sub('[\.-/()._]','', ip)
    
    if ip2.isalpha():
        result = dns.resolver.query(ip, 'A')
    
        for ipval in result:
            ip= ipval.to_text()
        scanHost(ip)
        scanDNS(ip)
    else:
        scanHost(ip)
    
   

    
def scanHost(ip):
    print ("")
    print("scaneando :" + str(ip))

    
    nm.scan(ip)
    print("scanning port ...")
    for host in nm.all_hosts():
        
        for port in range(20,81):
            if nm[host].has_tcp(port): 
                print ("scanning port " + str(port) + " " + str(host))
                print ("----------------------------------------------")
                print( str(port) + " open" )
                print ("")
                


def scanDNS(ip):
    domain = whois.whois(ip)
    print "[+]Domain: ", domain.domain
    print "[+]Email: ", domain.get('emails')
    print(domain.expiration_date)

    fullInfoWhois = raw_input("get full informacion (y /n):  >>")

    while fullInfoWhois!= 'y' and fullInfoWhois!= 'n':
        raw_input("error data, reintent? (y /n):  >> ")

    if fullInfoWhois == "y":
        createInfo(ip)


def createInfo(ip):
    domain = whois.whois(ip)
    archivo = open('whoisProtocol.json', 'wb')
    archivo.write( str(domain))
    print("report created:" + str(os.getcwd())+"/whoisProtocol.json" )

main()
#scanDNS()