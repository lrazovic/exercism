def to_rna(dna_strand):
    rna = ""
    conversion = {"G": "C", "C": "G", "T": "A", "A": "U"}
    for nucleotide in dna_strand:
        rna += conversion[nucleotide]
    return rna
