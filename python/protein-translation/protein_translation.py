from itertools import takewhile


def proteins(strand: str):
    conversion = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UCU": "Serine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
    splitted_proteins = [strand[i : i + 3] for i in range(0, len(strand), 3)]
    splitted_proteins = list(
        takewhile(lambda x: x not in ["UAA", "UAG", "UGA"], splitted_proteins)
    )
    return [conversion[protein] for protein in splitted_proteins]
