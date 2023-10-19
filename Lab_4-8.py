dna_sequence = input('Enter a 6-letter DNA sequence (a, c, t, g): ').lower()
complementary_pairs = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
complementary_sequence = ''
for base in dna_sequence:
    complementary_sequence += complementary_pairs[base]
print('Complementary DNA sequence:', complementary_sequence)