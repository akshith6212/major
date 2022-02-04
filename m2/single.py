import math
import scapy
from scapy.all import *
from data_m2 import Unpack
import matplotlib.pyplot as plt

def main():
  result = Unpack("pcap/capture_stanford-1.pcap")
  (arr,timearr) = result.getarray()
  # result.plot()

  for i in arr:
    print(i)

  n = len(arr)
  print(n)

main()

# n = 10
# for i  in range(0,n):
#   for i in range(0,2):
#     pass
#   print(i)
