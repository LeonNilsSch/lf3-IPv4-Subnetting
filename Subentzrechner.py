import os
import textwrap
import ipaddress

def binaryCalc(ipv):
    listBinary = []
    for i in ipv:
        # Konvertiert die Dezimalzahlen in ihre Binärform
        binary = format(int(i), "08b")
        listBinary.append(binary)
    return listBinary

def point(listBinary, name):
    result = ".".join(listBinary)
    print(name + '\t\t\t', result)
    return result

def dezimalCalc(binary, netmask, name):
    # Berechnet die Binärform der Subnetmaske
    netzmaskeInBinär = "1" * netmask + binary[netmask:]
    netzmaskeInBinärAufteilung = textwrap.wrap(netzmaskeInBinär, width=8)
    
    # Printed die Binär und Deyimalform 
    name_binary = "Subnetzmaske in Binär:\t"
    point(netzmaskeInBinärAufteilung, name_binary)
    
    dezimalzahl = [int(b, 2) for b in netzmaskeInBinärAufteilung]
    name_decimal = "Subnetzmaske in Dezimal:"
    point([str(d) for d in dezimalzahl], name_decimal)

def possibleSubnet(netmask):
    # Berechnet die Anzahl der offenen Bits und möglichen Host
    bits = 32 - netmask
    anzahlSubnetze = (2**bits) - 2
    print('Offene Bits und mögliche Hosts:\t\t\t', str(bits) + ",", anzahlSubnetze)

def minMaxAdress(ip, netmask):
    # Berechnet die kleinste und größte Hostadresse im Subnet
    network = ipaddress.ip_network(ip + '/' + str(netmask), strict=False)
    min_host = network.network_address + 1
    max_host = network.broadcast_address - 1

    print("Kleinste Hostadresse im Subnetz (dezimal):\t", min_host)
    print("Kleinste Hostadresse im Subnetz (binär):\t", format(int(min_host), '032b'))
    print("Größte Hostadresse im Subnetz (dezimal):\t", max_host)
    print("Größte Hostadresse im Subnetz (binär):\t\t", format(int(max_host), '032b'))

if __name__ == "__main__":
    ip = input("IP-Adresse eingeben: ")
    netmask = int(input("Netzmaske eingeben: "))
    ipv = ip.split(".")
    
    if len(ipv) == 4:
        # Führt die Berechnungen aus und gib die Ergebnisse aus
        binary = "00000000000000000000000000000000"
        name = "IP-Adresse in Binär:\t"
        listBinary = binaryCalc(ipv)
        point(listBinary, name)
        dezimalCalc(binary, netmask, name)
        possibleSubnet(netmask)
        minMaxAdress(ip, netmask)
    else:
        print("Ungültige IPv4-Adresse, bitte geben Sie eine neue ein!")
        os.system("python IpCalc_reformed.py")
