def count_words(book):
    total_words = len(book.split())
    return f"Found {total_words} total words"

def count_char(book):
    
    counts = {}
    for letter in book.lower():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    return counts


def sort_on(items):
    return items["num"]

def sort_dict(counts):
    new_dict = []
    for count in counts:
        new_dict.append({"char": count, "num": (counts[count])})

    new_dict.sort(key=sort_on, reverse=True)

    return new_dict
