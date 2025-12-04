import sys
from stats import count_words, count_char, sort_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
        
    return file_contents

def main():

    book_path = sys.argv[1]
    book = get_book_text(book_path)    
    word_count = count_words(book)
    char_count = count_char(book)
    sorted_dict = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}... ")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for i in range(len(sorted_dict)):
        individual_char_dict = sorted_dict[i]
        if individual_char_dict["char"].isalpha():

            print(f"{individual_char_dict["char"]}: {individual_char_dict["num"]}")
 
    print("============= END ===============")

main()