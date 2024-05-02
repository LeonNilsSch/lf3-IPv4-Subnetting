import os
import textwrap
 

#Eingabe der IPv4 und der Netzmasken Adresse
ip = input("IPv4-Adresse eingeben:\t\t")
netmask = int(input("Netzmaske eingeben:\t\t"))

#Ip am Punkt teilen
ipv = ip.split(".")


#Die Variable "name" wird erstellt, um einer nachfolgenden Funktion diesen zu übergeben
name = "IP-Adresse in Binär:\t"
listBinary = []
eingabeSymetrisch=""

 
#Rechnet von Dezimal in Binär um
def binaryCalc(ip):
    ipv = ip.split(".")
    for i in ipv:
        #Formatiert die Liste in binär um, also in vier achter Stücke
        j = format(int(i), "08b")
        listBinary.append(j)
    #Gibt Liste mit den Binären Zahlenblöcken aus
    return listBinary

#Berechnet die Binärform der Subnetmaske
def netzmaskenBinär(netmask):
    binary = "00000000000000000000000000000000"
    #Erschafft eine Zeichenkette aus 0 und 1 anhand der Subnetzmaske
    netzmaskeInBinär ="1" * netmask + binary[netmask:]

    #Teilt die Zeichenkette in 4 Teile, á 8 Stellen
    netzmaskeInBinärAufteilung = textwrap.wrap(netzmaskeInBinär, width=8)
    nameBinär ="Subnetzmaske in Binär:\t"

    #Die Liste mit der aufgeteilten Subnetzmaske wird an die Funktion "point()"weitergegeben, um die Subnetzmaske in Binär auszugeben.
    #Zu dem wir der Text für die Ausgabe mit übergeben
    point(netzmaskeInBinärAufteilung,nameBinär)

    #Gibt den String aus 1 und 0 weiter
    return netzmaskeInBinär

#Rechnet Binär in Dezimal um
def dezimalCalc(result,ausgabeName):
    dezimalzahl = []
    #Teilt den übergebenen String in 4 Teile
    netzmaskeInBinärAufteilung = textwrap.wrap(result, width=8)

    #Rechnet von Binär in Dezimal um
    for i in range(4):
        binärZahlen=netzmaskeInBinärAufteilung[i]
        decimalNumber = int(binärZahlen, 2)
        #Fügt den Integer in eine Liste ein
        dezimalzahl.append(decimalNumber)

    #Der übergebende Text wird der Funktion übergeben
    #Die Liste mit den Dezimalzahlen wird and die Funktion "point()" übergeben
    point(dezimalzahl,ausgabeName)
    #Gibt die Liste mit den Dezimalzahlen weiter
    return dezimalzahl

   
def point(liste,name):
    #Füge alle Elemente der Liste mit einem Punkt zusammen
    #Und wandelt es vorher in einen String um, so dass es zusammengefügt werden kann
    for i in range(4):
        liste[i]=str(liste[i])
    
    #".join" sorgt dafür, das alle Elemente einer Liste mit einen Punkt zusammengefügt werden
    resultPoint = ".".join(liste)
    print(name+'\t',resultPoint)


#Fügt eine Liste aus Strings ohne Punkt zusammen
def ohnePunkte(binarySubnet):
    #Fügt den Inhalt einer Liste ohne Punkt zusammen
    resultOhnePoint = "".join(binarySubnet)
    return resultOhnePoint

#Erstellt die Netzwerkmaske in Binär
def netzwerkAdresse(subnetmaskOPBinary,ipOPBinary):
    liste=[]
    #AND-Operation (wenn 1 &1 =1 und wenn 0&1=0) gibt die Netzwerkadresse aus in Binär
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
        #Füge jedes Element zur resultierenden Zeichenkette hinzu
        result += element
    return result

 
#Berechnet die Broadcast-Address in Binär
def broadcastAddress(netwerkAdresseBinär,netmask):
    übriggebliebeneBits=32-netmask
    #Nimmt die Netzwerkadresse in Binär ohne Punkt und setzt die Anzahl an Bits auf 0, die nicht von der Subnetzmaske betroffen sind.
    #Wichtig ist, das Ergebnis von "übriggebliebeneBits" wird von hinten gezählt.
    netwerkAdresseBinär = netwerkAdresseBinär[:-übriggebliebeneBits] + "1" * übriggebliebeneBits

    return netwerkAdresseBinär

 
#Rechnet die mögliche Anzahl an Blöcken aus und die Anzahl der Hostadressen
def BlockanzahlUBlockHostgröße(vlsm,netmask):
    Hostbits=32-vlsm #VLSM Nummer
    berechnungAnzahlBitsMöglichkeitenImBlock=(2**Hostbits)#Nur immer bei 0 - 1,da die IP Adressen bei 0 anfangen

    subnetzbits=vlsm-netmask #VLSM Bits - Subnetzmaskenbits
    möglicheSubnetzte=2**subnetzbits

    gesamtnetzgröße=2**(32-netmask)#Alle Bits (32)- Subnetzmaskenbits
    subnetzgröße =gesamtnetzgröße/möglicheSubnetzte

    anzahlDerBlöcke=gesamtnetzgröße//subnetzgröße
    print("Blockanzahl\t\t\t",anzahlDerBlöcke)
    print("Subnetzgröße\t\t\t",subnetzgröße)
    
    return berechnungAnzahlBitsMöglichkeitenImBlock,gesamtnetzgröße,anzahlDerBlöcke

#Rechnet die kleinste und größste IP-Adresse in einem Block aus
def kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste):
    for i in range(0,3): #Nur bis 2, da 3 anders berechnet wird
        ipkleinste[i]=broadcastadresse[i]
        ipGrößste[i]=broadcastadresse[i]

    ipkleinste[3]=netzwerkadresseListe[3]+1
    ipGrößste[3]=broadcastadresse[3]-1

    return ipkleinste, ipGrößste

 
#Setzt den gewünschten Teil der IP-Adresse auf 0 zurück und erhöht einen gewünschten Teil der IP-Adresse (wird zur Berechnung von "symetrischesNetzwerk()" gebraucht)
def nullSetzten(start, ende, blockNr, berechnungAnzahlBitsMöglichkeitenImBlock, broadcastadresse, netzwerkadresseListe):
    for i in range(start, ende):
        broadcastadresse[i] = 0
        netzwerkadresseListe[i] = 0

    broadcastadresse[blockNr] += 1   #Erhöhung des Zahlenblocks um +1
    netzwerkadresseListe[blockNr] += 1

    broadcastadresse[3] = broadcastadresse[3] + berechnungAnzahlBitsMöglichkeitenImBlock -1 #Rechnet die Broadcastadresse aus (aktuelle + anzahl Bits -1, weil es der erste ist und die 0 beachtet werden muss)

##Setzt den gewünschten Teil der IP-Adresse auf 255  und erhöht einen gewünschten Teil der IP-Adresse (wird zur Berechnung von "symetrischesNetzwerk()" gebraucht)
def Zahl255Setzten(größer,start,ende,broadcastadresse,netzwerkadresseListe):
    for i in range(start, ende):
        broadcastadresse[i] = 255
    broadcastadresse[start-1]=int(broadcastadresse[start-1])+größer
    netzwerkadresseListe[3]=0

#Gibt und rechnet die möglichen Hostblöcke mit VLSM aus
def symetrischesNetzwerk(netzwerkAdresseDezimal,subnetzmaskeDezimal,berechnungAnzahlBitsMöglichkeitenImBlock,broadcastadresseDezimal):
    #Fügt den von der Funktion übergebenen Wert in die Variablen ein
    netzwerkadresseListe=netzwerkAdresseDezimal[:]
    broadcastadresse=netzwerkAdresseDezimal[:]
    subnetzMaske=subnetzmaskeDezimal[:]
    ipkleinste=netzwerkadresseListe[:]
    ipGrößste=netzwerkadresseListe[:]
    bitAnzahl=berechnungAnzahlBitsMöglichkeitenImBlock[0]
    blockanzahl=int(berechnungAnzahlBitsMöglichkeitenImBlock[2])
    listenposition=3

    
    
    
    point(netzwerkAdresseDezimal,"Netzwerkadresse:\t")
    point(broadcastadresseDezimal,"Größste Broadcastadresse:")
    print(end="\n")

    for i in range(4):
        broadcastadresse[i]=int(broadcastadresse[i])
        netzwerkadresseListe[i]=int(netzwerkadresseListe[i])

    #Fragt, ob wirklich alle Möglichkeiten ausgegeben werden sollen
    allesAusgeben = input("Sollen alle möglichkeiten ausgegeben werden? ")
    if allesAusgeben=="Ja"or allesAusgeben=="ja"or allesAusgeben=="j":
        #Wenn ja, wird die Variable Netzgröße = der wahren Netzgröße, gesetzt
        netzgröße=berechnungAnzahlBitsMöglichkeitenImBlock[1]/bitAnzahl
        netzgröße=blockanzahl

    else:
        #Wenn nicht, wird die Variable auf 4 gesetzt und die kleinste Netzwerkadresse und die höchste Broadcastadresse wird ausgegeben
        print("Es werden die ersten 4 Ausgegeben!",end="\n\n")
        netzgröße=4
        blockanzahl=4

    
    if bitAnzahl>=255:
        for i in range(blockanzahl):
            #Berechnung der Zahl die plus gerechnet werden soll
            größer255E=bitAnzahl//255
            größer255Z=größer255E//255
            größer255D=größer255Z//255
            
            #Prüft, ob die grade Erhöht Position in der IP-Adresse, kleiner ist als die passende Position in der größsten Broadcastadresse
            if broadcastadresse[listenposition] < int(broadcastadresseDezimal[listenposition]) and listenposition < 3:
                netzwerkadresseListe[3]=0
                netzwerkadresseListe[listenposition]=broadcastadresse[listenposition]+1
                broadcastadresse[listenposition]=broadcastadresse[listenposition]+vergrößern
                print(vergrößern)

            elif broadcastadresse[listenposition] >= int(broadcastadresseDezimal[listenposition]) and listenposition <= 3:
                exit()

            #Prüft, ob die "bitAnzahl" kleiner ist als 255 und wenn ja, ob die Variable "größer255E" kleiner ist als gleich 255 ist
            elif bitAnzahl>=255 and größer255E<=255:
                if i==0:
                    #da man bei Null startet, rechnet man -1
                    größer255E-=1
                #"Zahl255Setzten()" setzt die Broadcastadresse in Bestimmten Listen Teilen auf 255 und die Netzwerkadresse auf der dritten Position auf 0
                Zahl255Setzten(größer255E,3,4,broadcastadresse,netzwerkadresseListe)
                #"vergrößern" übergibt die Variable, die Zahl beinhaltet, welche die Vergrößerung bestimmt. Und rechnet +1, da nur wegen der kleinsten Netzwerkadresse -1 gerechnet wurde
                vergrößern=größer255E+1
                #Gibt die Listenposition an, welche vergrößert wird
                listenposition=2
            
            elif größer255E>= 255 and  größer255Z <= 255:
                print(größer255Z)
                if i==0:
                    #da man bei Null startet, rechnet man -1
                    größer255Z-=1
                #"Zahl255Setzten()" setzt die Broadcastadresse in Bestimmten Listen Teilen auf 255 und die Netzwerkadresse auf der dritten Position auf 0
                Zahl255Setzten(größer255Z,2,4,broadcastadresse,netzwerkadresseListe)
                #"vergrößern" übergibt die Variable, die Zahl beinhaltet, welche die Vergrößerung bestimmt. Und rechnet +1, da nur wegen der kleinsten Netzwerkadresse -1 gerechnet wurde
                vergrößern=größer255Z+1
                #Gibt die Listenposition an, welche vergrößert wird
                listenposition=1

            elif größer255Z>=255 and größer255D<=255:
                if i==0:
                    #da man bei Null startet, rechnet man -1
                    größer255D-=1
                #"Zahl255Setzten()" setzt die Broadcastadresse in Bestimmten Listen Teilen auf 255 und die Netzwerkadresse auf der dritten Position auf 0
                Zahl255Setzten(größer255D,1,4,broadcastadresse,netzwerkadresseListe)
                 #"vergrößern" übergibt die Variable, die Zahl beinhaltet, welche die Vergrößerung bestimmt. Und rechnet +1, da nur wegen der kleinsten Netzwerkadresse -1 gerechnet wurde
                vergrößern=größer255D
                #Gibt die Listenposition an, welche vergrößert wird
                listenposition=0

            #Ausgabe der Adressen in Dezimal mit Punkt
            print("Hostblock:",i+1)
            point(netzwerkadresseListe,"Netzwerkadresse:\t")

            netzwerkadresseListe[3]=int(netzwerkadresseListe[3])

            #Berechnung der kleinsten und größsten IP-Adresse
            ipkleinste=netzwerkadresseListe
            ipkleinste[3]=netzwerkadresseListe[3]+1
            
            ipGrößste=broadcastadresse
            ipGrößste[3]=broadcastadresse[3]-1

             #Ausgabe der Adressen in Dezimal mit Punkt
            point(ipkleinste,"Kleinste IP-Adresse:\t")
            point(ipGrößste,"Größe IP-Adresse:\t")
            broadcastadresse[3]=int(broadcastadresse[3])+1
            point(broadcastadresse,"Broadcastadresse:test\t")
            print(end="\n")

            #"point()" ändert die Variablen in einen String um. Deswegen wird hier, zum weiteren berechnen der Adressen, diese wieder in einen Integer umgewandelt
            for i in range(4):
                netzwerkadresseListe[i]=int(netzwerkadresseListe[i])
                ipkleinste[i]=int(ipkleinste[i])
                ipGrößste[i]=int(ipGrößste[i])
                broadcastadresse[i]=int(broadcastadresse[i])
                
    else:
        

        for i in range(netzgröße):  #Netzgröße= Anzahl der möglichen Blöcke
            
            #"point()" ändert die Variablen in einen String um. Deswegen wird hier, zum weiteren berechnen der Adressen, diese wieder in einen Integer umgewandelt
            for j in range(4):
                netzwerkadresseListe[j]=int(netzwerkadresseListe[j])
                ipkleinste[j]=int(ipkleinste[j])
                ipGrößste[j]=int(ipGrößste[j])
                broadcastadresse[j]=int(broadcastadresse[j])
                subnetzMaske[j]=int(subnetzMaske[j])

            if broadcastadresse[3] == 0:
                #Berechnung der Broadcastadresse, Netzwerkadresse, und "kleinerGroß()". Die Broadcastadresse wir hier -1 Gerechnet, da die erste Netzwerkadresse immer mit 0 anfängt
                broadcastadresse[3]+=bitAnzahl - 1
                netzwerkadresseListe[3]=0
                kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)

            elif subnetzMaske[0] ==255 and broadcastadresse[3]==broadcastadresse[2]==broadcastadresse[1]==255 or broadcastadresse[0]==255 or subnetzMaske[1] ==255 and broadcastadresse[3]==broadcastadresse[2]==255 or subnetzMaske[2] ==255 and broadcastadresse[3]==255:
                #Sorgt für ein Ende der For-Schleife und beendet die Ausführung, wenn entweder die Broadcastadresse auf 255.255.255.255 ist oder wenn die Subnetzmaske erreicht wird
                exit() 

            elif broadcastadresse[3] == 255 and broadcastadresse[2] == 255 and broadcastadresse[1] == 255 and subnetzMaske[0] < 255:
                #Rechnet beim ersten IP-Teil +1 und setzt den Rest auf 0 zurück, um die weiteren Adressen zu berechnen
                nullSetzten(1,4,0,bitAnzahl,broadcastadresse,netzwerkadresseListe)#1.Startwert, 2. Endwert, 3. ZahlenblockNr der Adresse
                kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)

            elif broadcastadresse[3] == 255 and broadcastadresse[2] == 255 and subnetzMaske[1] < 255:
                #Rechnet beim zweiten IP-Teil +1 und setzt den Rest auf 0 zurück, um die weiteren Adressen zu berechnen
                nullSetzten(2,4,1,bitAnzahl,broadcastadresse,netzwerkadresseListe)#1.Startwert, 2. Endwert, 3. ZahlenblockNr der Adresse
                kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)

            elif broadcastadresse[3] == 255 and subnetzMaske[2] < 255:
                #Rechnet beim dritten IP-Teil +1 und setzt den Rest auf 0 zurück, um die weiteren Adressen zu berechnen
                nullSetzten(3,4,2,bitAnzahl,broadcastadresse,netzwerkadresseListe)#1.Startwert, 2. Endwert, 3. ZahlenblockNr der Adresse
                kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)

            else:
                #Rechnet die Netzwerkadresse, Broadcastadresse und die kleinerGroß Adresse aus.
                netzwerkadresseListe[3]=broadcastadresse[3]+1 #Netzwerkadresse= alte Broadcastadresse +1 auf den letzten IP-Zahlenblock
                broadcastadresse[3] += bitAnzahl #broadcastadresse = alte Broadcastadresse + Anzahl der möglichen Bits (32-VLSM=anzahlmöglicher Bits)
                kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)
                #Netzwerkadresse hier hinzufügen!
                
            print("Hostblock:",i+1)
            #Ausgabe der Adressen in Dezimal mit Punkt
            point(netzwerkadresseListe,"Netzwerkadresse:\t")
            point(ipkleinste,"Kleinste IP-Adresse:\t")
            point(ipGrößste,"Größe IP-Adresse:\t")
            point(broadcastadresse,"Broadcastadresse:\t")
            print(end="\n")

            

#Gibt und rechnet die gewünschten Asymetrischen Blöcke aus
def asymetrisch(netzwerkadresse,subnetzmaskeDezimal):
    #Fragt ab, wie viele Unterteilungen des Netzwerk man haben möchte
    #Ergbenis des Inputs wird in einen Integer umgewandelt.
    unterteilung= int(input("Wie oft soll es unterteilt werden? " ))
    angaben=[]
    reservierteBits=[]
    #Die übergebenen Inhalte beim Funktionsaufruf, werden in den Variablen gespeichert
    broadcastadresse=netzwerkadresse[:]
    ipkleinste=netzwerkadresse[:]
    ipGrößste=netzwerkadresse[:]
    netzwerkadresseListe=netzwerkadresse[:]
    subnetzmask=subnetzmaskeDezimal[:]
    #Gibt alle möglichen Dezimalzahlen an
    bits=[255,128,64,32,16,8,4,2,1]

    #Schleife, um die Größe der benötigten Hostadressen abzufragen.
    for i in range(unterteilung):
        i+=1
        anzahlDerDurchgänge=str(i)
        eingabeDerGröße=int(input("Bitte gebe die Hostgröße der "+anzahlDerDurchgänge+". Unterteilung an. " ))
        #Fügt die eingegebenen Zahlen in eine Liste ein
        angaben.append(eingabeDerGröße)

    #Sucht die entsprechenden Bits Anzahl für eingegegebende Zahl raus. Entwerder die nächste Höhere oder die genau gleiche
    for i in range(len(angaben)):
        #Da die Netzwerkadresse und die Broadcastadresse nicht als Hostmitgezählt wird, sollte + 2 gerechnet werden
        angaben[i]=angaben[i]+2

        #Prüft, ob die Zahl kleiner 4 oder größer 255 ist, um nicht mögliche 
        if angaben[i]>255:
            print("Bitte gebe die Zahlen nochmal ein! Die Bits dürfen nicht größer 255 sein")
            asymetrisch(netzwerkadresse,subnetzmaskeDezimal)

        #Fügt die nächst höheren Bits in eine Liste ein. Die Bits 1 und 2 werden nicht genutzt, da diese keine Hostadressen bereitstellen
        elif angaben[i]<=bits[6]:
            reservierteBits.append(4)

        elif angaben[i]<=bits[5]:
            reservierteBits.append(8)

        elif angaben[i]<=bits[4]:
            reservierteBits.append(16)

        elif angaben[i]<=bits[3]:
            reservierteBits.append(32)

        elif angaben[i]<=bits[2]:
            reservierteBits.append(64)

        elif angaben[i]<=bits[1]:
            reservierteBits.append(128)

        else:
            reservierteBits.append(255)

    #Berechnet die Broadcastadresse, Netzwerkadresse und die kleinste und größste Hostadresse, aber Broadcastadresse-1, da sonst zu viele Bits vergeben werden (Netzwerkadresse startet bei 0)
    for i in range(len(angaben)):
        for j in range(4):
            netzwerkadresseListe[j]=int(netzwerkadresseListe[j])
            ipkleinste[j]=int(ipkleinste[j])
            ipGrößste[j]=int(ipGrößste[j])
            broadcastadresse[j]=int(broadcastadresse[j])

        if i==0:
            broadcastadresse[3]=broadcastadresse[3]+reservierteBits[i]-1
            kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)

        #Prüft, ob der Subnetzbereich mit verändert werden würde. Wenn ja, wird die Ausgabe abgebrochen und das Programm startet von Vorne
        elif subnetzmask[2] ==255 and broadcastadresse[3]+reservierteBits[i] >255 or subnetzmask[1] ==255 and broadcastadresse[3]+reservierteBits[i] >255 and broadcastadresse[2]==255 or subnetzmask[0] ==255 and broadcastadresse[3] + reservierteBits[i] >255 and broadcastadresse[2]==255 and broadcastadresse[1]==255:
            print("Die gewählten Zahlen ergeben eine IP-Adresse, die mir der gewünschten Subnetzmaske nicht zusammenpassen. Bitte verändern Sie die Subnetzmaske oder die eingegebenen Bereiche.")
            os.system("python ipcalc.py")

        #Beendet das Programm, wenn nichts mehr erhöht werden kann, da entweder die Subnetzmaske erreicht ist oder die Broadcastadresse=255.255.255.255 ist
        elif subnetzmask[0] ==255 and broadcastadresse[3]==broadcastadresse[2]==broadcastadresse[1]==255 or broadcastadresse[0]==255 or subnetzmask[1] ==255 and broadcastadresse[3]==broadcastadresse[2]==255 or subnetzmask[2] ==255 and broadcastadresse[3]==255:
            exit()

        #Prüft, ob der erste Zahlenblock der IP-Adresse keine Subnetzmaske von 255 hat und ob der zweite IP-Adressen Zahlenblock = 255 ist. Dann werden Zahlenblock 2-4 auf 0 gesetzt und der erste Zahlenblock wird erhöht um 1
        elif broadcastadresse[1]==255 and subnetzmask[0]!=255:
            nullSetzten(1,4,2,reservierteBits[i],broadcastadresse,netzwerkadresseListe)#1.Startwert, 2. Endwert, 3. ZahlenblockNr
            kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)

        #Prüft, ob der zweite Zahlenblock der IP-Adresse keine Subnetzmaske von 255 hat und ob der dritte IP-Adressen Zahlenblock = 255 ist. Dann werden Zahlenblock 3-4 auf 0 gesetzt und der zweite Zahlenblock wird erhöht um 1
        elif broadcastadresse[2]==255 and subnetzmask[1]!=255:
            nullSetzten(2,4,2,reservierteBits[i],broadcastadresse,netzwerkadresseListe)#1.Startwert, 2. Endwert, 3. ZahlenblockNr
            kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)

        #Prüft, ob der dritte Zahlenblock der IP-Adresse keine Subnetzmaske von 255 hat und ob der vierte IP-Adressen Zahlenblock = 255 ist. Dann wird der 4 Zahlenblock auf 0 gesetzt und der dritte Zahlenblock wird erhöht um 1
        elif broadcastadresse[3] + reservierteBits[i] >255 or broadcastadresse[3]==255 and subnetzmask[2]!=255:
            nullSetzten(3,4,2,reservierteBits[i],broadcastadresse,netzwerkadresseListe)#1.Startwert, 2. Endwert, 3. ZahlenblockNr
            kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)
        
        #Netzwerkadresse, Broadcastadresse und kleinste und größste Zahl werden ausgerechnet
        else:
            netzwerkadresseListe[3]=broadcastadresse[3]+1
            broadcastadresse[3]=broadcastadresse[3]+reservierteBits[i]
            kleinerGroß(netzwerkadresseListe,broadcastadresse,ipkleinste,ipGrößste)


        print("Hostblock:",i+1)
        print("Host anzahl",reservierteBits[i])
        point(netzwerkadresseListe,"Netzwerkadresse:\t")
        point(ipkleinste,"Kleinste IP-Adresse:\t")
        point(ipGrößste,"Größe IP-Adresse:\t")
        point(broadcastadresse,"Broadcastadresse:\t")
        print(end="\n")

        #"point()" ändert die Variablen in einen String um. Deswegen wird hier, zum weiteren berechnen der Adressen, diese wieder in einen Integer umgewandelt

        


#Prüft, ob eine IPv4 Adresse eingegeben wurde und ansonsten gibt es ein Fehler aus
if len(ipv)==4:
    #Von Zeile 338 - 366 rufen die Variabeln Funktionen auf, die dann das Ergebnis auf in einer andere Funktion übergeben
    binaryIP=binaryCalc(ip)
    point(listBinary,name)

    binarySubnet=netzmaskenBinär(netmask)
    #Das Ergebnis von "binaryIPOhnePunkt" wird in die Variable "resultOhnePunkt" gespeicher
    dezimaleSubnetzadresse=dezimalCalc(binarySubnet,"Subnetzmaske in Dezimal:")
 
    #resultOhnePunkt=ohnePunkte(binarySubnet)
    binaryIPOhnePunkt=ohnePunkte(binaryIP)

    netzwerkAdresse=netzwerkAdresse(binarySubnet,binaryIPOhnePunkt)
    broadcastadresseBinär=broadcastAddress(netzwerkAdresse,netmask) #Größste Broadcastadresse
    
    #Sorgt dafür, dass in Dezimal umgerechtnet wird und mit Punkt ausgegeben wird. Da die Funktion "dezimalCalc()"" auch "point()" aufrunf und "point()" das Ergebnis ausgibt
    #Hier wird nur die Liste in die Variable gespeichert, die bei "dezimalCalc()" "returnt" wurde
    broadcastadresseDezimal=dezimalCalc(broadcastadresseBinär, "Broadcastadresse in Dezimal:") 
    netzwerkadresseUmwandlungDezimal=dezimalCalc(netzwerkAdresse,"Netzwerkadresse in Dezimal:")
    
    eingabeSymetrisch= input("Soll es Symetrisch sein? " )


    if eingabeSymetrisch=="Ja"or eingabeSymetrisch=="ja"or eingabeSymetrisch=="j":
        angabeVLSM=int(input("Wie groß soll die VLSM Zahl sein? "))
        #Prüft, ob die VLSM überhaubt möglich ist
        if angabeVLSM > netmask or angabeVLSM <= 30:
            berechnungAnzahlBitsMöglichkeitenImBlock=BlockanzahlUBlockHostgröße(angabeVLSM,netmask)
            symetrischesNetzwerk(netzwerkadresseUmwandlungDezimal,dezimaleSubnetzadresse,berechnungAnzahlBitsMöglichkeitenImBlock,broadcastadresseDezimal)
        else:
            print("Bitte gebe einen neue VLSM Zahl beim neu Start des Programmes ein")
            os.system("python ipcalc.py")

    else:
        asymetrisch(netzwerkadresseUmwandlungDezimal,dezimaleSubnetzadresse)

else:

    print("ungültige IPv4-Adresse, bitte gebe eine Neue ein!")
    #startet das Programm von Vorne
    os.system("python ipcalc.py")