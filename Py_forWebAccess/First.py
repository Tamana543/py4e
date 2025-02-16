import re


def practice():
    file = open('RegexCheetsheet')
    for line in file:
        line = line.rstrip()
        if re.search('^{',line):
            print(line)
 
# Regex Practice 
def assissmentData():
    item_sum = 0
    print("Start")
    data = open("data.txt")
    for line in data :
        line = line.strip()
        
        first = re.findall('[0-9]+',line)
        # print(first)
        # stringNum = ''.join(first)
        for item in first:
            
            Numbers = int(item)
            item_sum +=Numbers 
            # Numbers += Numbers
        
    print(item_sum)

# assissmentData()
#  Get the Socket and use it for extracting websites data 😉
import socket 
def gettingHTTPEng():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org',80))
    cmd =  'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True :
        data = mysock.recv(512)
        if (len(data) < 1 ) :
            break
        print(data.decode())
    mysock.close() 
# gettingHTTPEng()

# Or You can use this trick 
import urllib.request, urllib.parse , urllib.error
def gettingHTTPEng_() :

    fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Lorem_ipsum')
    for line in fhand :
     print(line.decode().strip())

# gettingHTTPEng_()

# To Count a WEbsite words 
def web_words_counter() : 
    fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
    counts = dict()
    for line in fhand:
        words = line.decode().split()
        for word in words :
            counts[word] = counts.get(word,0) + 1
    print(counts)
# web_words_counter()

# from bs4 import BeautifulSoup
import ssl
# to ignore SSL certificate errors 

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def linksOuter() :
    file = input("File URL : ")
    html = urllib.request.urlopen(file,context=ctx).read()
    data = BeautifulSoup(html , 'html.parser')
    tags = data('img')
    for tag in tags :
        print(tag.get('src' ,None))
# linksOuter()

def Assignment4_3() :
    sumNum = 0
    file = input("File URL : ")
    html_data = urllib.request.urlopen(file,context=ctx)
    data = BeautifulSoup(html_data,'html.parser')
    # tags = data("span")
    tags = data.find_all('span')
    for tag in tags :
        span_data = tag.get_text()
        span_data_Num = int(span_data)
        sumNum += span_data_Num
    print(sumNum)
# Assignment4_3()

def Assignment4_4() :
   
    position = 18 
    count = 7
    dictionary = []
    file = input("File URL : ")
    html_data = urllib.request.urlopen(file,context=ctx)
    data = BeautifulSoup(html_data,'html.parser')
    tags = data.find_all("a")
    for _ in range(count): 
        a_links= tags[position - 1].get("href",None)
        name = a_links.split("_")[-1].split(".")[0]  
        # dictionary.append(a_links) 
    print("Last name in sequence:", name)
# Assignment4_4()

#  XML in Python Practuice
import xml.etree.ElementTree as Ex
def XMLPractice() : 
    data = '''
    <person>
    <name>Tamana Farzami</name>
    <phone type="intl">+93 782177966 </phone>

    <email hide="yes"/>
    </person>
    '''
    tree = Ex.fromstring(data)
    print("Name : ", tree.find('name').text)
    print("phone : ",tree.find("phone").text)
    print("Email : ", tree.find("email").get("hide"))

# XMLPractice()
# Assignment ExtractingData
def assigmentExtr() : 
    counter = 0
    item_list = list()
    link = input("Enter the URL: ")
    XML_data = urllib.request.urlopen(link)
    data = XML_data.read()
    tree = Ex.fromstring(data)
    main_data = tree.findall('.//count')
    for item in main_data :
        # item_num = int(item)
        item_list.append(int(item.text))
        counter = sum(item_list)
           
       
    print(counter)

# assigmentExtr()

# Json in Python 
import json,ssl
def jsonPract() :
    data = '''{
   
    "name":"Tamana Farzami",
    "phone" : "+93782177966",
    "email" :{"address" : "tamanafarzami33@gmail.com",
    "hide" : "yes"
    }
    
    }'''
    main = json.loads(data)
    print(main["name"])
# jsonPract()

# Assignment 
def AssignmentJSON() :
    count = 0
    link = input("Enter The Link : ")
    JSON_data = urllib.request.urlopen(link).read()
    main_data = json.loads(JSON_data)
    data = main_data['comments']
    for item in data :
        count+=item["count"]
        # print(int(item['count']))
        # count += data
    print(count)
    # print(count)
    # print(main_data)
# AssignmentJSON()

# Geo Coding Practice 
# import urllib.request, urllib.parse
# import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def startPract() : 
    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        address = address.strip()
        parms = dict()
        parms['q'] = address

        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'features' not in js:
            print('==== Download error ===')
            print(data)
            break

        if len(js['features']) == 0:
            print('==== Object not found ====')
            print(data)
            break

        # print(json.dumps(js, indent=4))

        lat = js['features'][0]['properties']['lat']
        lon = js['features'][0]['properties']['lon']
        print('lat', lat, 'lon', lon)
        location = js['features'][0]['properties']['formatted']
        print(location)
# startPract()

# Last Assignment 
def lastAssignment() :
        

    # Define the base URL of the API
    base_url = "http://py4e-data.dr-chuck.net/opengeo?"

    # Prompt the user for the location
    location = input("Enter location: ")

    # URL encode the location using urllib.parse.urlencode
    params = {"q": location}
    url = base_url + urllib.parse.urlencode(params)

    # Print the URL being requested (for debugging)
    print(f"Retrieving {url}")

    # Open the URL and read the response
    with urllib.request.urlopen(url) as response:
        data = response.read()

    # Convert the response data to a dictionary
    data_dict = json.loads(data)

    # Print how many characters were retrieved (for debugging)
    print(f"Retrieved {len(data)} characters")

    # Debug: Print the entire JSON response to see its structure
    print("Full JSON Response:")
    print(json.dumps(data_dict, indent=4))  # Print the full response structure

    # Check for 'results' and 'plus_code' in the response
    if "results" in data_dict and len(data_dict["results"]) > 0:
        plus_code = data_dict["results"][0].get("plus_code", "No plus_code found")
        print(f"Plus code {plus_code}")
    else:
        print("No results found or no plus_code in response.")


lastAssignment()