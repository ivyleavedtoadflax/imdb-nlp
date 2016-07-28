# coding: utf-8
get_ipython().magic('save my_session1.py 1-50')
test
test.shape
num_reviews 
clean_test_reviews
clean_test_reviews = []
print "Cleaning and parsing the test set movie reviews...\n"
for i in xrange(0,num_reviews):
        if( (i+1) % 1000 == 0 ):
                print "Review %d of %d\n" % (i+1, num_reviews)
            clean_review = review_to_words( test["review"][i] )
            clean_test_reviews.append( clean_review )
        
for i in xrange(0,num_reviews):
        if( (i+1) % 1000 == 0 ):
                print( "Review %d of %d\n" % (i+1, num_reviews))
            clean_review = review_to_words( test["review"][i] )
            clean_test_reviews.append( clean_review )
        
for i in xrange(0,num_reviews):
        if( (i+1) % 1000 == 0 ):
                print( "Review %d of %d\n" % (i+1, num_reviews))
            clean_review = review_to_words( test["review"][i] )
            clean_test_reviews.append( clean_review )
        
get_ipython().magic('paste')
get_ipython().magic('paste')
for i in range(0,num_reviews):
        if( (i+1) % 1000 == 0 ):
                print( "Review %d of %d\n" % (i+1, num_reviews))
            clean_review = review_to_words( test["review"][i] )
            clean_test_reviews.append( clean_review )
        
get_ipython().magic('paste')
clean_test_reviews
get_ipython().magic('paste')
get_ipython().magic('paste')
get_ipython().magic('save my_session 50-67')
