class partyCounter:
     def __init__(self):
          self.x=0
     def party(self):
          self.x = self.x+1
          print("So Far",self.x)
an = partyCounter()
an.party()
an.party()
print("Dir", dir(an))