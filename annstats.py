import csv
from collections import defaultdict

all_values = []
letter_freqs = defaultdict(int)
length_freqs = defaultdict(int)

with open("annotations500.csv", 'rb') as annfile:
    annreader = csv.reader(annfile, delimiter=",")
    # skip the header
    annreader.next()

    for row in annreader:
        index, letters = row

        if int(index) < 500:
            all_values += letters

            captcha_len = len(letters)
            length_freqs[captcha_len] += 1

            for letter in letters:
                letter_freqs[letter] += 1
        else:
            break


print(letter_freqs)
print(sorted(letter_freqs.keys()))

print(length_freqs)        
