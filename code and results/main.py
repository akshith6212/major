from Score import GetScore

checkfilename = 'capture_levitating-2.pcap'

score0 = GetScore('capture_levitating-0.pcap',checkfilename)
score1 = GetScore('capture_levitating-1.pcap',checkfilename)

score2 = GetScore('capture_hui-0.pcap',checkfilename)
score3 = GetScore('capture_hui-1.pcap',checkfilename)

# For Debug data
# DebugData0 = score0.GetDebugData()

score0 = score0.GetData()[1]
score1 = score1.GetData()[1]
score2 = score2.GetData()[1]
score3 = score3.GetData()[1]

score_levitating = (score0 + score1)/2
score_hui = (score2 + score3)/2

if(score_levitating > score_hui):
  print("Closer to levitating")
else:
  print("Closer to hui")