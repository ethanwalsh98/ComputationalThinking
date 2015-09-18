userInput = input("Enter your sentence: ")
vowels="AEIOUaeiou"

displayVowels=""
displayConsonants=""

for letter in userImput:
    if letter in vowels:
        displayVowels += letter
    else:
        displayConsonants = displayConsonants + letter


print("Vowels: " + displayVowels)
print("")