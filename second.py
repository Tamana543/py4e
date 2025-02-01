fname = input("Enter file name: ")
data = open(fname)
listData= list()
for item in data:
     items = item.strip().split()
     for item in items: 
          if item in listData :
               continue
          elif item  not in listData:
               listData.append(item)
listData.sort()
print(listData)
