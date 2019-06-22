import os
import nltk
import string
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def Concatenation(folder, name):
    with open(name, 'w') as outfile:
        for file in os.listdir(folder):
            with open(folder+file) as infile:
                for line in infile:
                    if line.strip():
                        outfile.write(line)

def Trim(text, text_trimmed):
    with open(text, 'r') as infile:
        lines = infile.readlines()
        with open(text_trimmed, 'w') as outfile:
            for line in lines:
                outfile.write(line.translate(str.maketrans('', '', string.punctuation))
                              .translate(str.maketrans('', '', '0123456789')))

def Tokenize_texts(text):
    output = []
    with open(text, 'r') as infile:
        lines = infile.readlines()
    for line in lines:
        line_list = nltk.word_tokenize(line)
        for word in line_list:
            output.append(word)
    return output

def Lemmatize_texts(list):
    output = []
    for word in list:
        output.append(lemmatizer.lemmatize(word))
    return output

def Remove_names(list):
    output = []
    tag_list = nltk.pos_tag(list)
    for word in tag_list:
        if word[1] != 'NNP':
            output.append(word[0])
    return output

def Extract_frequent(list):
    output = []
    freq = nltk.FreqDist(list)
    for word in freq.most_common(50):
        output.append(word)
    return output


Concatenation("english/", "English.txt")
Concatenation("spanish/", "Spanish.txt")
Concatenation("swedish/", "Swedish.txt")

Trim("English.txt", "English_trimmed.txt")
Trim("Spanish.txt", "Spanish_trimmed.txt")
Trim("Swedish.txt", "Swedish_trimmed.txt")

english_contents = Lemmatize_texts(Tokenize_texts("English_trimmed.txt"))
spanish_contents = Lemmatize_texts(Tokenize_texts("Spanish_trimmed.txt"))
swedish_contents = Lemmatize_texts(Tokenize_texts("Swedish_trimmed.txt"))

english_contents = Remove_names(english_contents)
spanish_contents = Remove_names(spanish_contents)
swedish_contents = Remove_names(swedish_contents)

english_frequent = Extract_frequent(english_contents)
spanish_frequent = Extract_frequent(spanish_contents)
swedish_frequent = Extract_frequent(swedish_contents)

print(english_frequent)
print(spanish_frequent)
print(swedish_frequent)
