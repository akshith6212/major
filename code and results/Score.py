import math
import scapy
from scapy.all import *
from data import Unpack

class GetScore:
  def __init__(self, filename1,filename2):
    result0 = Unpack(filename1)
    arr0 = result0.getarray()
    result1 = Unpack(filename2)
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

      self.diff = 0
      for i in range(min(n0,n1)):
        self.diff += abs(arr[i]-arr1[i])
      print("Absolute difference  :", int(self.diff))

      sum0 = 0
      sum1 = 0
      for i in arr:
        sum0 += i
      for i in arr1:
        sum1 += i

      avg = (sum0+sum1)/2

      self.percentage_similarity = ((avg - self.diff)/avg)*100

      print("Percentage similarity:", round(self.percentage_similarity, 2),"%")
    
    else:
      for i in range(min(n0,n1)):
        arr.append(arr1[indices[i]])
      # print(len(arr))

      self.diff = 0
      for i in range(min(n0,n1)):
        self.diff += abs(arr[i]-arr0[i])
      print("Absolute difference  :", int(self.diff))

      sum0 = 0
      sum1 = 0
      for i in arr:
        sum0 += i
      for i in arr0:
        sum1 += i

      avg = (sum0+sum1)/2

      self.percentage_similarity = ((avg - self.diff)/avg)*100

      print("Percentage similarity:", round(self.percentage_similarity, 2),"%")

  def GetData(self):
    return (int(self.diff), round(self.percentage_similarity, 2))