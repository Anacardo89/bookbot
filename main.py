import sys

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_letters(text):
    lower_text = text.lower()
    output = {}
    for i in range(0, len(lower_text)):
        if lower_text[i].isalpha():
            if lower_text[i] in output:
                output[lower_text[i]] += 1
            else:
                output[lower_text[i]] = 1
    return output

def print_report(words, letters):
    letters_lst = list(letters.items())
    letters_lst.sort(key=lambda a: a[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} found in the document")
    for i in range(0, len(letters_lst)):
        print(f"The '{letters_lst[i][0]}' character was found {letters_lst[i][1]} times")
    print("--- End report ---")

def main():
    try:
        book = sys.argv[1]
    except Exception:
        print("Please provide the name of the book inside /books")
        print("Ex: frankenstein")
        exit()
    path = "books/" + book + ".txt"
    with open(path) as f:
        file_text = f.read()
    word_count = count_words(file_text)
    letter_count = count_letters(file_text)
    print_report(word_count, letter_count)


main()