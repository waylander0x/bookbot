def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    def sort_on(item):
        return item["num"]
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
