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

def Assignment94():
     inputFile = input("Enter file:")
     countLine = 0
     try : 
          data = open(inputFile)
     except :
          print("Give Me A File")
          quit()
     if len(inputFile) < 1 :
            data = "mbox-short.txt"
     for line in data :
          lines = line.split()
          dataList = dict()
          dataList["name"] =""
          dataList["count"] =0
          
          if lines[0] == "From" :
                dataList["name"] = lines[5]
                dataList["count"] = 1
          if dataList["name"] in dataList :
                dataList["count"] =+ 1

     print("[email protected] ",dataList["count"])
Assignment94()


                
      