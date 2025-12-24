from stats import num_words_in_string, num_of_characters, sort_list
import sys

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    sys_filepath = sys.argv
    
    if len(sys_filepath) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys_filepath[1])
    num_words = num_words_in_string(file_contents)
    char_list = num_of_characters(file_contents)
    sorted_char_count = sort_list(char_list)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
