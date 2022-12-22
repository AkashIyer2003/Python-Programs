import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from gensim.models import Word2Vec
import numpy as np
import re

def lemmatize_words(words): # used
    lemmatized_words = []
    for word in words:
        tempList = []
        for word2 in word:
            tempList.append(wordlemmatizer.lemmatize(word2))
        lemmatized_words.append(tempList)
    return lemmatized_words

def uniqueWord(w): # used 
    w2=[]
    for word in w:
        tempList=[]
        for word2 in word:
            if tempList.count(word2)<1:
                    tempList.append(word2)
        w2.append(tempList)
    return w2

def remove_special_characters(text): # used
    regex = r'[^a-zA-Z0-9\s]'
    text = re.sub(regex,'',text)
    return text

def removeStopWord(word_text):  # used
    filtered_sentence = [] 
    stop_words = set(stopwords.words('english'))   
    for w in word_text:
        tempList=[]
        for x in w:
            if x.lower() not in stop_words: 
                tempList.append(x)
        filtered_sentence.append(tempList)
    return filtered_sentence   
 
def meanOfWord(model, sentence): # used
#     posValue=nltk.pos_tag(sentence)
    posList=['CD']
    nounList=['NN','NNP','NNS','NNPS']
    value=[]
    count=0
    noun=0
    for word in sentence:
        a=model.similar_by_word(word)
        temp=[]
        for w in a:
          temp.append(w[1])
        posValue=nltk.pos_tag([word])
#         print(posValue)
        wordScore=np.mean(temp)
        if posValue[0][1] in posList:
            count=count+1
        else:
            valueIfNum=checkNum(word)
            count=count+valueIfNum
        if posValue[0][1] in nounList:
            noun=noun + .25
        value.append(wordScore)
    return np.mean(value)+count+noun

        
    
def checkNum(s):
    l= ['1','2','3','4','5','6','7','8','9','0']
    check =False

    for i in s:
        if i in l:
            check = True
            break
    if check == True:
        return 1
    else:
        return 0
 
Stopwords = set(stopwords.words('english'))

wordlemmatizer = WordNetLemmatizer()

text="China remains the main area of concern for BMW after sales there fell 16% last year. However, BMW is hopeful of a much better year in 2005 as its direct investment in China begins to pay dividends. The company only began assembling luxury high-powered sedans in China in 2003. 2004 was generally a good year for BMW, which saw revenues from its core car-making operations rise 11%."
sentences = sent_tokenize(text) # 1: sent tokenize
text_noSpecial_character = remove_special_characters(str(text)) 
word_text = [[text_noSpecial_character for text_noSpecial_character in 
sentences.split()] for sentences in sentences] # 3: word token
stop_text= removeStopWord(word_text) # 4: remove stop words
unique_text= uniqueWord(stop_text)   # 5: remove duplicate words
lemma_text = lemmatize_words(unique_text) # 6: lemmatization

model = Word2Vec(lemma_text, min_count=1,sg=1)

score=[]
for index, sentence in enumerate(lemma_text):
    i = lemma_text.index(sentence)
    meanScore= meanOfWord(model,sentence)
#         print(str(labels[index])+ ":"+ str(sentence)+ str(meanScore) )
    temp = [i,meanScore]
    score.append(temp)
#     print(meanOfWord(model,sentence))
print(score)

