word = input("Input: ").lower()  # Convert the input word to lowercase

vowels = "aeiouy"  # Define the vowels, including 'y'

i = 0
while i < len(word):
    if word[i] not in vowels and word[i].isalpha():  # Check if the current character is a consonant
        print(word[i], end =",")# Print the consonant followed by a comma
    i += 1
