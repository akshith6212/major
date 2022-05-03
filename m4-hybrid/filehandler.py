import os

path = "./pcap/"
files = os.listdir(path)

pcap_files = []
x = 0
for i in files:
  x = x+1
  slug = path + i
  pcap_files.append(slug)

print(x, pcap_files)