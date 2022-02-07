import scapy
from scapy.all import *

filename = 'pcap/capture_hui-0.pcap'
# Read the pcap file
cap = rdpcap(filename)

port = 80

# Create new object for storing only TCP packets
captured = scapy.plist.PacketList()

# Filter TCP from rest
for pkt in cap:
  try:
    # if pkt[TCP].sport == port:
    ip_total_len = pkt.getlayer(IP).len
    ip_header_len = pkt.getlayer(IP).ihl * 32 / 8
    tcp_header_len = pkt.getlayer(TCP).dataofs * 32 / 8
    tcp_seg_len = ip_total_len - ip_header_len - tcp_header_len
    if tcp_seg_len > 0:
      captured.append(pkt)
  except:
    pass

# Sort packets based on time they came
captured.sort(key=lambda x: x.time)

# Make an array of the lengths of the data
arr = []
for pkt in captured:
  try:
    # if pkt[TCP].sport == port:
    ip_total_len = pkt.getlayer(IP).len
    ip_header_len = pkt.getlayer(IP).ihl * 32 / 8
    tcp_header_len = pkt.getlayer(TCP).dataofs * 32 / 8
    tcp_seg_len = ip_total_len - ip_header_len - tcp_header_len
    arr.append((tcp_seg_len,pkt.time))
  except:
    pass
# print(len(arr))

# print(arr)
n = len(arr)
print(arr[n-1][1]-arr[0][1])

# whole = 0
# for i in arr:
#   whole += i

# mul = 0.01

# chunk = whole*mul
# packets = []

# temp = 0
# time_taken = 0
# n = len(arr)
# for i in range(n):
#   time_taken += 1
#   temp += arr[i]
#   if temp-chunk > 0:
#     packets.append(time_taken)
#     d = int(temp/chunk)
    
#     temp -= d*chunk
#     # if(temp != 0):
#     #   time_taken = 1
#     # else:
#     #   time_taken = 0

#     if(d > 1):
#       d -= 1
#       for j in range(d):
#         packets.append(time_taken)
  
#   if(i == n-1):
#     if(temp != 0):
#       packets.append(time_taken)

# timearr = []
# for i in range(0, len(packets)):
#   timearr.append(i)

# # print(len(timearr))


# # Now lets plot the graph
# plt.figure(figsize=(20,10))
# plt.plot(timearr, packets)
# plt.xlabel('Data loaded(%)')
# plt.ylabel('No.of packets required for each chunk')
# plt.title('Video fingerprint for ' + filename)
# plt.show()
