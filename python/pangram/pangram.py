def is_pangram(sentence):
    words = set([t for t in sentence.lower() if t.isalpha()])
    return len(words) == 26
