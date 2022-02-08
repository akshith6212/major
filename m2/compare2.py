import math
import scapy
from scapy.all import *
from data_m2 import Unpack
import matplotlib.pyplot as plt

def main():
  result0 = Unpack("pcap/capture_hui-0.pcap")
  (arr0,mul,Cumulative) = result0.getarray()
  # result0.plot()

  result1 = Unpack("pcap/capture_hui-1.pcap")
  (arr1,mul,Cumulative) = result1.getarray()
  # result1.plot()

  # n0 = len(arr0)
  # n1 = len(arr1)

  # if(n0<n1):
  #   (arr0,timearr0) = result1.getarray()
  #   (arr1,timearr1) = result0.getarray()

  # arr0 = arr0[:min(n0,n1)]

  d = int(1/mul)
  timearr = []
  for i in range(0, d):
    timearr.append(i)

  n0 = len(arr0)
  n1 = len(arr1)

  print(n0,n1)

  plt.figure(figsize=(20,10))
  plt.plot(timearr, arr0, color='r', label='hui-0')
  plt.plot(timearr, arr1, color='g', label='hui-1')
  plt.xlabel('Data loaded(%)')
  if(Cumulative):
    plt.ylabel('Cumulative no.of packets required for each chunk')
  else:
    plt.ylabel('No.of packets required for each chunk')
  plt.title('Video fingerprint comparison')
  plt.legend()
  plt.show()
main()