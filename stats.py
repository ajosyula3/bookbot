def num_words_in_string(file_contents) -> int:
    num_array = file_contents.split()
    return len(num_array)

def num_of_characters(file_contents) -> list:
    char_count = {}

    file_contents = file_contents.lower()

    for char in file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_list(char_count) -> list:
    char_list = []

    #convert dictionary into a list of dictionaries to sort on
    for char, count in char_count.items():
        char_list.append({
            "char": char,
            "num": count
        })
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(items):
    return items["num"]
