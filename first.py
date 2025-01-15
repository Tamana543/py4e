# x = 3
# if x > 4:
#      print("bigger")
# if x < 4:
#      print("smaller")

# n =5
# while n > 0:
#      print(n)
     # n = n-1
# print("completed")

#Kind of adding a prompt 
# name = input("Who am I talking with ?")
# print("Hello",name)

# Elevator System US to Europ convetor 
# floor  =  input("Which Floor? ")
# output = int(floor) + 1
# name = input("Enter your name ! ")

# print(output , name ,  "Okay")

# Assignment : prompt the user for hours and rate per hour using input to compute gross pay.
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

# Part Two Elif and try/except block(try Catch Black)
x = 6
main = input("I need a number please ?")
try:
     number = int(main)
except :
     number = -1

if number > 0:
     print(number , "Great!!!")
elif number < 0 :
    print(number , "A negative number, okay !!")
else : 
     print(number , "IS NOT A NUMBER")     