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

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as clientsocket:
    while True:
        print(" ")
        print('--------------------------------------------------------------------------------------------------------------------')
        print("Kerkesa nuk mund te permbaje me shume se 128 karaktere!")
        print('--------------------------------------------------------------------------------------------------------------------')
        print('\nOperacioni (IPADDRESS, PORT, NAME, COUNT, REVERSE, PALINDROME, TIME, GAME, CONVERT[cmTofeet, feetTocm, kmTomiles, milesTokm], GCF, PRIME, ENCRYPT, DECRYPT)?')
        var=input().upper().encode()
        if var=='':
            break

        clientsocket.sendto(var, (serverName, serverPort))
        message, address= clientsocket.recvfrom(128)
        print(repr(message.decode()))
