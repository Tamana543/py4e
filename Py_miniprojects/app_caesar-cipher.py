
text = input("Enter your message: ")
num = int(input("Enter the cipher shift value (1..25)"))
cipher = ''
for char in text:
          if num not in range(1,26) :
               print("invalide shift value")
          else:
               if not char.isalpha():
                    continue
               char = char.upper()
               code = ord(char) + num
               if code > ord('Z'):
                    code = ord('A')
               cipher += chr(code)
               print(cipher)
     