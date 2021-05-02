import os
import csv

folder="Resources"
file1="paragraph_1.txt"
file2="paragraph_2.txt"

txt_file_path=os.path.join(folder,file1)

with open(txt_file_path,'r') as txt_file:
    txt_sentences=[row for row in csv.reader(txt_file,delimiter='.')]
print(f"{len(txt_sentences[0])}\t Sentences")

with open(txt_file_path,'r') as txt_file:
    txt_words=[row for row in csv.reader(txt_file,delimiter=' ')]
print(f"{len(txt_words[0])}\t Words")

for sentence in txt_sentences[0]:
    print(sentence)

for word in txt_words[0]:
    print(word)
    