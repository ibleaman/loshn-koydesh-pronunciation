# input file
phonetic_list = 'phonetic-to-orthographic.txt'

# output_file
orthographic_list = 'orthographic-to-phonetic.txt'

import csv
import re

with open(phonetic_list, 'r') as file:
    data = file.read()

phonetic_forms = data.split('\n')

orthographic_forms = dict()

# FOR ALPHABETIZATION
# map digraphs to precombined characters, only for those relevant to alphabetization
precombined = {
    ('בֿ','בֿ'),
    ('כּ','כּ'),
    ('פּ','פּ'),
    ('פֿ','פֿ'),
    ('שׂ','שׂ'),
    ('תּ','תּ'),
}
diacritics_to_remove = 'ִַָּ' + '…׳״'
alphabetically_equivalent = {
    ('ך', 'כ'),
    ('ם', 'מ'),
    ('ן', 'נ'),
    ('ף', 'פֿ'),
    ('ץ', 'צ'),
    ('ײ', 'יי'),
}
# new alphabetical order; based on Niborski (1999:xiii)
alphabet = ' ־אבבֿגדהוזחטיכּכלמנסעפּפֿצקרששׂתּת'

for entry in phonetic_forms:
    phon = entry.split('\t')[0]
    orth = entry.split('\t')[1]

    alph = orth # a simplified representation used for alphabetization
    for pair in precombined:
        alph = re.sub(pair[0], pair[1], alph)
    for character in diacritics_to_remove:
        alph = re.sub(character, '', alph)
    for pair in alphabetically_equivalent:
        alph = re.sub(pair[0], pair[1], alph)

    if alph not in orthographic_forms:
        orthographic_forms[alph] = {orth: [phon]}
    else:
        if orth not in orthographic_forms[alph]:
            orthographic_forms[alph][orth] = [phon]
        else:
            orthographic_forms[alph][orth].append(phon)

with open(orthographic_list, 'w') as text_file:
    for alph in sorted(orthographic_forms.keys(), key=lambda word: [alphabet.index(c) for c in word]):
        for orth in orthographic_forms[alph]:
            text_file.write(orth + '\t' + ','.join(orthographic_forms[alph][orth]) + '\n')
