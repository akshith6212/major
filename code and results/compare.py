import math
import scapy
from scapy.all import *
from data import Unpack

def main():
  result0 = Unpack('capture_stanford-0.pcap')
  arr0 = result0.getarray()
  result1 = Unpack('capture_stanford-1.pcap')
  arr1 = result1.getarray()

  n0 = len(arr0)
  n1 = len(arr1)

  print(n0,n1)

  n = max(n0,n1)/min(n0,n1)

  indices = []

  for i in range(min(n0,n1)):
    indices.append(int(i*n))

  # store the sampled values in arr
  arr = []
  if(n0 > n1):
    for i in range(min(n0,n1)):
      arr.append(arr0[indices[i]])
    # print(len(arr))

    diff = 0
    for i in range(min(n0,n1)):
      diff += abs(arr[i]-arr1[i])

    print("Absolute difference  :", int(diff))

    sum0 = 0
    sum1 = 0
    for i in arr:
      sum0 += i
    for i in arr1:
      sum1 += i

    avg = (sum0+sum1)/2

    percentage_similarity = ((avg - diff)/avg)*100

    print("Percentage similarity:", round(percentage_similarity, 2),"%")
  
  else:
    for i in range(min(n0,n1)):
      arr.append(arr1[indices[i]])
    # print(len(arr))

    diff = 0
    for i in range(min(n0,n1)):
      diff += abs(arr[i]-arr0[i])
    print("Absolute difference  :", int(diff))

    sum0 = 0
    sum1 = 0
    for i in arr:
      sum0 += i
    for i in arr0:
      sum1 += i

    avg = (sum0+sum1)/2

    percentage_similarity = ((avg - diff)/avg)*100

    print("Percentage similarity:", round(percentage_similarity, 2),"%")

main()