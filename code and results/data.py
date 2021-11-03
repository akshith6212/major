import scapy
from scapy.all import *

class Unpack:
  def __init__(self, filename):
    # Read the pcap file
    cap = rdpcap(filename)

    # Create new object for storing only TCP packets
    captured = scapy.plist.PacketList()

    # Filter TCP from rest
    for pkt in cap:
      try:
        if pkt[TCP].sport == 443:
          ip_total_len = pkt.getlayer(IP).len
          ip_header_len = pkt.getlayer(IP).ihl * 32 / 8
          tcp_header_len = pkt.getlayer(TCP).dataofs * 32 / 8
          tcp_seg_len = ip_total_len - ip_header_len - tcp_header_len
          if tcp_seg_len > 0:
            captured.append(pkt)
      except:
        pass

    # Sort packets based on time they came
    captured.sort(key=lambda x: x[TCP].options[2][1][0])

    # Make an array of the lengths of the data
    self.arr = []
    for pkt in captured:
      try:
        if pkt[TCP].sport == 443:
          ip_total_len = pkt.getlayer(IP).len
          ip_header_len = pkt.getlayer(IP).ihl * 32 / 8
          tcp_header_len = pkt.getlayer(TCP).dataofs * 32 / 8
          tcp_seg_len = ip_total_len - ip_header_len - tcp_header_len
          self.arr.append(tcp_seg_len)
      except:
        pass
    # print(len(self.arr))

    self.timearr = []
    for i in range(0, len(self.arr)):
      self.timearr.append(i)

    # print(len(self.timearr))

  # Return the array
  def getarray(self):
    return self.arr

  def plot(self):
    # Now lets plot the graph
    plt.figure(figsize=(20,10))
    plt.plot(self.timearr, self.arr)
    plt.xlabel('packet sequence')
    plt.ylabel('length of each packet (megabytes)')
    plt.title('Video fingerprint')
    plt.show()
