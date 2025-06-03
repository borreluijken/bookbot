import sys
from stats import get_num_words, count_chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main(path):
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    chars = count_chars(book_text)
    chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}...')
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")

    for key, value in chars.items():
        if key.isalpha():
            print(f'{key}: {value}')

    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
