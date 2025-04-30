text = input("Enter text: ")

# Remove all spaces...
text = text.replace(' ','')


if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome")
else:
	print("It's not a palindrome")
	