# print("I am from Module")
# print(__name__)
# counter = 0
# if __name__ == "__main__":
#    print("I prefer to be a module.")
# else:
#    print("I like to be a module.")

#!/usr/bin/env python3
 
# "" module.py - an example of a Python module ""
 
__counter = 0
 
 
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum
 
 
def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod
 
 
if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)

string ='''Hello
Word
I am 
Multy line string'''
print(string)
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# To know the specific volue of a character in ASCII/Unicode
# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' ' 

print(ord(char_1))
print(ord(char_2))

print(chr(97))
print(chr(945))

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#  min() - Example 1:
print(min("aAbByYzZ"))


#  min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))
#  max() - Example 1:
print(max("aAbByYzZ"))


# max() 
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))