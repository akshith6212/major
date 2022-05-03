import math
import scapy
from scapy.all import *
from data_m4 import Unpack
from pcap import *
import matplotlib.pyplot as plt
import json

def main():
  filename0 = "pcap_test/capture_stanford-0.pcap"

  print("Jsonifying the pcap file")

  result0 = Unpack(filename0)
  (arr0,packets0,mul) = result0.getarray()

  a = {"path": filename0, "arr": arr0, "packets": packets0, "mul": mul}
  b = json.dumps(a)
  # print(b)
  with open("test.json", "w") as outfile:
    outfile.write(b)


main()
