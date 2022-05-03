import math
import scapy
from scapy.all import *
from data_m4 import Unpack
import matplotlib.pyplot as plt

def main():
  filename0 = "./pcap/test/capture_29-2239-insane.pcap"
  filename1 = "./pcap/test/capture_29-2244-insane.pcap"
  filename2 = "./pcap/test/tony-peter_480_1.pcap"
  filename3 = "./pcap/test/tony-peter_480_2.pcap"
  filename4 = "./pcap/test/capture_30-2105_RRR.pcap"
  filename5 = "./pcap/test/capture_30-2109_RRR.pcap"
  
  result0 = Unpack(filename0)
  (arr0,packets0,mul) = result0.getarray()
  
  result1 = Unpack(filename1)
  (arr1,packets1,mul) = result1.getarray()

  result2 = Unpack(filename2)
  (arr2,packets2,mul) = result2.getarray()
  
  result3 = Unpack(filename3)
  (arr3,packets3,mul) = result3.getarray()

  # result4 = Unpack(filename4)
  # (arr4,packets4,mul) = result4.getarray()
  
  # result5 = Unpack(filename5)
  # (arr5,packets5,mul) = result5.getarray()

  d = int(1/mul)
  timearr = []
  for i in range(0, d):
    timearr.append(i)

  packets0 = packets0[:d]
  packets1 = packets1[:d]
  packets2 = packets2[:d]
  packets3 = packets3[:d]
  # packets4 = packets4[:d]
  # packets5 = packets5[:d]

  plt.figure(figsize=(20,10))
  plt.plot(timearr, packets0, color='r', label=filename0)
  plt.plot(timearr, packets1, color='r', label=filename1)
  plt.plot(timearr, packets2, color='y', label=filename2)
  plt.plot(timearr, packets3, color='y', label=filename3)
  # plt.plot(timearr, arr4, color='m', label='hui-0')
  # plt.plot(timearr, arr5, color='y', label='hui-1')
  plt.xlabel('Data loaded(%)')
  plt.ylabel('No.of packets required for each chunk')
  plt.title('Video fingerprint comparison')
  plt.legend()
  plt.show()

  # fig, axs = plt.subplots(4, sharex=True, sharey=True, figsize=(20,10))
  # fig.add_subplot(111, frameon=False)
  # plt.tick_params(labelcolor='none', which='both', top=False, bottom=True, left=False, right=False)
  # axs[0].plot(timearr, packets0, color='r', label=filename0)
  # axs[1].plot(timearr, packets1, color='g', label=filename1)
  # axs[2].plot(timearr, packets2, color='b', label=filename2)
  # axs[3].plot(timearr, packets3, color='y', label=filename3)
  # # axs[4].plot(timearr, packets4, color='y', label=filename4)
  # # axs[5].plot(timearr, packets5, color='y', label=filename5)
  # axs[0].legend()
  # axs[1].legend()
  # axs[2].legend()
  # axs[3].legend()
  # # axs[4].legend()
  # # axs[5].legend()
  # plt.title('Video fingerprint for '+filename0+" , "+filename1+" , "+filename2+" , "+filename3+" , "+filename4+" , "+filename5)
  # plt.xlabel('Chunk sequence')
  # plt.ylabel('No.of packets required for each chunk')
  # plt.show()

main()