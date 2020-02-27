import nmap
nm = nmap.PortScanner()
results = nm.scan('127.0.0.1', '22,25,80,443')

#print(nm['127.0.0.1']['tcp'][80]) #see specific port
#print(nm.csv())    #view ports in detail
#print(nm['127.0.0.1'].state()) #view host if up


results = nm.scan('192.168.1.6', arguments="-sSV -A -n -T2")  # nmap... arguments
print(results)