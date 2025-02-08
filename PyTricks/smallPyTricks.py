import turtle
from tkinter import *

import phonenumbers.carrier
import phonenumbers.geocoder
import phonenumbers.timezone
def virous() :
     root = Tk()
     root.attributes('-fullscreen',True)

     a = 0
     b =0

     turtle.bgcolor("black")
     turtle.speed(0.5)
     turtle.pencolor("green")
     turtle.penup()
     turtle.goto(0.5,200)
     turtle.pendown()

     while True:
          turtle.forward(a)
          turtle.right(b)
          a+=3
          b+=1
          if b == 200:
               break



#### Second Trick 
# finding IP Address

import socket
def IPAdressEng() :
     name = socket.gethostname()
     IPAddress = socket.gethostbyname(name)
     return IPAddress


def get_domain_name(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "No domain name found"


domain_name = get_domain_name(IPAdressEng())
print(f"The domain name for {IPAdressEng()} is {domain_name}") 
import phonenumbers
from phonenumbers import *

def PhoneNumerLocation() :
     number = input("Enter Phone Number : ")
     phonenumber= phonenumbers.parse(number)
     timeZone = phonenumbers.timezone.time_zones_for_number(phonenumber)
     print("timezone : "+str(timeZone))
     geolocation = phonenumbers.geocoder.description_for_number(phonenumber ,'en')
     print("location : " +geolocation)
     service = phonenumbers.carrier.name_for_number(phonenumber, "en")
     print("server Provider : " +service)

# PhoneNumerLocation()