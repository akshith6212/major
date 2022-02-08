import math
import scapy
from scapy.all import *
from data_m3 import Unpack
import matplotlib.pyplot as plt

def main():
  filename0 = "pcap/capture_stanford-0.pcap"
  filename1 = "pcap/capture_stanford-1.pcap"
  filename2 = "pcap/capture_levitating-0.pcap"
  filename3 = "pcap/capture_levitating-1.pcap"
  filename4 = "pcap/capture_hui-0.pcap"
  filename5 = "pcap/capture_hui-1.pcap"
  
  result0 = Unpack(filename0)
  (arr0,mul,Cumulative) = result0.getarray()
  # result0.plot()

  result1 = Unpack(filename1)
  (arr1,mul,Cumulative) = result1.getarray()
  # result1.plot()

  result2 = Unpack(filename2)
  (arr2,mul,Cumulative) = result2.getarray()
  # result2.plot()

  result3 = Unpack(filename3)
  (arr3,mul,Cumulative) = result3.getarray()
  # result3.plot()

  result4 = Unpack(filename4)
  (arr4,mul,Cumulative) = result4.getarray()
  # result4.plot()

  result5 = Unpack(filename5)
  (arr5,mul,Cumulative) = result5.getarray()
  # result5.plot()

  d = int(1/mul)-1
  timearr = []
  for i in range(0, d):
    timearr.append(i)

  arr0 = arr0[:d]
  arr1 = arr1[:d]
  arr2 = arr2[:d]
  arr3 = arr3[:d]
  arr4 = arr4[:d]
  arr5 = arr5[:d]

  n0 = len(arr0)
  n1 = len(arr1)
  n2 = len(arr2)
  n3 = len(arr3)
  n4 = len(arr4)
  n5 = len(arr5)

  print(n0,n1,n2,n3,n4,n5)

  plt.figure(figsize=(20,10))
  plt.plot(timearr, arr0, color='r', label=filename0)
  plt.plot(timearr, arr1, color='g', label=filename1)
  plt.plot(timearr, arr2, color='b', label=filename2)
  plt.plot(timearr, arr3, color='c', label=filename3)
  plt.plot(timearr, arr4, color='m', label=filename4)
  plt.plot(timearr, arr5, color='y', label=filename5)
  plt.xlabel('Data loaded(%)')
  if(Cumulative):
    plt.ylabel('Cumulative time taken for each chunk (seconds)')
  else:
    plt.ylabel('Time taken for each chunk (seconds)')
  plt.title('Video fingerprint comparison')
  plt.legend()
  plt.show()
main()