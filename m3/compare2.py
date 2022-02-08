import math
import scapy
from scapy.all import *
from data_m3 import Unpack
import matplotlib.pyplot as plt

def main():
  filename0 = "pcap/capture_hui-0.pcap"
  filename1 = "pcap/capture_hui-1.pcap"
  
  result0 = Unpack(filename0)
  (arr0,mul,Cumulative) = result0.getarray()
  # result0.plot()

  result1 = Unpack(filename1)
  (arr1,mul,Cumulative) = result1.getarray()
  # result1.plot()

  d = int(1/mul)-1
  timearr = []
  for i in range(0, d):
    timearr.append(i)

  arr0 = arr0[:d]
  arr1 = arr1[:d]

  n0 = len(arr0)
  n1 = len(arr1)

  print(n0,n1)

  plt.figure(figsize=(20,10))
  plt.plot(timearr, arr0, color='r', label=filename0)
  plt.plot(timearr, arr1, color='g', label=filename1)
  plt.xlabel('Data loaded(%)')
  if(Cumulative):
    plt.ylabel('Cumulative time taken for each chunk (seconds)')
  else:
    plt.ylabel('Time taken for each chunk (seconds)')
  plt.title('Video fingerprint comparison')
  plt.legend()
  plt.show()
main()