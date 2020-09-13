def distance(strand_a, strand_b) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Invalid strand length")
    return sum(char_a != char_b for char_a, char_b in zip(strand_a, strand_b))
