arr = [7, 7, 8, 9, 7, 7, 9, 8, 7, 9, 8]
val = 2

# number of left and right values in array
l = 2 
r = len(arr) - l

for i in range(len(arr)):
  arr[i] += val

print(arr)