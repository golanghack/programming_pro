#! /usr/bin/env python3
"""
This program is designed to automatically filter messages.

The spam/non-spam switch is done automatically by the script.
Script trained on data
https://www.kaggle.com/uciml/sms-spam-collection-dataset
"""

import pandas as pd 
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
import warnings
import re 
warnings.filterwarnings('ignore')
nltk.download('stopwords')
nltk.download('wordnet')

# reading data
message = pd.read_csv('spam.csv', encoding='latin-1')
message.drop(['Unnamed: 0'], axis=1, inplace=True)

# separating target and features 
y = pd.DataFrame(message.label)
x = message.drop(['label'], axis=1)

# countvectorization
count_vectors = CountVectorizer(max_features=5000)
temp_1 = count_vectors.fit_transform(x['final_text'].values.astype('U')).toarray()
transformer = TfidfTransformer()

temp_1 = transformer.fit_transform(temp_1)
temp_1 = pd.DataFrame(temp_1.toarray(), index=x.index)
x = pd.concat([x, temp_1], axis=1, sort=False)

# drop final_text 
x.drop(['final_text'], axis=1, inplace=True)

# converting to int datatype 
y = y.astype(int)

# random forest
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(x, y)

# users 
message_for_user = 'Enter text, please -> '
text = input(message_for_user)

# data cleaning/preprocessing/removing (remove punctuation and digits)
updated_text = ''
for i in range(len(text)):
    if text[i] not in string.punctuation:
        if text[i].isdigit == False:
            updated_text = updated_text + text[i]
            
text = updated_text

# data cleaning/preprocessing/tokenazing (convert to lowercase and tokenaizing)
text = re.split('\W+', text.lower())

# data cleanin/preprocessing (stopwords)
updated_list = []
stopwords = nltk.corpus.stopwords.words('english')
for i in range(len(text)):
    if text[i] not in stopwords:
        updated_list.append(text[i])
text = updated_list

# data cleaning/preprocessing (lemmentizing)
updated_list = []
wordlem = nltk.WordNetLemmatizer()
for i in range(len(text)):
    updated_list.append(wordlem.lemmatize(text[i]))
text = updated_list

# data cleaning/preprocessing (mergining token)
text = ''.join(text) 
text = count_vectors.transform([text])
text = tf.transform(text)
pred = model.predict(text)

if pred == 0:
    print('In message don`t have a spam.')
else:
    print('In message have a spam!')