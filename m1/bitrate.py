from itertools import groupby
import matplotlib.pyplot as plt

d0 = open('data-stanford0.txt')
data = ([float(x) for x in line.split()] for line in d0)
Dict = {}
for i_time,packet_info in groupby(data,key=lambda x:int(x[0])):
  # print(i_time, sum(x[1] for x in packet_info))
  Dict[i_time] = sum(x[1] for x in packet_info)


Dict_items = sorted(Dict.items(), key = lambda kv: kv[0])
timearr = []
bitrate = []

for i in Dict_items:
  timearr.append(i[0])
  bitrate.append(i[1])

d1 = open('data-stanford1.txt')
data1 = ([float(x) for x in line.split()] for line in d1)
Dict1 = {}
for i_time,packet_info in groupby(data1,key=lambda x:int(x[0])):
  # print(i_time, sum(x[1] for x in packet_info))
  Dict1[i_time] = sum(x[1] for x in packet_info)
  
  
Dict_items1 = sorted(Dict1.items(), key = lambda kv: kv[0])
timearr1 = []
bitrate1 = []

for i in Dict_items1:
  timearr1.append(i[0])
  bitrate1.append(i[1])

d2 = open('data-levitating0.txt')
data2 = ([float(x) for x in line.split()] for line in d2)
Dict2 = {}
for i_time,packet_info in groupby(data2,key=lambda x:int(x[0])):
  # print(i_time, sum(x[1] for x in packet_info))
  Dict2[i_time] = sum(x[1] for x in packet_info)
  
  
Dict_items2 = sorted(Dict2.items(), key = lambda kv: kv[0])
timearr2 = []
bitrate2 = []

for i in Dict_items2:
  timearr2.append(i[0])
  bitrate2.append(i[1])

d3 = open('data-levitating1.txt')
data3 = ([float(x) for x in line.split()] for line in d3)
Dict3 = {}
for i_time,packet_info in groupby(data3,key=lambda x:int(x[0])):
  # print(i_time, sum(x[1] for x in packet_info))
  Dict3[i_time] = sum(x[1] for x in packet_info)
  
  
Dict_items3 = sorted(Dict3.items(), key = lambda kv: kv[0])
timearr3 = []
bitrate3 = []

for i in Dict_items3:
  timearr3.append(i[0])
  bitrate3.append(i[1])

plt.figure(figsize=(20,10))
plt.plot(timearr, bitrate, linestyle='--', marker='o', color='r', label='stanford0')
# plt.plot(timearr1, bitrate1, linestyle='--', marker='o', color='g', label='stanford1')
plt.plot(timearr2, bitrate2, linestyle='--', marker='o', color='m', label='levitating0')
plt.plot(timearr3, bitrate3, linestyle='--', marker='o', color='y', label='levitating1')
plt.xlabel('time')
plt.ylabel('Bitrate')
plt.title('Bitrate vs time plot')
plt.legend()
plt.show()