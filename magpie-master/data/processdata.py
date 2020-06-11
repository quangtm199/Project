from pyvi import ViTokenizer, ViPosTagger # thư viện NLP tiếng Việt
from tqdm import tqdm
import numpy as np
import gensim # thư viện NLP
import io
import re, os, string
import pandas as pd
dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
dir_path = os.path.join(dir_path, 'data')
print(dir_path);
filename = './stopwords.csv'
data = pd.read_csv(filename, sep="\t", encoding='utf-8')

list_stopwords = data['stopwords']
def normalize_text(text):
    listpunctuation = string.punctuation.replace('_', '')
    for i in listpunctuation:
        text = text.replace(i, ' ')
    return text.lower()
def clean_text(text):
    text = re.sub('<.*?>', '', text).strip()
    text = re.sub('(\s)+', r'\1', text)
    return text

def remove_stopword(text):
    pre_text = []
    words = text.split()
    for word in words:
        if word not in list_stopwords:
            pre_text.append(word)
    text2 = ' '.join(pre_text)

    return text2

def get_data(folder_path):
    m = ""
    X = []
    y = []
    dirs = os.listdir(folder_path)

    for path in tqdm(dirs):

        if(path[-4:]==".txt"):
            try:
                 with open(os.path.join(folder_path, path), 'r', encoding="utf-8") as f:
                     lines = f.read()
                     lines = gensim.utils.simple_preprocess(lines)
                     lines = ' '.join(lines)
                     lines = ViTokenizer.tokenize(lines)
                     lines=clean_text(lines)
                     lines=remove_stopword(lines)

                     a=os.path.join(folder_path, path)

                     path1='C:/Users/Microsoft Windows/Desktop/Project2/magpie-master/magpie-master/data/hep-categories/'+path;
                     f1=open(path1, 'w+', encoding="utf-8")
                     f1.write(lines)
            except:
                ko=""
                ko=path[:-4]+".lab"
                os.remove(os.path.join(folder_path, path))
                os.remove(os.path.join(folder_path, ko))




        else:
            a=os.path.join(folder_path, path)

            with io.open(a,'r') as f:
                labels = f.read()
                m=m+str(labels)





    return X, y,m

train_path = os.path.join("C:/Users/Microsoft Windows/Desktop/Project2/magpie-master/magpie-master/data/hep-categories")
X_data, y_data ,m= get_data(train_path)
f=io.open(dir_path+'\hep-categories'+ '.labels', 'w')
f.write(m)
