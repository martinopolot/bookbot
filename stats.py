def get_num_words(text):
    words = text.split()
    return len(words)

# Count Characters
"""
- define a function taking in one param (text)
- create an empty dictionary or list to map character counts
- loop thru the text - for each character, update the count in the dictionary
"""
"""def count_character_string(text):
    text = text.lower()
    lowered_chars = set(text) # to remove duplicates
    character_count = {}

    for char in lowered_chars:
        character_count[char] = text.count(char)
    return character_count"""


# def count_character_string(text):
#     char_counts = {}
#     for char in text.lower():
#         if char.isalpha():  # only count alphabet letters
#             char_counts[char] = char_counts.get(char, 0) + 1
#     return char_counts

# def get_num_words(text):
#     words = text.split()
#     return len(words)


"""def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
"""

# def sort_char_counts(char_counts):
#     char_list = [{'char': char, 'count': count} for char, count in char_counts.items()]
#     char_list.sort(key=lambda x: x['count'], reverse=True)
#     return char_list


"""
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
"""
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list