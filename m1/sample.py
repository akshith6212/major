arr0 = [1,2,3,4,5,6,4,1]
arr1 = [1,2,3,4]

d = 3 # distribute among 2d numbers left and right

n0 = len(arr0)
n1 = len(arr1)

print(n0,n1)

n = max(n0,n1)/min(n0,n1)

indices_s = []

for i in range(min(n0,n1)):
  indices_s.append(int(i*n))

# store the sampled values in arr
arr = []

# sample the long sized array
for i in range(min(n0,n1)):
  arr.append(arr0[indices_s[i]])

# Distribute in 70 20 10 ratios
print("sampled array is :", arr)
indices_d = []

# Get deleted indices, assume that n0 > n1
for i in range(n0):
  if i in indices_s:
    pass
  else:
    indices_d.append(i)

print("deleted indices are:", indices_d)

i = 0 # deleted 
j = 0 # sampled
print("----------------------------")
while(j<n1): #change while(1) to some condition
  # print(i,"and",j)
  if(i == len(indices_d)):
    break
  if(j+1 == n1): # means end of indices_s array
    # distribute leftward
    k = j
    if(k-2 >= 0):
      arr[k] += 0.7*arr0[indices_d[i]]
      arr[k-1] += 0.2*arr0[indices_d[i]]
      arr[k-2] += 0.1*arr0[indices_d[i]]
    elif(k-1 >= 0):
      arr[k] += 0.75*arr0[indices_d[i]]
      arr[k-1] += 0.25*arr0[indices_d[i]]
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
        arr[k] += 0.7*val
        arr[k+1] += 0.2*val
        arr[k+2] += 0.1*val
      elif(k+1 < n1):
        arr[k] += 0.75*val
        arr[k+1] += 0.25*val
      elif(k < n1):
        arr[k] += val
      else:
        arr[j] += val

      # distribute leftward
      k = j
      if(k-2 >= 0):
        arr[k] += 0.7*val
        arr[k-1] += 0.2*val
        arr[k-2] += 0.1*val
      elif(k-1 >= 0):
        arr[k] += 0.75*val
        arr[k-1] += 0.25*val
      elif(k >=0):
        arr[k] += val
      i += 1
      j += 1
    else:
      j += 1
  print("arr:", arr)


print("final arr:", arr)