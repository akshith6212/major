import math
import scapy
from scapy.all import *
from data_m4 import Unpack
from pcap import *
import matplotlib.pyplot as plt
import os
from tabulate import tabulate

path = "./pcap_test_campus/kolla-my/"
files = os.listdir(path)

pcap_files = []
x = 0
for i in files:
  if '.pcap' in i:
    x = x+1
    slug = path + i
    pcap_files.append(slug)


dp = {} # for storing contents as a dp array

def main(filename, filename_to):
  filename0 = filename_to
  filename1 = filename

  if(filename0 == filename1):
    return 100.00

  print("Comparing ",filename0, filename1)

  try:
    result0 = dp[filename0]
  except:
    result0 = Unpack(filename0)
    dp[filename0] = result0

  try:
    result1 = dp[filename1]
  except:
    result1 = Unpack(filename1)
    dp[filename1] = result1

  (arr0,packets0,mul) = result0.getarray()
  (arr1,packets1,mul) = result1.getarray()

  sum0 = 0
  sum1 = 0
  for i in arr0:
    sum0 += i
  for i in arr1:
    sum1 += i

  # check if both are similar
  if(math.isclose(sum0,sum1,rel_tol=0.23)): 
    # implement algo-2
    print("Implementing algo-2")
    d = int(1/mul)
    timearr = []
    for i in range(0, d):
      timearr.append(i)

    packets0 = packets0[:d]
    packets1 = packets1[:d] 

    n0 = len(packets0)
    n1 = len(packets1)

    # print(n0,n1)

    sum0 = 0
    sum1 = 0
    for i in packets0:
      sum0 += i
    for i in packets1:
      sum1 += i

    if(sum0 < sum1):
      delta = abs(int(sum1/n1)-int(sum0/n0))
      for i in range(len(packets0)):
        packets0[i] += delta
      sum0 += len(packets0)*delta
    else:
      delta = abs(int(sum1/n1)-int(sum0/n0))
      for i in range(len(packets1)):
        packets1[i] += delta
      sum1 += len(packets1)*delta

    diff = 0
    for i in range(n1):
      diff += abs(packets0[i]-packets1[i])

    # print("Absolute difference  :", int(diff))

    avg = (sum0+sum1)/2

    # print(sum0, sum1, avg, diff)

    percentage_similarity = ((avg - diff)/avg)*100

    # print("percentage_similarity: ",percentage_similarity,"%")
    return round(percentage_similarity, 2)
  
  else:
    # implement algo-1
    print("Implementing algo-1")
    n0 = len(arr0)
    n1 = len(arr1)

    # swap arrays
    if(n0 < n1):
      (arr0,packets0,mul) = result1.getarray()
      (arr1,packets1,mul) = result0.getarray()
      n0,n1 = n1,n0
      filename0,filename1 = filename1,filename0

    # print(n0,n1)

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

    # print("Absolute difference  :", int(diff))

    sum0 = 0
    sum1 = 0
    for i in arr:
      sum0 += i
    for i in arr1:
      sum1 += i

    avg = (sum0+sum1)/2

    # print(sum0, sum1, avg)

    percentage_similarity = ((avg - diff)/avg)*100

    timearr = []
    for i in range(0, len(arr)):
      timearr.append(i)

    # print("Percentage similarity:", round(percentage_similarity, 2),"%")
    return round(percentage_similarity, 2)


filename_to = "./pcap_test_480_campus/bitcoin_480_1.pcap"

arr = []
for i in pcap_files:
  result = main(i, filename_to)
  if(result != 100):
    arr.append((result, i))

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
# clearConsole()

top = 5

print("\n------------------------------------------------------------------------------------------------")
print("Compared",filename_to," with ",len(pcap_files)," files")
print("Top",top," files chosen to be similar with ",filename_to, " are:")
print("------------------------------------------------------------------------------------------------ \n")
arr.sort(key=lambda y: y[0], reverse=True)
print(arr)

top_percentages = arr[:top]
estimated_percentages = []
# sum = 0
# for i in top_percentages:
#   sum += i[0]

# for i in top_percentages:
#   estimated_percentages.append(( i[1], round(i[0]/sum, 4)*100 ))

print(tabulate(top_percentages, headers=["Filename", "Percentage Similarity"]))