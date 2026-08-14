def dna_to_rna(dna):
    res = ""
    for letter in dna:
        if letter  == 'T':
            res += 'U'
        else:
            res += letter
    return res