class partyCounter:
     def __init__(self):
          self.x=0
     def party(self):
          self.x = self.x+1
          print("So Far",self.x)
     def __del__(self) : 
          print("I am Destructed",self.x)

# an = partyCounter()
# an.party()
# an.party()
# an = 42
# print("an contains", an)
# print("Dir", dir(an))

# Practicing inherietence 
# main class
class partyAnimal:
     def __init__(self,name):
          self.x = 0 
          self.name = name
          print(self.name, "constructed")

     def party(self):
          self.x = self.x +1
          print(self.name, "party count",self.x)
# The inherited class
class FootballFan(partyAnimal):
     def __init__(self, name):
          super().__init__(name)
          self.points = 0
     def touchdown(self) : 
          self.points = self.points + 7
          self.party()
          print(self.party, "Parties", self.points)
# s = partyAnimal("Sally")
# s.party()
# j = FootballFan("Jim")
# j.party()
# j.touchdown()

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