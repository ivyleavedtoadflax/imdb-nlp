# coding: utf-8
get_ipython().magic('run my_session.py')
get_ipython().magic('run my_session.py')
clean_train_reviews = []
for i in range(0, num_reviews):
    if ((i+1)%1000 = 0):
        print("Review %d of %d\n" % (i+1, num_reviews) )
    clean_train_reviews.append(review_to_words( train['review'][i] ))
    
for i in range(0, num_reviews):
    if ((i+1)%1000 == 0):
        print("Review %d of %d\n" % (i+1, num_reviews) )
    clean_train_reviews.append(review_to_words( train['review'][i] ))
    
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(analyzer="word", \)
vectorizer = CountVectorizer(analyzer="word",
tokenizer = None,
preprocessor = None,
stop_words = None,
max_features = 5000)
train_data_features = vectorizer.fit_transform(clean_train_reviews)
train_data_features
train_data_features = train_data_features.toarray()
train_data_features
train_data_features.shape
vocab = vectorizer.get_feature_names()
vocab
import numpy as np
dist = np.sum(train_data_features, axis=0)
for tag, count in zip(vocab, dist):
    print(count, tag)
    
# Training a Random Forest
from sklearn.ensemble import RandomForestClassifier
# Initialise random forest with 100 trees
forest = RandomForestClassifier(n_estimators = 100)
forest
forest = forest.fit(train_data_features, train['sentiment'])
# Create a submission
test = pd.read_csv('data/testData.tsv'
header = 0,
delimiter = '\t',
quoting = 3)
test = pd.read_csv('data/testData.tsv',
header = 0,
delimiter = '\t',
quoting = 3)
test.shape
for i in range(0, num_reviews):
    if( (i+1) % 1000 == 0):
        print('Review %d of %d\n' % (i+1, num_reviews))
        
clean_review = review_to_words(test['review'][i])
clean_review
clean_test_reviews.append(clean_review)
clean_review
clean_test_reviews = []
clean_test_reviews.append(clean_review)
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()
test_data_features
result = forest.predict(test_data_features)
result
output = pd.DataFrame(data={'id':test['id'], 'sentiment':result})
output
result
test_data_features
result
result = forest.predict(test_data_features)
result
get_ipython().magic('history')
get_ipython().magic('save my_session1.py')
get_ipython().magic('save my_session1.py 1-50')
