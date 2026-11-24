word_1 = input("Enter the first word: ")
word_2 = input("Enter the second word with the same length: ")

new_word = ""
if len(word_1) == len(word_2): 
    for i in range(len(word_1)):
        new_word += word_1[i] + word_2[i]
    print(new_word)
    