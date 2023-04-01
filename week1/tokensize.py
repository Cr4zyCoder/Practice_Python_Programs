# problem statement : The goal is to tokensize the following 5 sentences into words, excluding the stop words
# input: 
# sentemces:["a new world record was set", "in the holy city of ayodha",
#            "on the eve of diwali on tuesday",
#            "with over three lakh diya or earthen lamps"
#            "lit up simultaneously on the banks of the sarayu river"]

# stopwords=['for', 'a', 'of', 'the','and','to' ,'in', 'on ' ,'was' ]

sentences = ["a new world record was set", "in the holy city of ayodha",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]


stop_words = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'was']


def tokenize(sentence):
    words = sentence.lower().split()
    words = [word for word in words if word not in stop_words]
    return words


tokenized_sentences = []
for sentence in sentences:
    words = tokenize(sentence)
    tokenized_sentences.append(words)


for sentence in tokenized_sentences:
    print(sentence)
