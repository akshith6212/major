import math
import scapy
from scapy.all import *
from data_m2 import Unpack
import matplotlib.pyplot as plt

Cumulative = 0

def main():
  # filename0 = "pcap/Bitcoin made simple - guardian-1.pcap"
  filename0 = "pcap/capture_stanford-0.pcap"
  # filename0 = "pcap/NFT in 3min-1.pcap"
  filename1 = "pcap/capture_stanford-1.pcap"

  print("Comparing ",filename0, filename1)

  result0 = Unpack(filename0, Cumulative)
  (arr_0,arr0,mul) = result0.getarray()
  # result0.plot()

  result1 = Unpack(filename1, Cumulative)
  (arr_1,arr1,mul) = result1.getarray()
  # result1.plot()

  d = int(1/mul)
  timearr = []
  for i in range(0, d):
    timearr.append(i)

  arr0 = arr0[:d]
  arr1 = arr1[:d] 

  n0 = len(arr0)
  n1 = len(arr1)

  # print(n0,n1)

  sum0 = 0
  sum1 = 0
  for i in arr0:
    sum0 += i
  for i in arr1:
    sum1 += i

  if(sum0 < sum1):
    delta = int(sum1/sum0)
    for i in range(len(arr0)):
      arr0[i] += delta
    sum0 += len(arr0)*delta
  else:
    delta = int(sum0/sum1)
    for i in range(len(arr1)):
      arr1[i] += delta
    sum1 += len(arr1)*delta

  diff = 0
  for i in range(n1):
    diff += abs(arr0[i]-arr1[i])

  # print("Absolute difference  :", int(diff))

  avg = (sum0+sum1)/2

  print(sum0, sum1, avg, diff)

  percentage_similarity = ((avg - diff)/avg)*100

  print("percentage_similarity: ",percentage_similarity,"%")

  timearr_s = []
  for i in range(0,len(arr_0)):
    timearr_s.append(i)

  plotting = 1
  
  if(plotting):
    print(n0,n1)
    # plt.figure(figsize=(20,10))
    # plt.plot(timearr, arr0, color='r', label=filename0)
    # plt.plot(timearr, arr1, color='g', label=filename1)
    # plt.xlabel('Data loaded(%)')
    # if(Cumulative):
    #   plt.ylabel('Cumulative no.of packets required for each chunk')
    # else:
    #   plt.ylabel('No.of packets required for each chunk')
    # plt.title('Video fingerprint comparison')
    # plt.legend()
    # plt.show()

    # fig, axs = plt.subplots(2)
    # fig.suptitle('Video fingerprint for '+filename0+" , "+filename1)
    # axs[0].plot(timearr, arr0, color='r', label=filename0)
    # axs[1].plot(timearr, arr1, color='g', label=filename1)
    # for ax in axs.flat:
    #   ax.set(xlabel='Chunk sequence', ylabel='No.of packets required for each chunk')
    # plt.show()
    # Set general font size
    plt.rcParams['font.size'] = '13'
    fig, axs = plt.subplots(2,  figsize=(20,10))
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', which='both', labelsize=20, top=False, bottom=False, left=False, right=False)
    axs[1].plot(timearr, arr0, color='b', label=filename0+" With dividing into chunks")
    # axs[1].plot(timearr, arr1, color='g', label=filename1)
    axs[0].plot(timearr_s, arr_0, color='g', label=filename0+" Without dividing into chunks")
    axs[0].legend(prop={"size":16})
    axs[1].legend(prop={"size":16})
    axs[0].set_xlabel('Chunk sequence', fontsize = 16)
    axs[1].set_xlabel('Chunk sequence', fontsize = 16)
    plt.title('Video fingerprint for '+filename0+" , "+filename1, fontsize = 16)
    plt.ylabel('No.of packets required for each chunk', fontsize = 16)
    plt.show()

main()