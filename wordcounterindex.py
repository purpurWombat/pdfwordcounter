'''import sys

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
print(d)'''
import re
from tkinter import *
from tkinter import filedialog as fd

root  = Tk()
pathDokument = fd.askopenfilename(parent=root, title='Wähle eine Datei')
anzworter = 0
#pathDokument = "test.pdf"

def getAnzWoerter(datei):
    woerter = 0
    for line in datei:
        #linie wird aus datei gelesen
        line = re.sub(r'[^a-zA-Z0-9 ]+', '', line)  #die linie iwird nach wörtern gesucht und als str gespeichert
        line = line.split()                          #der linestr wird geteil und als liste gespeichert
        counter = len(line)
        woerter += counter
    return woerter


try:
    f = open(pathDokument, 'r')
    anzworter = getAnzWoerter(f)
except UnicodeDecodeError:
    anzworter = 0
    try:
       f = open(pathDokument, 'r', encoding='latin-1')
       anzworter = getAnzWoerter(f)  
    except UnicodeDecodeError:
        anzworter = 0
        try:
            f = open(pathDokument, 'r', encoding='latin2')
            anzworter = getAnzWoerter(f)
        except:
            anzworter = 0
            try:
                f = open(pathDokument, 'r', encoding='utf-8')
                anzworter = getAnzWoerter(f)
            except UnicodeDecodeError:
                print("Dateiformat passt nicht")




print("Wörter:", anzworter)