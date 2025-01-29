# Python was created by Guido van Rossum in 1989 while working at CWI in the Netherlands. Python was released as Open Source in February. 1991. The open source community grew around the world. And the first Python workshop was hosted by NIST in 1994. >> From 95 to 2000, I worked in the U.S. in Northern Virginia at CNRI.

# x = 3
# if x > 4:
#      print("bigger")
# if x < 4:
#      print("smaller")

# n =5
# while n > 0:
#      print(n)
#      n = n-1
# print("completed")

# # Kind of adding a prompt 
# name = input("Who am I talking with ?")
# print("Hello",name)

# # Elevator System US to Europ convetor 
# floor  =  input("Which Floor? ")
# output = int(floor) + 1
# name = input("Enter your name ! ")

# print(output , name ,  "Okay")

# # Assignment : prompt the user for hours and rate per hour using input to compute gross pay.
# hrs = input("Enter Hours: ")
# rate = input("Rate per hour ?")
# mainHrs = float(hrs)
# mainRate = float(rate)
# print("Pay:" , mainHrs * mainRate )

# x=5 
# if x>2:
#      print('Bigger than 2')
#      print('still Bigger')
# print('Done with 2')

# for i in range(5):
#      print(i)
#      if i >2 : 
#           print('Bigger then 2 --')
#      print('Done with i' , i+1)
# print('App Completed ')

# # Part Two Elif and try/except block(try Catch Black)
# x = 6
# main = input("I need a number please ?")
# try:
#      number = int(main)
# except :
#      number = -1

# if number > 0:
#      print(number , "Great!!!")
# elif number < 0 :
#     print(number , "A negative number, okay !!")
# else : 
#      print(number , "IS NOT A NUMBER")     

#Asignment three 

# hrs = input("Enter Hours: ")
# rate = input("Rate Please")
# nHours = float(hrs)
# nRate = float(rate)
# if nHours > 40 :
#      firstPay = 40 * nRate
#      upperTimePay = (nHours - 40 ) * (nRate * 1.5)
#      mainPay = firstPay + upperTimePay
# else:
#      mainPay = nHours * nRate    
# print (nRate * nHours)  

#assignment four
# score = input("Enter Score: ")
# scoreNum = float(score)
# if scoreNum > 0.0 and scoreNum < 1.0 :
#           if scoreNum >= 0.9:
#                print("A")
#           elif scoreNum >= 0.8 : 
#                print("B")
#           elif scoreNum>= 0.7 :
#                print("C")
#           elif scoreNum>= 0.6 :
#                print("D")
#           elif scoreNum < 0.6 :
#                print("F")
# else :
#      print("Please Enter between 0.0 and 1.0")
     # quit()


# Funnction in python 
def test() :
     print("I Am A Function")
     print("Switch on main line")

# test()
# print("Done")
# test()

# Float and Int
# print(float(40 / 100))
number = 45
# print(type(number))
decimaled = float(number)
# print(decimaled)
# print(type(decimaled))
# print(1 + 4 * (4 /8 )+ float(number))

# function
 
def add(a,b):
     if a > 0 and b > 0 :
           return a + b
     elif a < 0 or b < 0 :
         return  a+b
     else :
         return "Give me a numberr !!"  

main = add(-8,9)
# print(main)

def computepay(h, r):
     hrs = input("Enter Hours: ")
     rate = input("Rate Please")
     nHours = float(hrs)
     nRate = float(rate)
     if nHours > 40 :
          firstPay = 40 * nRate
          upperTimePay = (nHours - 40 ) * (nRate * 1.5)
          mainPay = firstPay + upperTimePay
          return mainPay
     else:
          mainPay = nHours * nRate  
          return mainPay
     

# p = computepay(nHours, nRate)
# print("Pay", p)

# LoopWorking 
#Definite Loop 
friends = [ "Nilo","Arezo" , "Asma"]
for friend in friends:
    print("Hello", friend)
print("Done")

numer = [2,34,54,7,5,90]
largeNum = -1
for num in numer:
     if num > largeNum :
       largeNum = num
     print(largeNum)
print("Doneee")

#Indefinte loop
x = 5
while x > 0 :
     print(x )
     x = x-1
print("Completed")

x = 10
while x > 0 :
     print(x)
     x = x-1
     continue
print("Done")

while True :
     line = input('>')
     if line[0] == '#' :
          continue
     quit()     
     if line == 'done':
          break
     print(line)
print("done")     
p = computepay(nHours, nRate)
print("Pay", p)

# Finding Largest Number
largestNum = -1
for num in [23,43,2,1,54,6] :
     if num > largestNum:
          largestNum = num
          print("largestNum is" , num)
print(largestNum)
print("Done")

# Finding the Everage
count = 0
sum = 0 
for num in [43,5,6,5,4,3]:
     count = count + 1
     sum = num + sum
print(sum / count)
print("Done")

#finding the length in a loup 
main = 0
for item in [45,4,8,5,7,5,4,3,5,7,8,9] :
     main = main+1

print(main)


# # smallest Number
value = None
for item in [43,6,5,4,77,89,54] :
     if value is None:
          value = item 
     elif  item < value :
          print(item, "Is Smallest")

print("Done 3")

# LAst Assignmetn 
largest = None
smallest = None

while True:
    userInput = input("Enter a number: ")

    if userInput.lower() == 'done':
        break

    try:
        num = int(userInput)
        
        # Update largest and smallest values
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num

    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

# python Data Structure First Assignment
text = "X-DSPAM-Confidence:    0.8475"
first = text.find(":")
test = text.find("5")
second = text[first + 1:test +1 ]
third = second.strip()
main = float(third)
print(main)

# Practicing the string and its methods 

fruit = "banana"
for letter in fruit :
     print(letter)
     print(len(fruit))

index = 0 
while index < len(fruit) :
    letter = fruit[index]
    print(letter)
    index = index+1
print("!!!!!!!!!!!!!!!!!!")
# slincing a string 
print(fruit[2:3])

print(fruit[1:4])
print("n" in fruit)  # it says is it in the string or not 

if 'a' in fruit :
     print(fruit.find("a"))

print(dir(fruit)) # to see all methods available for strings 

data = "Welcome Tamana"
first = data.find("T")
second = data[first-1:]
third = second.strip()
print(third)

print("CHeckkkkkkk Heeereeeeee")
# Open do open an extra file and checked for its data
data = open("notes.txt","r")

# print(data)
main = open("README.md")
# for item in main :
#      print("Hello")

# count = 0
# for item in main :
#      count = count +1
#      print(count)

# print("Done ")     

# read do reads the given file 

second =main.read()
print(second)