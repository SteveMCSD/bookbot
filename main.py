import sys
from stats import get_word_count, char_count, get_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    contents = get_book_text(book)
    word_count = get_word_count(contents)
    char_list = char_count(contents)
    report = get_report(word_count, char_list, book)
    print(report)
    

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

main()
