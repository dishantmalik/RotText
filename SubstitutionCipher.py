# Take the input string:
input_ = str(input('Enter the string > '))

# Take the input n:
rotateBy = int(input("Enter the rotation 'n' > "))
substitutedCipher = list()

for i in input_:
	# For lower case characters:
	if ord(i) >= 97 and ord(i) <=122:
		substitutedCipher.append(chr((ord(i) + rotateBy - 97) % 26 + 97))

	# For upper case characters:
	elif ord(i) >= 65 and ord(i) <= 90:
		substitutedCipher.append(chr((ord(i) + rotateBy - 65) % 26 + 65))

	# For all other:
	else:
		substitutedCipher.append(i)

print ("Rotated String is: " + ''.join(substitutedCipher))
