import sys
from stats import count_words, count_characters, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    # Check if we have exactly one argument (plus script name)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from command-line argument
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_counts = count_characters(book_text)
    sorted_chars = sort_char_counts(char_counts)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
