import socket
from ping3 import ping
import sys

def pingHost(host:str, timeout):
    resp = ping(host,timeout=timeout)    
    if resp == None:
        return False
    else:
        return True

def pingSweep(network:str, start=0, end=255, timeout=1):
    online = []
    for i in range(start,end+1):
        host = f'{network}.{i}'
        print(f'\rPinging {i-start}/{end-start}', end='')
        try:
            if(pingHost(host, timeout)):
                online.append(host)
        except:
            pass
    return online

def portScanner(host:str, start=1, end=65535, timeout=1):
    openPorts =[]
    for  i in range(start,end+1):
        target = f'{host}:{i}'
        print(f'\rScanning {target}', end='')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
		
        try:
            result = s.connect_ex((host,i))
            if result ==0:
                openPorts.append(i)
            s.close()
        except:
            pass
    return openPorts
            

network = input('Enter network\n')
start = int(input('Enter start host\n'))
end = int(input('Enter end host\n'))
timeout = float(input('Enter timeout duration\n'))

hosts = pingSweep(network,start,end,timeout)
# hosts = portScanner('192.168.60.80', timeout=1)
print('\nList of online hosts - ')

idx = 0
for i in hosts:
    print(f'{idx+1}->{i}\t{socket.gethostbyaddr(i)[0]}')
    idx+=1
    # print(i)

host = int(input('\nEnter host number to scan\n'))

if(idx>len(hosts) or idx<0):
    print("Invalid host")
else:
    ports = portScanner(hosts[host-1])
    print(f'\nOpen ports on host {hosts[host-1]} are-')
    for i in ports:
        print(i)