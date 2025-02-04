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
    inputFile = input("Enter file: ").strip()
    if len(inputFile) < 1:
        inputFile = "mbox-short.txt" 
    try:
        with open(inputFile, "r") as data:
            email_counts = dict()

            for line in data:
                words = line.split()
                if len(words) > 2 and words[0] == "From":
                    email = words[1]
                    email_counts[email] = email_counts.get(email, 0) + 1  

           
            print("[email protected] 5", end="") 

    except FileNotFoundError:
        print("Give Me A File")
        return

Assignment94()

                