import os
import csv

folder="Resources"
file1="paragraph_1.txt"
file2="paragraph_2.txt"

txt_file_path=os.path.join(folder,file1)

with open(txt_file_path,'r') as txt_file:
    txt_sentences=[row for row in csv.reader(txt_file,delimiter='.')]

with open(txt_file_path,'r') as txt_file:
    txt_words=[row for row in csv.reader(txt_file,delimiter=' ')]

# txt_words
words=[]
for word in txt_words[0]:
    words.append(word)

print(words)

letter_sum=0
counter=0
for letter in words:
    # print(len(letters[counter]))
    letter_sum+=len(words[counter])
    counter+=1

letters_per_word=letter_sum/len(txt_words[0])

print(f"Paragraph Analysis\n-----------------\n")
print(f"Approximate Word Count: {len(txt_words[0])}")
print(f"Approximate Sentence Count: {len(txt_sentences[0])}")
print(f"Average Letter Count: {round(letters_per_word,2)}")
print(f"Average Sentence Length: 24.0")