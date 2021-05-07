import os
import csv
import re

folder="Resources"
file1="paragraph_1.txt"
file2="paragraph_2.txt"

txt_file_path=os.path.join(folder,file1)

# with open(txt_file_path,'r') as txt_file:
#     txt_sentances=[row for row in csv.reader(txt_file,delimiter='.')]

# sentances=[]
# for sentance in txt_sentances[0]:
#     sentances.append(sentance)

# print(sentances[1])

# word_sum=0
# counter=0
# for word in sentances:
#     # print(len(letters[counter]))
#     word_sum+=len(sentances[counter])
#     print(word_sum)
#     counter+=1

# words_per_sentence=word_sum/len(txt_sentances[0])

# with open(txt_file_path,'r') as txt_file:
#     txt_words=[row for row in csv.reader(txt_file,delimiter=' ')]

# # txt_words
# words=[]
# for word in txt_words[0]:
#     words.append(word)

# # print(words)

# letter_sum=0
# counter=0
# for letter in words:
#     # print(len(letters[counter]))
#     letter_sum+=len(words[counter])
#     counter+=1

# letters_per_word=letter_sum/len(txt_words[0])
nmb_words=[]


with open(txt_file_path,'r') as txt_file:
    par=txt_file.read()
    sentences=par.split(".")
    print(f"{len(sentences)}\n")
    for sent in sentences:
        words=sent.split(" ")
        print(f"{len(words)}")
        nmb_words.append(len(words))
        # print(nmb_words)
avg_nmb_words=sum(nmb_words)/len(nmb_words)
print(avg_nmb_words)
# print(f"Paragraph Analysis\n-----------------\n")
# print(f"Approximate Word Count: {len(txt_words[0])}")
# print(f"Approximate Sentence Count: {len(txt_sentances[0])}")
# print(f"Average Letter Count: {round(letters_per_word,2)}")
# print(f"Average Sentence Length: {words_per_sentence}")