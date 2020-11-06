# Simplest packet crafting script
from scapy.all import *

packet = IP(dst="github.com")/ICMP()
resp = sr1(packet)

print(resp[IP].src)
hexdump(packet)
