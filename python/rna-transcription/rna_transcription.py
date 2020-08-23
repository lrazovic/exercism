def to_rna(dna_strand: str):
    conversion = {"G": "C", "C": "G", "T": "A", "A": "U"}
    translation = dna_strand.maketrans(conversion)
    return dna_strand.translate(translation)
