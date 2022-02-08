import math
import scapy
from scapy.all import *
from data import Unpack

def main():
  result0 = Unpack('pcap/gv 720p-1.pcap')
  arr0 = result0.getarray()
  result0.plot()
main()