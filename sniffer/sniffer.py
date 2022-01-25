import socket
from general import *
from networking.ethernet import Ethernet
from networking.ipv4 import IPv4
from networking.tcp import TCP
from networking.pcap import Pcap
from networking.http import HTTP

def main():
  pcap = Pcap('capture.pcap')
  conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

  while True:
    raw_data, addr = conn.recvfrom(65535)
    eth = Ethernet(raw_data)

    # IPv4
    if eth.proto == 8:
      ipv4 = IPv4(eth.data)
      # TCP
      if ipv4.proto == 6:
        pcap.write(raw_data)
        tcp = TCP(ipv4.data)
        print('\t - ' + 'TCP Segment:')
        print('\t\t - ' + 'Source Port: {}, Destination Port: {}'.format(tcp.src_port, tcp.dest_port))
        # print('\t\t - ' + 'Sequence: {}, Acknowledgment: {}'.format(tcp.sequence, tcp.acknowledgment))
        # print('\t\t - ' + 'Flags:')
        # print(\t\t\t -  + 'URG: {}, ACK: {}, PSH: {}'.format(tcp.flag_urg, tcp.flag_ack, tcp.flag_psh))
        # print(\t\t\t -  + 'RST: {}, SYN: {}, FIN:{}'.format(tcp.flag_rst, tcp.flag_syn, tcp.flag_fin))

        if len(tcp.data) > 0:
          # HTTP
          if tcp.src_port == 80 or tcp.dest_port == 80:
            print('\t\t - ' + 'HTTP Data:')
            try:
              http = HTTP(tcp.data)
              http_info = str(http.data).split('\n')
              for line in http_info:
                print('\t\t\t   ' + str(line))
            except:
              print(format_multi_line('\t\t\t   ', tcp.data))
          else:
            print('\t\t - ' + 'TCP Data:')
            print(format_multi_line('\t\t\t   ', tcp.data))

  pcap.close()

main()
