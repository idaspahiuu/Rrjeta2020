import socket 
import datetime
import sys
import math
import platform
import random
from _thread import *

#funksioni qe shfaq IP adresen
def IPADDRESS():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    z="IP address: " + str(ip_address)
    sClient.sendall(str.encode(z))
#funksioni i cili shfaq emrin e klientit(metode e zgjedhur)
def NAME():
    hostname=socket.gethostname()
    z="Emri i klientit: "+str(hostname)
    serversocket.sendto(str.encode(z), address)
#funksioni qe shfaq numrin e portit
def PORT():
    z="PORT number: "+ str(addr[1])
    sClient.sendall(str.encode(z))

#funksioni i cili numeron zanoret, bashketingelloret dhe karakteret e veqanta dhe ne fund jep numrin total te karaktereve
def COUNT(a):
    c = 0
    v = 0
    k = 0
    cons=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z"]
    vow=["a","e","i","o","u","y"]
    
    z=str(a).lower()
    for x in z:
        if x in cons:
            c += 1
        elif x in vow:
            v += 1
        else:
            k+=1
    a=('Teksti i pranuar permban %d karaktere'%(c+v+k))
    sClient.sendall(str.encode(a))

#funksioni i cili tregon nese nje tekst eshte apo nuk eshte palindrom
def PALINDROME(s):
    s=str(s)
    z="".join(reversed(s))
    if(z==s):
        t="Teksti eshte palindrom!"
    else:
        t="Teksti nuk eshte palindrom!"
    sClient.sendall(str.encode(t))

#funksioni i cili kthen mbrapsht dhe e shfaq fjalen apo tekstin e dhene
def REVERSE(s):
	s=str(s)
	s="".join(reversed(s))
	sClient.sendall(str.encode(s))

#funksioni i cili shfaq kohen reale 
def TIME():
    koha=datetime.datetime.now()
    z=koha.strftime("%d"+"."+"%m"+"."+"%Y"+" "+"%H"+":"+"%M"+":"+"%S"+"%p")
    sClient.sendall(str.encode(z))

#funksioni i cili zgjedh 7 numra te qfardoshem ne intervalin 1-35 dhe i shfaq ata
def GAME():
	array=[]
	for x in range(7):
		array.append(random.randint(1,35))
	sClient.sendall(str.encode(str(sorted(array))))

#funksioni i cili shfaq pjestuesin me te madh te perbashket te dy numrave te dhene	
def GCF(x,y):
    if int(x) > int(y): 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    z="GCF: " + str(gcd)
    sClient.sendall(str.encode(z))
    
#funksioni ben konvertimin nga nje njesi matese ne tjetren
def CONVERT(z,x):
    z=str(z)
    z=z.strip().upper()
    if(z=="CMTOFEET"):
        ft=int(x)*0.0328084
        ft=round(ft,2)
        z=str(ft)+"ft"
    elif(z=="FEETTOCM"):
        cm=int(x)/0.0328084
        cm=round(cm,2)
        z=str(cm)+"cm"
    elif(z=="KMTOMILES"):
        m=int(x)*0.621371
        m=round(m,2)
        z=str(m)+"miles"
    elif(z=="MILESTOKM"):
        km=int(x)/0.621371
        km=round(km,2)
        z=str(km)+"km"
    else:
        z="Kerkesa nuk eshte valide!"
    sClient.sendall(str.encode(z))

#metodat e zgjedhura

#funksioni prime i cili tregon nese numri eshte i thjeshte apo jo
def PRIME(a):
    if int(a)>1:
        for i in range(2,a):
            if(a%i)==0:
                z="Numri i dhene nuk eshte numer i thjeshte!"
            else:
              z="Numri i dhene eshte numer i thjeshte pasi plotpjestohet vetem me veten dhe numrin 1!"
              sClient.sendall(str.encode(z))

#enkriptimi permes kodit caesar cipher
def ENCRYPT(text,s):
    text=str(text)
    s=int(s)
    result = "" 
  
     
    for i in range(len(text)): 
        char = text[i] 
  
         
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
         
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    sClient.sendall(str.encode(result))

#dekriptimi permes kodit cezar cipher
def DECRYPT(ciphertext, s):
    text=str(ciphertext)
    s=int(s)
    result = "" 
  
     
    for i in range(len(ciphertext)): 
        char = ciphertext[i] 
  
         
        if (char.isupper()): 
            result += chr((ord(char) - s-65) % 26 + 65) 
  
         
        else: 
            result += chr((ord(char) - s - 97) % 26 + 97) 
  
    sClient.sendall(str.encode(result))



def NONE():
     z="Kerkesa jovalide!"
     sClient.sendall(str.encode(z))

def options(op):
    opt=op
    op = op.split()
    response=""
    if(op[0]=="IPADDRESS"):
        IPADDRESS()
    elif(op[0]=="PORT"):
        PORT()
    elif(op[0]=="COUNT"):
        COUNT(opt[6:])
    elif(op[0]=="REVERSE"):
        REVERSE(opt[8:])
    elif(op[0]=="PALINDROME"):
        PALINDROME(opt[11:])
    elif(op[0]=="TIME"):
        TIME()
    elif(op[0]=="GAME"):
        GAME()
    elif(op[0]=="PRIME"):
        PRIME(int(op[1]))
    elif(op[0]=="GCF"):
        GCF(int(op[1]),int(op[2]))
    elif(op[0]=="CONVERT"):
        CONVERT(op[1],op[2])
    elif(op[0]=="ENCRYPT"):
        ENCRYPT(op[1],int(op[2]))
    elif(op[0]=="DECRYPT"):
        DECRYPT(op[1],int(op[2]))
    else:
        NONE()

def clientthread(sClient):
    try:
        while True:
            opsioni = sClient.recv(128).decode()
            options(opsioni)
        sClient.close()
    except:
        print("Ka ndodhur nje gabim gjate marrjes se kerkeses nga klienti!")

serverName ='localhost'
port = 13000
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((serverName, port))
print('--------------------------------------------------------------------------------------------------------------------')
print('FIEK-TCP Protocol - Server.')
print('Port number: '+ str(port))
print('Serveri eshte gati per te pranuar kerkesa.')
print('--------------------------------------------------------------------------------------------------------------------')

while True:
    try:
        serversocket.listen()
        sClient, addr = serversocket.accept()
        print("Klienti eshte lidhur me serverin!"+"\nClient's Port number:"+str(addr[1]))
        start_new_thread(clientthread, (sClient, ))
    except:
        print("Gabimi tek Client socket!")
serversocket.close()
