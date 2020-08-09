import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
print("Start")

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    t=str.maketrans(".,:;'[]()*&^%$#@!~/?<>=-_",25*" ")
    file_contents=file_contents.translate(t)
    list_of_words=[]
    w=file_contents.split()
    for e in w:
        if e.isalpha():
            list_of_words.insert(0,e)
    freq={}
    for word in list_of_words:
        x=word.lower()
        if x not in uninteresting_words:
            if (word in freq):
                freq[word]+=1
            else:
                freq[word]=1  
    
    
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()

filename=input("Enter your filename:")

file = open(filename)

line = file.read().replace("\n", " ")
file.close()

file_contents=line
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
print ("Image uploaded successfuly")


