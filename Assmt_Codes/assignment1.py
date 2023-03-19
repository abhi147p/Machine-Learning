
def read_corpus(corpus_file):
    out = []
    with open(corpus_file) as f:
        for line in f:
            tokens = line.strip().split()
            out.append( (tokens[1], tokens[3:]) )
    return out

all_docs = read_corpus('all_sentiment_shuffled.txt')
split_point = int(0.8*len(all_docs))
train_docs = all_docs[:split_point]
eval_docs = all_docs[split_point:]
