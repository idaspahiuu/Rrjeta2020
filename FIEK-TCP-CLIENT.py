
import socket

print('--------------------------------------------------------------------------------------------------------------------')
print('FIEK-TCP Protocol - Client')
print('Server name: localhost' + '\nPort number: ' + str(13000))
print('--------------------------------------------------------------------------------------------------------------------')
print('')
var=input('Doni te ndryshoni te dhenat e serverit?(PO/JO) ')
var=var.upper()
if(var=="PO"):
	serverName=input('Server name: ')
	serverPort=int(input('Port number: '))
else:
	serverName='localhost'
	serverPort=int('13000')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as clientsocket:
    clientsocket.connect((serverName,serverPort))
    while True:
        print(" ")
        print('--------------------------------------------------------------------------------------------------------------------')
        print("Kerkesa nuk mund te permbaje me shume se 128 karaktere!")
        print('--------------------------------------------------------------------------------------------------------------------')
        print('\nOperacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, CONVERT[cmTofeet, feetTocm, kmTomiles, milesTokm], GFC, PRIME, ENCRYPT, DECRYPT)?')
        var=input().upper().encode()
        if var=='':
            break
        clientsocket.sendall(var)
        r=clientsocket.recv(128).decode()
        print(repr(r))