import socket


ip = input('[+] Ingresa la IP: ')

def scanner(puerto):    
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, puerto))        
        return True
    except:
        return False

for NumeroPuerto in range(1, 1025):
    print("Escaneando puerto:", NumeroPuerto)
    if scanner(NumeroPuerto):
        print('[*] puerto', NumeroPuerto, '/tcp', 'está abierto')
