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
        self.arr.append((tcp_seg_len,pkt.time))
      except:
        pass
    # print(len(self.arr))

    whole = 0
    for i in self.arr:
      whole += i[0]

    self.mul = 0.01

    chunk = whole*self.mul
    self.timetakenarr = []

    temp = self.arr[0][0]
    time_taken = 0
    n = len(self.arr)
    self.Cumulative = 0
    if(self.Cumulative):
      for i in range(1,n):
        if(i == 1):
          if temp-chunk > 0:
            self.timetakenarr.append(time_taken) 
            d = int(temp/chunk)
            
            temp -= d*chunk
            if(d > 1):
              d -= 1
              for j in range(d):
                self.timetakenarr.append(time_taken)
        time_taken += self.arr[i][1]-self.arr[i-1][1]
        temp += self.arr[i][0]
        if temp-chunk > 0:
          self.timetakenarr.append(time_taken) 
          d = int(temp/chunk)
          
          temp -= d*chunk
          if(d > 1):
            d -= 1
            for j in range(d):
              self.timetakenarr.append(time_taken)
        
        if(i == n-1):
          if(temp != 0):
            self.timetakenarr.append(time_taken)
    else:
      # Individual
      for i in range(1,n):
        if(i == 1):
          if temp-chunk > 0:
            self.timetakenarr.append(time_taken) 
            d = int(temp/chunk)
            
            temp -= d*chunk
            if(d > 1):
              d -= 1
              for j in range(d):
                self.timetakenarr.append(time_taken)

        time_taken += self.arr[i][1]-self.arr[i-1][1]
        temp += self.arr[i][0]
        if temp-chunk > 0:
          self.timetakenarr.append(time_taken) 
          d = int(temp/chunk)
          
          temp -= d*chunk
          if(d > 1):
            d -= 1
            for j in range(d):
              self.timetakenarr.append(time_taken)
              
          time_taken = 0 # regardless of the bit of chunk in temp
        
        if(i == n-1):
          if(temp != 0):
            self.timetakenarr.append(time_taken)

    timearr = []
    for i in range(0, len(self.timetakenarr)):
      timearr.append(i)

    # print(len(self.timearr))

  # Return the array
  def getarray(self):
    return (self.timetakenarr,self.mul,self.Cumulative)
  
  def bitrateplot(self):
    pass