import math
import scapy
from scapy.all import *
from data import Unpack
from pcap import *
import matplotlib.pyplot as plt

def main():
  filename0 = "pcap/capture_stanford-0.pcap"
  # filename0 = "pcap/NFT in 3min-1.pcap"
  filename1 = "pcap/capture_stanford-1.pcap"

  print("Comparing ",filename0, filename1)
  
  result0 = Unpack(filename0)
  result1 = Unpack(filename1)
  arr0 = result0.getarray()
  arr1 = result1.getarray()

  n0 = len(arr0)
  n1 = len(arr1)

  # swap arrays
  if(n0 < n1):
    arr0 = result1.getarray()
    arr1 = result0.getarray()
    n0,n1 = n1,n0
    filename0,filename1 = filename1,filename0

  print(n0,n1)

  n = n0/n1

  indices_s = []

  for i in range(n1):
    indices_s.append(int(i*n))

  # store the sampled values of arr0 in arr
  arr = []

  # sample the long sized array
  for i in range(n1):
    arr.append(arr0[indices_s[i]])
  # print(len(arr))

  dist = 1
  if(dist):
    # after sampling now re-distribute the deleted ones
    indices_d = []

    # Get deleted indices, assume that n0 > n1
    for i in range(n0):
      if i in indices_s:
        pass
      else:
        indices_d.append(i)

    i = 0 # deleted 
    j = 0 # sampled
    while(j<n1): #change while(1) to some condition
      # print(i,"and",j)
      if(i == len(indices_d)):
        break
      if(j+1 == n1): # means end of indices_s array
        # distribute leftward
        k = j
        if(k-2 >= 0):
          arr[k] += 0.5*arr0[indices_d[i]]
          arr[k-1] += 0.3*arr0[indices_d[i]]
          arr[k-2] += 0.2*arr0[indices_d[i]]
        elif(k-1 >= 0):
          arr[k] += 0.6*arr0[indices_d[i]]
          arr[k-1] += 0.4*arr0[indices_d[i]]
        elif(k >=0):
          arr[k] += arr0[indices_d[i]]
        i += 1
      else:
        if(indices_s[j] < indices_d[i] and indices_d[i] < indices_s[j+1]):
          val = arr0[indices_d[i]]/2
          # print(val)
          # break
          # distribute rightward
          k = j+1
          if(k+2 < n1):
            arr[k] += 0.5*val
            arr[k+1] += 0.3*val
            arr[k+2] += 0.2*val
          elif(k+1 < n1):
            arr[k] += 0.6*val
            arr[k+1] += 0.4*val
          elif(k < n1):
            arr[k] += val
          else:
            arr[j] += val

          # distribute leftward
          k = j
          if(k-2 >= 0):
            arr[k] += 0.5*val
            arr[k-1] += 0.3*val
            arr[k-2] += 0.2*val
          elif(k-1 >= 0):
            arr[k] += 0.6*val
            arr[k-1] += 0.4*val
          elif(k >=0):
            arr[k] += val
          i += 1
          j += 1
        else:
          j += 1

  diff = 0
  for i in range(n1):
    diff += abs(arr[i]-arr1[i])

  print("Absolute difference  :", int(diff))

  sum0 = 0
  sum1 = 0
  for i in arr:
    sum0 += i
  for i in arr1:
    sum1 += i

  avg = (sum0+sum1)/2

  print(sum0, sum1, avg)

  percentage_similarity = ((avg - diff)/avg)*100

  timearr = []
  for i in range(0, len(arr)):
    timearr.append(i)

  print("Percentage similarity:", round(percentage_similarity, 2),"%")
  # plt.figure(figsize=(20,10))
  # plt.plot(timearr, arr, color='r', label=filename0)
  # plt.plot(timearr, arr1, color='g', label=filename1)
  # plt.xlabel('Packet sequence')
  # plt.ylabel('Length of each packet')
  # plt.title('Video fingerprint for '+filename0+" , "+filename1)
  # plt.legend()
  # plt.show()

  timearr_s = []
  for i in range(0, len(arr0)):
    timearr_s.append(i)

  for i in range(0,len(arr0)-len(arr)):
    arr.append(0)
  # Set general font size
  plt.rcParams['font.size'] = '13'
  fig, axs = plt.subplots(2, sharey=True, figsize=(10,5))
  fig.add_subplot(111, frameon=False)
  plt.tick_params(labelcolor='none', which='both', labelsize=25, top=False, bottom=False, left=False, right=False)
  axs[0].plot(timearr_s, arr0, color='g', label=filename0+" Without sampling and redistribution")
  axs[1].plot(timearr_s, arr, color='b', label=filename0+" With sampling and redistribution")
  axs[0].legend(prop={"size":16})
  axs[1].legend(prop={"size":16})
  plt.title('Video fingerprint for '+filename0+" , "+filename1, fontsize = 16)
  plt.xlabel('Packet sequence', fontsize = 16)
  plt.ylabel('Length of each packet', fontsize = 16)
  plt.show()

main()