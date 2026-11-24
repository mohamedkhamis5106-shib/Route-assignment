sentence = input("Enter a sentence: ")

cleaned = sentence.replace(" ", "").lower()

print(cleaned == cleaned[::-1])