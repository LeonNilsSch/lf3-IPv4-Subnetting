import sys
import os
import textwrap


#eingabe der IPv4 und der Netzmasken Adresse
ip = input("IP-Adresse eingeben: ")
netmask = int(input("Netzmaske eingeben: "))
#ip am Punkt teilen
ipv = ip.split(".")
binary = "00000000000000000000000000000000"

result = ""
name = "IP-Adresse in Binär:\t"
listBinary = []

def binaryCalc(ipv):
    
    for i in ipv:
        #formatiere die liste zu binär um
        j = format(int(i), "08b")
        listBinary.append(j)
    return listBinary


def dezimalCalc(binary,netmask):
    # Berechnet die Binärform der Subnetmaske
    netzmaskeInBinär ="1" * netmask + binary[netmask:]
    netzmaskeInBinärAufteilung = textwrap.wrap(netzmaskeInBinär, width=8)

    #listBinary=netzmaskeInBinärAufteilung
    nameBinär ="Subnetzmaske in Binär:\t"
    point(netzmaskeInBinärAufteilung,nameBinär)

    dezimalzahl = []
    stringListe = []

    #rechnet von Binär in Dezimal um
    for i in range(4):
        binärZahlen=netzmaskeInBinärAufteilung[i]
        decimalNumber = int(binärZahlen, 2)
        dezimalzahl.append(decimalNumber)
    
    # for i in range(4):
    #     dezimalInString = str(dezimalzahl[i])
    #     stringListe.append(dezimalInString)
    nameDezimal ="Subnetzmaske in Dezimal:"
    point(dezimalzahl,nameDezimal)
    return netzmaskeInBinärAufteilung

def point(listBinary,name):
    #füge alle Elemente der Liste mit einem Punkt zusammen
    resultPoint = ".".join(listBinary)
    print(name+'\t',resultPoint)
    return resultPoint


def binärOhnePunkte(binarySubnet):
    resultOhnePoint = "".join(binarySubnet)
    print(resultOhnePoint,"ohnePunkt")
    return resultOhnePoint


def possibleSubnet(netmask):
    bits = 32-netmask
    anzahlSubnetze=(2**bits)-2
    print('Offene Bits und mögliche Hosts:\t',str(bits)+",", anzahlSubnetze)
    


def netzwerkAdresse(subnetmaskOPBinary,ipOPBinary):
    liste=[]
    # AND-Operation (wenn 1 &1 =1 und wen 0&1=0) gibt die Netzwerkadresse aus in Binär
    for j in range(len(subnetmaskOPBinary)):
        if subnetmaskOPBinary[j]==ipOPBinary[j]:
            if subnetmaskOPBinary[j]!="0":
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
    print(ipOPBinary)


def broadcastAddress(ip, sub):
    
    print("max")








#prüft, ob eine IPv4 Adresse eingegeben wurde und ansonsten gibt es ein Fehler aus
if len(ipv)==4:
    #binaryCalc(ipv)
    binaryIP=binaryCalc(ipv)
    point(listBinary,name)
        #dezimalCalc(binary,netmask,name)
    possibleSubnet(netmask)
    binarySubnet=dezimalCalc(binary,netmask)
        #binärOhnePunkte(binarySubnet)
    #das Ergebniss von binärOhnePunkte wird in die Variable resultOhnePunkt gespeicher
    resultOhnePunkt=binärOhnePunkte(binarySubnet)
    binaryIPOhnePunkt=binärOhnePunkte(binaryIP)
    netzwerkAdresse(resultOhnePunkt,binaryIPOhnePunkt)
    broadcastAddress(resultOhnePunkt,binaryIPOhnePunkt)
else:
    print("ungültige IPv4-Adresse, bitte gebe eine Neue ein!")
    #startet das Programm von Vorne
    os.system("python IpCalc_reformed.py")
    