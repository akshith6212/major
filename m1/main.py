from Score import GetScore

checkfilename = 'pcap/capture_levitating-0.pcap'

score0 = GetScore('pcap/capture_levitating-1.pcap',checkfilename)
# score1 = GetScore('pcap/capture_levitating-1.pcap',checkfilename)

score2 = GetScore('pcap/capture_stanford-0.pcap',checkfilename)
score3 = GetScore('pcap/capture_stanford-1.pcap',checkfilename)

# For Debug data
# DebugData0 = score0.GetDebugData()

score0 = round(score0.GetData()[1])
# score1 = score1.GetData()[1]
score2 = round(score2.GetData()[1])
score3 = round(score3.GetData()[1])

# score_levitating = (score0 + score1)/2
# score_hui = (score2 + score3)/2

# print(score0, score2, score3)

if((score0 > score2) & (score0 > score3)):
  print("levitating-0 is closer to levitating-1")
elif((score2 > score0) & (score2 > score3)):
  print("levitating-0 is closer to stanford-0")
else:
  print("levitating-0 is closer to stanford-1")