def get_num_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return len(file.read().split())

def get_num_chars(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        work_string = file.read().lower()
    char_count = {}
    for char in work_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sorted_list_of_dictionaries(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
        else:
            pass
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list