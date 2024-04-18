import os
import textwrap

def ip_to_binary(ip):
    # Split the IP address by "."
    octets = ip.split(".")
    # Convert each octet to binary and format it to 8 bits
    binary_octets = [format(int(octet), "08b") for octet in octets]
    # Join the binary octets with "."
    return ".".join(binary_octets)

def netmask_to_binary(netmask):
    # Create the binary string for the subnet mask
    binary_mask = "1" * netmask + "0" * (32 - netmask)
    # Split the binary mask into octets
    binary_octets = textwrap.wrap(binary_mask, width=8)
    # Convert each octet to decimal
    decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
    # Join the decimal octets with "."
    return ".".join(decimal_octets)

def main():
    ip = input("Enter the IP address: ")
    netmask = int(input("Enter the subnet mask: "))
    
    # Check if the IP address is valid
    if len(ip.split(".")) != 4:
        print("Invalid IPv4 address.")
        os.system("python ipcalc.py")
        return
    
    ip_binary = ip_to_binary(ip)
    netmask_binary = netmask_to_binary(netmask)
    
    print("IP address:\t\t", ip)
    print("Binary IP address:\t", ip_binary)
    print("Subnet mask:\t\t", netmask)
    print("Binary subnet mask:\t", netmask_binary)

if __name__ == "__main__":
    main()
