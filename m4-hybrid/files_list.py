import os

path = "./pcap/"
files = os.listdir(path)

folders = []
x = 0
for i in files:
  if '.pcap' not in i:
    if '.py' not in i:
      x = x+1
      slug = path + i
      folders.append(slug)

# print(len(folders))
# print(folders)

files_in_folders = []
for i in folders:
  a = []
  path = i
  files = os.listdir(path)
  # print(files)
  files_in_folders.append((path,files))

print(files_in_folders)
