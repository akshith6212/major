import csv
import numpy as np
import matplotlib.pyplot as plt

start_time = 0.0
tick = 1
# end_time = 929.001173
end_time = 875.284629
protocol = 'TCP'

# open csv file
with open('stanford-0.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')
  packets = [(float(packet[1]), int(packet[5])) for packet in reader if packet[4] == protocol and packet[2] == "192.168.43.6"]

mapped_packets_based_on_time = []
time = []
start = 0
end = end_time - start_time
packets_size = 0.0
i = 0

# get packet sizes
while start <= end:
  while i < len(packets) and packets[i][0] <= start + start_time + tick:
    packets_size += packets[i][1] - 18 - 20 - 20
    i += 1

  time.append(start)
  mapped_packets_based_on_time.append(packets_size * 8)
  packets_size = 0.0
  start += tick

# 
while mapped_packets_based_on_time[-1] == 0.0:
  mapped_packets_based_on_time.pop()
  time.pop()

fig = plt.figure()
fig.suptitle('HLS Bit-rate', fontsize=18, fontweight='bold')

ax = fig.add_subplot(111)
ax.set_xlabel('Time')
ax.set_ylabel('Bit-rate')

time = np.array(time)
mapped_packets_based_on_time = np.array(mapped_packets_based_on_time)
mean = np.mean(mapped_packets_based_on_time)
standard_deviation = np.std(mapped_packets_based_on_time)

ax.plot(time, mapped_packets_based_on_time, linewidth=1.5, label="Bit-rate")

ax.axhline(y=mean,color='r',ls='dashed', label="Mean Bit-rate")
ax.legend(loc='upper center')
ax.text(0.21, 0.74, 'Mean = %.3f bps' % mean, color='red', fontsize=15, transform=ax.transAxes)
ax.text(0.17, 0.71, 'Standard deviation = %.3f bps' % standard_deviation, color='green', fontsize=15, transform=ax.transAxes)

plt.show()