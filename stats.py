def get_num_words(string):
    return len(string.split())


def count_chars(string):
    counts = {}
    for ch in string.lower():
        if ch not in counts.keys():
            counts[ch] = 0
        counts[ch] += 1
    return counts
