import math
import scapy
from scapy.all import *
from data_m2 import Unpack
import matplotlib.pyplot as plt

def main():
  result0 = Unpack("pcap/capture_stanford-0.pcap")
  (arr0,timearr0) = result0.getarray()
  
  result1 = Unpack("pcap/capture_stanford-1.pcap")
  (arr1,timearr1) = result1.getarray()

  result2 = Unpack("pcap/capture_levitating-0.pcap")
  (arr2,timearr2) = result2.getarray()
  
  result3 = Unpack("pcap/capture_levitating-1.pcap")
  (arr3,timearr3) = result3.getarray()

  result4 = Unpack("pcap/capture_hui-0.pcap")
  (arr4,timearr4) = result4.getarray()
  
  result5 = Unpack("pcap/capture_hui-1.pcap")
  (arr5,timearr5) = result5.getarray()

  d = 73
  timearr = []
  for i in range(0, d):
    timearr.append(i)

  arr0 = arr0[:d]
  arr1 = arr1[:d]
  arr2 = arr2[:d]
  arr3 = arr3[:d]
  arr4 = arr4[:d]
  arr5 = arr5[:d]

  # plt.plot(timearr, arr0, color='r', label='stanford-0')
  # plt.plot(timearr, arr1, color='g', label='stanford-1')
  plt.plot(timearr, arr2, color='b', label='levitating-0')
  plt.plot(timearr, arr3, color='c', label='levitating-1')
  plt.plot(timearr, arr4, color='m', label='hui-0')
  plt.plot(timearr, arr5, color='y', label='hui-1')
  plt.xlabel('Data loaded(%)')
  plt.ylabel('No.of packets required for each chunk')
  plt.title('Video fingerprint comparison')
  plt.legend()
  plt.show()
main()