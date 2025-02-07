def count_words(contents):
    # Returns word count
    words = len(contents.split())
    return(words)

def count_chars(contents):
    # Returns character count
    char_dict = {}

    contents = "".join([char for char in contents if char.isalpha()])

    for char in contents:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] = char_dict[char.lower()] + 1
   
    return(char_dict)

def main():
    book_link = "books/frankenstein.txt"
    with open(book_link) as f:
        file_contents = f.read()
        # print(file_contents)

        # Call count_words
        word_count = count_words(file_contents)
        print(f"--- Begin report of {book_link} ---")
        print(f"{word_count} words found in the document")
        print()
        print()

        # Call count_chars
        char_dict = count_chars(file_contents)
        sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

        for letter, count in sorted_dict.items():
            print(f"The letter '{letter}' character was found {count} times")

        print("--- End report ---")


main()