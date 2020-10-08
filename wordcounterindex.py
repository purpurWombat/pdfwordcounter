import sys


from collections import Counter
def word_count(filename):
    with open(filename) as f:
        return Counter(f.read().split())

zeichenMitLeerzeichen = 0

counter = word_count('/Users/okanerkaptan/Downloads/WordcountTestText.rtf')
for i in counter:
    print(i, ':', counter[i])
    zeichenMitLeerzeichen = zeichenMitLeerzeichen +1 
print("Das ist die gesamte anzahl an Zeichen :", zeichenMitLeerzeichen) #stimmt doch nicht ist nicht das gesamte anzahl an Zeichen lel
#oder

user_str = input('Enter String')
l = user_str.split()
d = {}
for j in l:
    d[j] = d.get(j, 0)+1
print(d)