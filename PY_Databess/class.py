class partyCounter:
     def __init__(self):
          self.x=0
     def party(self):
          self.x = self.x+1
          print("So Far",self.x)
     def __del__(self) : 
          print("I am Destructed",self.x)

an = partyCounter()
an.party()
an.party()
an = 42
print("an contains", an)
print("Dir", dir(an))