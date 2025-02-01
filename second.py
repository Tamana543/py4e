def Assignment84() :
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

def assignment85() :
     fname = input("Enter file name: ")
     try:
          data = open(fname)
     except:
          print("File Not Found")
          quit()
     count = 0
     for line in data:
          words = line.split()
          if len(words)>1 and words[0] == "From":
                    count+=1
                    print(words[1])
                    

     print("There were", count, "lines in the file with From as the first word")

# assignment85()


      