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

def ipUmrechnenToBinary(ip,listBinary):
        #loop um in binary zu schreiben
        for i in ipv:
            #formatiere die liste zu binär um
            j = format(int(i), "08b")
            listBinary.append(j)
        ipBinary = listBinary[0]+"."+listBinary[1]+"."+listBinary[2]+"."+listBinary[3]
        print("IP-Adresse:\t\t",ip)
        print("IP-Adresse in Binary: \t",ipBinary)

def netmaskUmrechnenToBinary(netmask,binary):
    # "1"*24 erstellt eine 24 lange Zeichenkette an Einsen. binary[24:] nimmt alle Nullen hinter den 24 Nullen, die zur 1 werden und rechnet diesen an die 24 einsen ran
    netzmaskeInBinär ="1" * netmask + binary[netmask:]
    #der Textwarp Import sorgt dafür, das die Variable netzmaskeInBinär in 8er Bereiche auf
    netzmaskeInBinärAufteilung = textwrap.wrap(netzmaskeInBinär, width=8)

    netzmaskeMitPunktenInBinary = netzmaskeInBinärAufteilung[0]+"."+netzmaskeInBinärAufteilung[1]+"."+netzmaskeInBinärAufteilung[2]+"."+netzmaskeInBinärAufteilung[3]
    print("Netzmaske:\t\t", netmask)
    print("Netzmaske in Binary: \t",netzmaskeMitPunktenInBinary)


    
#def netmaskUmrechnenToIP(netzmaskeInBinärAufteilung):
    #  subnetzmaske = "255." + ".".join(str(int(ipBinary[i:i+8], 2)) for i in range(0, 32, 8))
    #  subnetzmaskeAufteilung = subnetzmaske.split(".")
    #  for i in range(4):
    #      if net
    





   
    
#prüft, ob eine IPv4 Adresse eingegeben wurde und ansonsten gibt es ein Fehler aus
if len(ipv)==4:
    ipUmrechnenToBinary(ip,listBinary)
    netmaskUmrechnenToBinary(netmask,binary)
   
else:
    print("ungültige IPv4-Adresse, bitte gebe eine Neue ein!")
    #startet das Programm von Vorne
    os.system("python ipcalc.py")