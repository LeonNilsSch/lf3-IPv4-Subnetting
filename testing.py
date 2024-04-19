import sys
import os
import textwrap
#eingabe der IPv4 Adresse
#testen meistens bei 192.16.24.2
ip = input("IP-Adresse eingeben: ")
#ip am . teilen
ipv = ip.split(".")
#testen bei Netzmaske ist 24
netmask = int(input("Netzmaske eingeben: "))
binary = "00000000000000000000000000000000"
listBinary=[]
listeNetmaskeDezimal=[]

def ipUmrechnenToBinary(ip,listBinary):
    #loop um in binary zu schreiben
    for i in ipv:
        #formatiere die liste zu binär um
        j = format(int(i), "08b")
        listBinary.append(j)

    ipBinary = listBinary[0]+"."+listBinary[1]+"."+listBinary[2]+"."+listBinary[3]
    print("IP-Adresse:\t\t",ip)
    print("IP-Adresse in Binary: \t",ipBinary)
    return

def netmaskUmrechnenToBinary(netmask,binary):
    # "1"*24 erstellt eine 24 lange Zeichenkette an Einsen. binary[24:] nimmt alle Nullen hinter den 24 Nullen, die zur 1 werden und rechnet diesen an die 24 einsen ran
    netzmaskeInBinär ="1" * netmask + binary[netmask:]

    #der Textwarp Import sorgt dafür, das die Variable netzmaskeInBinär in 8er Bereiche auf
    netzmaskeInBinärAufteilung = textwrap.wrap(netzmaskeInBinär, width=8)

    netzmaskeMitPunktenInBinary = netzmaskeInBinärAufteilung[0]+"."+netzmaskeInBinärAufteilung[1]+"."+netzmaskeInBinärAufteilung[2]+"."+netzmaskeInBinärAufteilung[3]
    print("Netzmaske:\t\t", netmask)

    for i in range(4):
        binärZahlen=netzmaskeInBinärAufteilung[i]
        decimalNumber = int(binärZahlen, 2)
        listeNetmaskeDezimal.append(decimalNumber)

    listenNetzmaskenDezimalMitPunkt = str(listeNetmaskeDezimal[0])+"."+str(listeNetmaskeDezimal[1])+"."+str(listeNetmaskeDezimal[2])+"."+str(listeNetmaskeDezimal[3])
    print("Netzmaske:\t\t",listenNetzmaskenDezimalMitPunkt)
    print("Netzmaske in Binary: \t",netzmaskeMitPunktenInBinary)
    return netzmaskeInBinär

def possibleSubnet(netmask):
    bits = 32-netmask
    anzahlSubnetze=(2**bits)-2
    print(bits, anzahlSubnetze)

def minMaxAdresse():
    i="11111111111000000000000000000000"
    k="00011111111100000111000011110000"
    liste=[]
    for j in range(len(i)):
        if i[j]==k[j]:
            if i[j]!="0":
                liste.append("1")
            else:
                liste.append("0")
        else:
            liste.append("0")
    result = ""
    for element in liste:
        # Füge jedes Element zur resultierenden Zeichenkette hinzu
        result += element
    result2 = textwrap.wrap(result, width=8)
    listeNetmaskeDezimal2=[]   
     
    for i in range(4):
        binärZahlen2=result2[i]
        decimalNumber2 = int(binärZahlen2, 2)
        
        listeNetmaskeDezimal2.append(decimalNumber2)
    print(result)
    print(result2)
    print(listeNetmaskeDezimal2)
    print(i, k)


#prüft, ob eine IPv4 Adresse eingegeben wurde und ansonsten gibt es ein Fehler aus
if len(ipv)==4:
    ipUmrechnenToBinary(ip,listBinary)
    netmaskUmrechnenToBinary(netmask,binary)
    possibleSubnet(netmask)
    minMaxAdresse()
   
else:
    print("ungültige IPv4-Adresse, bitte gebe eine Neue ein!")
    #startet das Programm von Vorne
    os.system("python ipcalc.py")
    
    