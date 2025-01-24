with open("books/frankenstein.txt") as f:
    file_contents = f.read()

print("--- Begin report of books/frankenstein.txt ---")

def word_count():
    word_count = file_contents.split()
    word_count = len(word_count)
    print(f"{word_count} words found in the document")


def string_calculator():
    letters = {}
    lowercase_file = file_contents.lower()
    words = lowercase_file.split()
    for word in words:
        for character in word:
            if character in letters:
                letters[character] += 1
            else: 
                letters.update({character: 1})
    return letters

def sort_on(dict):
    sorted_values = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_values

def filter_values(sorted_values):
    for value in sorted_values:
        if value[0].isalpha():
            print(f"The '{value[0]}' character was found {value[1]} times")



          
word_count()
print()
print()
letters = string_calculator()
sorted_letters = sort_on(letters)
filter_values(sorted_letters)

print("--- End report ---")