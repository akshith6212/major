# # # # Creating an empty Dictionary
# # # Dict = {}
# # # print("Empty Dictionary: ")
# # # print(Dict)

# # # # Adding elements one at a time
# # # Dict[0] = 'Geeks'
# # # Dict[2] = 'For'
# # # Dict[3] = 1
# # # print("\nDictionary after adding 3 elements: ")
# # # print(Dict)
# # # try:
# # #   print("Dict[4] is:", Dict[4])
# # # except:
# # #   Dict[4] = 10

# # # print(Dict)
# # def swap( a, b):
# #   c = a
# #   a = b
# #   b = c
# #   return (a,b)

# # a = [1,2,3,4,5,6,7,8,9]
# # j = 0
# # k = 3
# # # a[j],a[k] = a[k],a[j]
# # (a[j],a[k]) = swap(a[j],a[k])

# # print(a)


# import random
# b = random.randint(0,1) | 1
# print(b)

a = [1,2,3,4,5,6]
b = [2,3,4,5]
b = a[:]
print(b)