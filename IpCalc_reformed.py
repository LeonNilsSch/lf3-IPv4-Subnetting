import sys
import os
import textwrap


#eingabe der IPv4 und der Netzmasken Adresse
ip = input("IP-Adresse eingeben: ")
netmask = int(input("Netzmaske eingeben: "))
#ip am Punkt teilen
ipv = ip.split(".")
binary = "00000000000000000000000000000000"
listBinary = []
result = ""
name = "IP-Adresse in Binär:\t"

test = ipv

def binaryCalc(test):
    for i in test:
        #formatiere die liste zu binär um
        j = format(int(i), "08b")
        listBinary.append(j)
    return listBinary

def point(listBinary,name):
    result = ""
    i=0
    for element in listBinary:
        i+=1
        if i==4:
            result += element
        else:
            result += element+"."
            # Füge jedes Element zur resultierenden Zeichenkette hinzu
    print(name+'\t',result)
    return result

def dezimalCalc(binary,netmask,name):
    netzmaskeInBinär ="1" * netmask + binary[netmask:]
    netzmaskeInBinärAufteilung = textwrap.wrap(netzmaskeInBinär, width=8)
    listBinary=netzmaskeInBinärAufteilung
    name ="Subnetzmaske in Binär:\t"
    point(listBinary,name)

    dezimalzahl = []
    stringListe = []

    for i in range(4):
        binärZahlen=listBinary[i]
        decimalNumber = int(binärZahlen, 2)
        dezimalzahl.append(decimalNumber)
    
    for i in range(4):
        dezimalInString = str(dezimalzahl[i])
        stringListe.append(dezimalInString)
    listBinary = stringListe
    name ="Subnetzmaske in Dezimal:"
    point(listBinary,name)

def possibleSubnet(netmask):
    bits = 32-netmask
    anzahlSubnetze=(2**bits)-2
    print('Offene Bits und mögliche Hosts:\t',str(bits)+",", anzahlSubnetze)
    

def minMaxAdress():
    print("kleinste und größte")
















#prüft, ob eine IPv4 Adresse eingegeben wurde und ansonsten gibt es ein Fehler aus
if len(ipv)==4:
    binaryCalc(test)
    point(listBinary,name)
    dezimalCalc(binary,netmask,name)
    possibleSubnet(netmask)
else:
    print("ungültige IPv4-Adresse, bitte gebe eine Neue ein!")
    #startet das Programm von Vorne
    os.system("python IpCalc_reformed.py")
    