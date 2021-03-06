___author__ = 'Ahmed Hani Ibrahim'
from rna import RNA


class DNA(object):
    def __init__(self, dna_string=""):
        self.__dna_string = dna_string
        self.__codon_table = {}

    def set_codon_table(self, codon_table):
        self.__codon_table = codon_table

    def get_codon_table(self):
        return self.__codon_table

    def set_dna_string(self, dna_string):
        self.__dna_string = dna_string

    def get_dna_string(self):
        return self.__dna_string

    def get_dna_to_amino_acid_candidates(self, amino_acid):
        substring_length = len(amino_acid) * 3
        rna = RNA()
        rna.set_codons_table(self.__codon_table)
        candidates = []
        for i in range(0, len(self.__dna_string)):
            if i + substring_length > len(self.__dna_string):
                break

            candidate_substring = self.__dna_string[i:(i + substring_length)]
            rna_string = self.__dna_to_rna_string(candidate_substring)
            rna.set_rna_string(rna_string)
            current_amino_acid = rna.to_amino_acid()

            if current_amino_acid == amino_acid:
                candidates.append(candidate_substring)
            else:
                reversed_dna = self.__reverse_dna(candidate_substring)
                reversed_rna = self.__dna_to_rna_string(reversed_dna)
                rna.set_rna_string(reversed_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

                complement_dna = self.__complement_dna(candidate_substring)
                complement_rna = self.__dna_to_rna_string(complement_dna)
                rna.set_rna_string(complement_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

                reversed_complement_dna = self.__complement_dna(self.__reverse_dna(candidate_substring))
                reversed_complement_rna = self.__dna_to_rna_string(reversed_complement_dna)
                rna.set_rna_string(reversed_complement_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

                complement_reversed_dna = self.__reverse_dna(self.__complement_dna(candidate_substring))
                complement_reversed_rna = self.__dna_to_rna_string(complement_reversed_dna)
                rna.set_rna_string(complement_reversed_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

        return candidates

    def to_rna_string(self):
        return self.__dna_to_rna_string(self.__dna_string)

    def reverse_dna(self):
        return self.__reverse_dna(self.__dna_string)

    def complement_dna(self):
        return self.__complement_dna(self.__dna_string)

    @staticmethod
    def __reverse_dna(dna_string):
        return dna_string[::-1]

    @staticmethod
    def __complement_dna(dna_string):
        reversed_dna = ""

        for i in range(0, len(dna_string)):
            if dna_string[i] == 'A':
                reversed_dna += 'T'
            elif dna_string[i] == 'G':
                reversed_dna += 'C'
            elif dna_string[i] == 'T':
                reversed_dna += 'A'
            elif dna_string[i] == 'C':
                reversed_dna += 'G'
            elif dna_string[i] == 'G':
                reversed_dna += 'C'

        return reversed_dna

    @staticmethod
    def __dna_to_rna_string(dna_string):
        return dna_string.replace('T', 'U')