import spacy

# Load the English language NLP
nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# 0.5929930274321619
# 0.40415016164997786
# 0.22358825939615987

"""
Cat and monkey are seen as the most similar, perhaps because they are animals.
The least similar is cat and banana because there isn't much to associate these.
Monkey and banana are seen as quite similar, probably because of the strong link
between a monkey and a banana.
"""

my_word1 = nlp("bread")
my_word2 = nlp("croissant")
my_word3 = nlp("baguette")

print(my_word1.similarity(my_word2))
print(my_word3.similarity(my_word2))
print(my_word3.similarity(my_word1))

# 0.7087429927486574
# 0.6772026679102146
# 0.6930636548279367

"""
I can see that the 3 words I chose are very strongly associated. 
Interestingly, bread and croissant are seen as more similar than bread and baguette.
"""

"""
example.py

Based on the average for each language model, I could see that en_core_web_sm was more likely to return a 
lower comparison result than en_core_web_md.

en_core_web_sm averages
complaints - 0.6829986399013144
recipes - 0.7451423521751951
complaints/ recipes - 0.4651991179626623

en_core_web_md averages
complaints - 0.8832437180248721
recipes - 0.9109821526692501
complaints/ recipes - 0.6749797394534064
"""