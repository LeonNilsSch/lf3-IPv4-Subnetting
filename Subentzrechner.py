import tkinter as tk
from tkinter import ttk
import ipaddress
import textwrap  

def calculate_subnet():
    ip = ip_entry.get()
    netmask = int(netmask_entry.get())
    ipv = ip.split(".")

    if len(ipv) == 4:
        binary = "00000000000000000000000000000000"
        listBinary = binaryCalc(ipv)
        netzmaskeInBinär = "1" * netmask + binary[netmask:]
        netzmaskeInBinärAufteilung = textwrap.wrap(netzmaskeInBinär, width=8)
        dezimalzahl = [int(b, 2) for b in netzmaskeInBinärAufteilung]
        
        netmask_binary_text = "Subnetzmaske in Binär:\t\n" + ".".join(netzmaskeInBinärAufteilung)
        netmask_decimal_text = "Subnetzmaske in Dezimal:\t\n" + ".".join([str(d) for d in dezimalzahl])
        
        netmask_label.config(text=netmask_binary_text + "\n\n" + netmask_decimal_text)
        
        bits = 32 - netmask
        anzahlSubnetze = (2**bits) - 2
        bits_hosts_label.config(text="Offene Bits und mögliche Hosts:\t\n" + str(bits) + ", " + str(anzahlSubnetze))
        
        network = ipaddress.ip_network(ip + '/' + str(netmask), strict=False)
        min_host = network.network_address + 1
        max_host = network.broadcast_address - 1
        min_host_label.config(text="Kleinste Hostadresse im Subnetz (dezimal):\t\n" + str(min_host))
        max_host_label.config(text="Größte Hostadresse im Subnetz (dezimal):\t\n" + str(max_host))
    else:
        result_label.config(text="Ungültige IPv4-Adresse, bitte geben Sie eine neue ein!")

def binaryCalc(ipv):
    listBinary = []
    for i in ipv:
        binary = format(int(i), "08b")
        listBinary.append(binary)
    return listBinary

root = tk.Tk()
root.title("Subnetzrechner")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S))

ip_label = ttk.Label(mainframe, text="IP-Adresse:")
ip_label.grid(column=0, row=0, sticky=tk.W)

ip_entry = ttk.Entry(mainframe)
ip_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

netmask_label = ttk.Label(mainframe, text="Netzmaske:")
netmask_label.grid(column=0, row=1, sticky=tk.W)

netmask_entry = ttk.Entry(mainframe)
netmask_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

calculate_button = ttk.Button(mainframe, text="Berechnen", command=calculate_subnet)
calculate_button.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))

netmask_label = ttk.Label(mainframe, text="")
netmask_label.grid(column=0, row=3, columnspan=2, sticky=(tk.W, tk.E))

bits_hosts_label = ttk.Label(mainframe, text="")
bits_hosts_label.grid(column=0, row=4, columnspan=2, sticky=(tk.W, tk.E))

min_host_label = ttk.Label(mainframe, text="")
min_host_label.grid(column=0, row=5, columnspan=2, sticky=(tk.W, tk.E))

max_host_label = ttk.Label(mainframe, text="")
max_host_label.grid(column=0, row=6, columnspan=2, sticky=(tk.W, tk.E))

root.mainloop()
