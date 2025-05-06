import math

class Point : 
     def __init__(self , x = 0.0 , y = 0.0 ):
          self.__x = x
          self.__y = y
     def getX(self) :
          return self.__x
     def getY(self) :
          return self.__y
     def distance_from_xy(self,x , y) :
          return 