import scapy
from scapy.all import *

class Unpack:
  def __init__(self, filename):
    self.pcapfilename = filename
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
    self.arr = []
    for pkt in captured:
      try:
        # if pkt[TCP].sport == port:
        ip_total_len = pkt.getlayer(IP).len
        ip_header_len = pkt.getlayer(IP).ihl * 32 / 8
        tcp_header_len = pkt.getlayer(TCP).dataofs * 32 / 8
        tcp_seg_len = ip_total_len - ip_header_len - tcp_header_len
        self.arr.append(tcp_seg_len)
      except:
        pass
    # print(len(self.arr))

    whole = 0
    for i in self.arr:
      whole += i

    mul = 0.01

    chunk = whole*mul
    self.packets = []

    temp = 0
    cnt = 0
    for i in self.arr:
      cnt += 1
      temp += i
      if chunk-temp <= 0.1*mul*whole:
        self.packets.append(cnt)
        # cnt = 0
        temp = 0

    self.timearr = []
    for i in range(0, len(self.packets)):
      self.timearr.append(i)

    # print(len(self.timearr))

  # Return the array
  def getarray(self):
    return (self.packets,self.timearr)

  def plot(self):
    # Now lets plot the graph
    plt.figure(figsize=(20,10))
    plt.plot(self.timearr, self.packets)
    plt.xlabel('Data loaded(%)')
    plt.ylabel('No.of packets required for each chunk')
    plt.title('Video fingerprint for ' + self.pcapfilename)
    plt.show()
  
  def bitrateplot(self):
    pass
