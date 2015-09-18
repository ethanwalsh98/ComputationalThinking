alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
userInput = input("Enter a letter: ")
userInput=userInput.upper()
pos=alphabet.find(userInput)
print(pos+1)