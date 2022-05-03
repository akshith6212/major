import math
import scapy
from scapy.all import *
from data_m3 import Unpack
import matplotlib.pyplot as plt

def main():
  filename0 = "../m4-hybrid/pcap/test/capture_29-2239-insane.pcap"
  filename1 = "../m4-hybrid/pcap/test/capture_29-2244-insane.pcap"
  filename2 = "../m4-hybrid/pcap/test/tony-peter_480_1.pcap"
  filename3 = "../m4-hybrid/pcap/test/tony-peter_480_2.pcap"
  filename4 = "../m4-hybrid/pcap/test/capture_30-2105_RRR.pcap"
  filename5 = "../m4-hybrid/pcap/test/capture_30-2109_RRR.pcap"
  
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

  # plt.figure(figsize=(20,10))
  # plt.plot(timearr, arr0, color='r', label=filename0)
  # plt.plot(timearr, arr1, color='g', label=filename1)
  # plt.plot(timearr, arr2, color='b', label=filename2)
  # plt.plot(timearr, arr3, color='c', label=filename3)
  # plt.plot(timearr, arr4, color='m', label=filename4)
  # plt.plot(timearr, arr5, color='y', label=filename5)
  # plt.xlabel('Data loaded(%)')
  # if(Cumulative):
  #   plt.ylabel('Cumulative time taken for each chunk (seconds)')
  # else:
  #   plt.ylabel('Time taken for each chunk (seconds)')
  # plt.title('Video fingerprint comparison')
  # plt.legend()
  # plt.show()

  fig, axs = plt.subplots(4, sharex=True, sharey=True, figsize=(20,10))
  fig.add_subplot(111, frameon=False)
  plt.tick_params(labelcolor='none', which='both', top=False, bottom=True, left=False, right=False)
  axs[0].plot(timearr, arr0, color='r', label=filename0)
  axs[1].plot(timearr, arr1, color='g', label=filename1)
  axs[2].plot(timearr, arr2, color='b', label=filename2)
  axs[3].plot(timearr, arr3, color='y', label=filename3)
  axs[4].plot(timearr, arr4, color='y', label=filename4)
  axs[5].plot(timearr, arr5, color='y', label=filename5)
  axs[0].legend()
  axs[1].legend()
  axs[2].legend()
  axs[3].legend()
  axs[4].legend()
  axs[5].legend()
  plt.title('Video fingerprint for '+filename0+" , "+filename1+" , "+filename2+" , "+filename3+" , "+filename4+" , "+filename5)
  plt.xlabel('Chunk sequence')
  plt.ylabel('No.of packets required for each chunk')
  plt.show()
main()