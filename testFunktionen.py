Netzwerkadresse="192.168.0.0"
NetzwerkadresseListe=[192,168,0,0]
BoardcarsAdresse=[192,168,0,0] #fängt mir der Netzwerkadresse an, dort wird aber immer + drauf gerechnet
subnetzMaske=[255,252,0,0]
ipkleinste=[192,168,0,0]
ipGröße=[192,168,0,0]
Hostbits=32-27 #VLSM Nummer
berechnungAnzahlBitsMöglichkeitenImBlock=(2**Hostbits)# nur immer bei 0 - 1,da die IP Adressen bei 0 anfangen

Subnetzbits=27-14 #VLSM Bits - Subnetzmaskenbits
möglicheSubnetzte=2**Subnetzbits

gesamtnetzgröße=2**(32-14)#alles Bits- Subnetzmaskenbits
subnetzgröße =gesamtnetzgröße/möglicheSubnetzte

anzahlDerBlöcke=gesamtnetzgröße/subnetzgröße

def kleinerGroß():
    for i in range(0,3): #nur bis 2, da 3 anders Berechnet wird
        ipkleinste[i]=BoardcarsAdresse[i]
        ipGröße[i]=BoardcarsAdresse[i]
    

    ipkleinste[3]=NetzwerkadresseListe[3]+1
    ipGröße[3]=BoardcarsAdresse[3]-1


    return ipkleinste, ipGröße
    

def boardUNetzwerkAdresseR(BoardcarsAdresse):
    BoardcarsAdresse[3]+= berechnungAnzahlBitsMöglichkeitenImBlock - 1


def nullSetzten(start,ende,blockNr):
    for i in range(start,ende):
        print(i)
        BoardcarsAdresse[i]=0
        NetzwerkadresseListe[i]=0
        print(i)

    BoardcarsAdresse[blockNr]+= 1   #erhöhung der des Zahlenblockens um 1
    NetzwerkadresseListe[blockNr] +=1

    BoardcarsAdresse[3]= BoardcarsAdresse[3] + berechnungAnzahlBitsMöglichkeitenImBlock - 1 # rechnet die Broadcast Adresse aus (aktuelle + anzahl Bits -1, weil es der erste ist und die 0 beachtet werden muss)


def symetrischesNetzwerk():
    for i in range(200000):  # Anzahl der Blöcke
        if BoardcarsAdresse[3] == 0:

            BoardcarsAdresse[3]+= berechnungAnzahlBitsMöglichkeitenImBlock - 1
            NetzwerkadresseListe[3]=0
            kleinerGroß()


        elif BoardcarsAdresse[0] == 255:
            exit()

        elif BoardcarsAdresse[3] == 255 and BoardcarsAdresse[2] == 255 and BoardcarsAdresse[1] == 255 and subnetzMaske[0] < 255:
            nullSetzten(1,4,0)#1.startwer, 2. endwert, 3. ZahlenblockNr

            kleinerGroß()

        elif BoardcarsAdresse[3] == 255 and BoardcarsAdresse[2] == 255 and subnetzMaske[1] < 255:
            nullSetzten(2,4,1)#1.startwer, 2. endwert, 3. ZahlenblockNr
            kleinerGroß()


        elif BoardcarsAdresse[3] == 255 and subnetzMaske[2] < 255:
            nullSetzten(3,4,2)#zweimal Ende, da somit spanweitenStart nicht neu gesetzt werden muss, da beides 3 ist
            #1.startwer, 2. endwert, 3. ZahlenblockNr
            kleinerGroß()

        else:
            NetzwerkadresseListe[3]=BoardcarsAdresse[3]+1 #rechnet die Netzwerkadresse aus
            BoardcarsAdresse[3] += berechnungAnzahlBitsMöglichkeitenImBlock #ausnahme
            kleinerGroß()
            #Netzwerkadresse hier hinzufügen!
        

        #ip Kleinste NetzwerkAdresse+1
        #ip Größe = BoardcastAdresse-1
        print("NetzwerkadresseListe ",i,NetzwerkadresseListe)
        print("kleinste ",i,ipkleinste)
        print("größe ",i,ipGröße)
        print("BoardcarsAdresse ",i,BoardcarsAdresse)
    
# das ausgegebende ERgebnis für die NetzwerkAdresse einfach +1, wenn das dann >255 ist ist die nöchste 3 Block +1 und 4 Block =0
# darauf achten, das BoardCast du Netzwerkadresse richtig ausgegeben werden
# zusätzlich die kleinste und die höchste angeben