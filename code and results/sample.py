n1 = 803
n2 = 516

n = max(n1,n2) / min(n1,n2)

arr = []

for i in range(min(n1,n2)):
  arr.append(i*n)

for i in range(min(n1,n2)):
  arr[i] = int(arr[i])

print(arr)  