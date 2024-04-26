#  #10001110.10111011.11111111.11111111 # 142.187.255.255
# ip="10001110101110111001000111100000" 
# aN="11111111111111000000000000000000"
# position=[]
# höchstelP=""
# for i in range(len(ip)):
#     if aN[i]=="1":
#         position.append(i)
#         print(position)
#         hoechste_zahl = max(position)+1 #13 im Beispiel
#         NullerBits=32-hoechste_zahl #kein Ausgleich mit -1 da man vorher +1 gerechnet hat print(NullerBits, hoechste_zahl+NullerBits)
#     for i in range(hoechste_zahl):
#         höchstelP+ ip[i]
#         for i in range(NullerBits):
#             jetzigeZahl=hoechste_zahl+i
#             höchstelP+="1"
# print(höchstelP)
# print("max")
sub=24
ipBinär="11111111111111111100000100000000"
t=32-sub
ipBinär = ipBinär[:-t] + "1" * t
print(ipBinär)