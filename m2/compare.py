import math
import scapy
from scapy.all import *
from data_m2 import Unpack
import matplotlib.pyplot as plt

def main():
  result0 = Unpack("pcap/capture_stanford-0.pcap")
  (arr0,mul,Cumulative) = result0.getarray()
  
  result1 = Unpack("pcap/capture_stanford-1.pcap")
  (arr1,mul,Cumulative) = result1.getarray()

  result2 = Unpack("pcap/capture_levitating-0.pcap")
  (arr2,mul,Cumulative) = result2.getarray()
  
  result3 = Unpack("pcap/capture_levitating-1.pcap")
  (arr3,mul,Cumulative) = result3.getarray()

  result4 = Unpack("pcap/capture_hui-0.pcap")
  (arr4,mul,Cumulative) = result4.getarray()
  
  result5 = Unpack("pcap/capture_hui-1.pcap")
  (arr5,mul,Cumulative) = result5.getarray()

  d = int(1/mul)
  timearr = []
  for i in range(0, d):
    timearr.append(i)

  arr0 = arr0[:d]
  arr1 = arr1[:d]
  arr2 = arr2[:d]
  arr3 = arr3[:d]
  # arr4 = arr4[:d]
  # arr5 = arr5[:d]

  plt.figure(figsize=(20,10))
  plt.plot(timearr, arr0, color='r', label='stanford-0')
  plt.plot(timearr, arr1, color='g', label='stanford-1')
  plt.plot(timearr, arr2, color='b', label='levitating-0')
  plt.plot(timearr, arr3, color='c', label='levitating-1')
  # plt.plot(timearr, arr4, color='m', label='hui-0')
  # plt.plot(timearr, arr5, color='y', label='hui-1')
  plt.xlabel('Data loaded(%)')
  if(Cumulative):
    plt.ylabel('Cumulative no.of packets required for each chunk')
  else:
    plt.ylabel('No.of packets required for each chunk')
  plt.title('Video fingerprint comparison')
  plt.legend()
  plt.show()
main()