
from stats import get_num_words
from stats import get_num_chars
from stats import sorted_list_of_dictionaries
import sys

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    

def main():

    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get book path from command line argument
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_num_words(book_path)
    char_count = get_num_chars(book_path)
    sorted_list = sorted_list_of_dictionaries(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}") 
    print("============= END ===============")

if __name__ == "__main__":
    main()