# import sys

# from stats import (
#     get_num_words,
#     chars_dict_to_sorted_list,
#     get_chars_dict,
# )

# # def count_words(text):
# #     number_of_words = text.split()
# #     return len(number_of_words)
# def main():
#     """Relative path to my Frankenstein text"""
#     # book_text = get_book_text("books/frankenstein.txt")
#     if len(sys.argv) < 2:
#         print("Usage: python3 main.py <path_to_book>")
#         sys.exit(1)
#     book_path = sys.argv[1]
#     # filename = sys.argv[1]
#     # try:
#     #     with open(filename, 'r') as f:
#     #         book_text = f.read()
#     # except FileNotFoundError:
#     #     print(f"File {filename} not found.")
#     #     sys.argv(1)
#     # word_count = get_num_words(book_text)
#     # character_dictionary = count_character_string(book_text)
#     # sorted_chars = sort_char_counts(character_dictionary)
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = count_character_string(text)
#     char_sorted_list = sort_char_counts(chars_dict)
#     print_report(book_path, num_words, chars_dict, char_sorted_list)

# def print_report(book_path, num_words, chars_sorted_list):
#     print("============ BOOKBOT ============")
#     print(f"Analyzing book found at {book_path}...")
#     print("----------- Word Count ----------")
#     print(f"Found {num_words} total words")
#     print("--------- Character Count -------")
#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"{item['char']}: {item['num']}")

#     print("============= END ===============")


# def get_book_text(file_path):
#     with open(file_path) as f:
#         return f.read()


# main()

# sys.exit(1)
# """
# # better
# def print_report(book_path, num_words, chars_sorted_list):
#     print("============ BOOKBOT ============")
#     print(f"Analyzing book found at {book_path}...")
#     print("----------- Word Count ----------")
#     print(f"Found {num_words} total words")
#     print("--------- Character Count -------")
#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"{item['char']}: {item['num']}")
# """
import sys
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()