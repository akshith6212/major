import math
import scapy
from scapy.all import *
from data_m3 import Unpack
import matplotlib.pyplot as plt

def main():
  # filename0 = "pcap/Bitcoin made simple - guardian-1.pcap"
  filename0 = "pcap/NFT in 3min-1.pcap"
  filename1 = "pcap/NFT in 3min-2.pcap"

  print("Comparing ",filename0, filename1)
  
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

  diff = 0
  for i in range(n1):
    diff += abs(arr0[i]-arr1[i])

  # print("Absolute difference  :", int(diff))

  sum0 = 0
  sum1 = 0
  for i in arr0:
    sum0 += i
  for i in arr1:
    sum1 += i

  avg = (sum0+sum1)/2

  print(sum0, sum1, avg, diff)

  percentage_similarity = ((avg - diff)/avg)*100

  print("percentage_similarity: ",percentage_similarity,"%")

  plotting = 1
  
  if(plotting):
    print(n0,n1)

    # plt.figure(figsize=(20,10))
    # plt.plot(timearr, arr0, color='r', label=filename0)
    # plt.plot(timearr, arr1, color='g', label=filename1)
    # plt.xlabel('Data loaded(%)')
    # if(Cumulative):
    #   plt.ylabel('Cumulative time taken for each chunk (seconds)')
    # else:
    #   plt.ylabel('Time taken for each chunk (seconds)')
    # plt.title('Video fingerprint comparison')
    # plt.legend()
    # plt.show()

    # fig, axs = plt.subplots(2)
    # fig.suptitle('Video fingerprint for '+filename0+" , "+filename1)
    # axs[0].plot(timearr, arr0, color='r', label=filename0)
    # axs[1].plot(timearr, arr1, color='g', label=filename1)
    # for ax in axs.flat:
    #   ax.set(xlabel='Chunk sequence', ylabel='Time taken for each chunk (seconds)')
    # plt.show()

    fig, axs = plt.subplots(2, sharey=True, figsize=(20,10))
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
    axs[0].plot(timearr, arr0, color='r', label=filename0)
    axs[1].plot(timearr, arr1, color='g', label=filename1)
    axs[0].legend()
    axs[1].legend()
    for ax in axs.flat:
      ax.set(xlabel='Chunk sequence')
    plt.title('Video fingerprint for '+filename0+" , "+filename1)
    plt.ylabel('No.of packets required for each chunk')
    plt.show()
main()