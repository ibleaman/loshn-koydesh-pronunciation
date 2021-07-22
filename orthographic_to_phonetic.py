# input file
phonetic_list = 'phonetic-to-orthographic.txt'

# output_file
orthographic_list = 'orthographic-to-phonetic.txt'


import csv

with open(phonetic_list, 'r') as file:
    data = file.read()

phonetic_forms = data.split('\n')

orthographic_forms = dict()

for entry in phonetic_forms:
    phon = entry.split('\t')[0]
    orth = entry.split('\t')[1]

    if orth not in orthographic_forms:
        orthographic_forms[orth] = []

    orthographic_forms[orth].append(phon)

with open(orthographic_list, 'w') as text_file:
    for orth, phon in sorted(orthographic_forms.items()):
        text_file.write(orth + '\t' + ','.join(phon) + '\n')
