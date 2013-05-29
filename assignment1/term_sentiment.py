import sys, json

def main():
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])
   
   scores = {}
   for line in sent_file:
      term, score  = line.split("\t")
      scores[term] = int(score)
   
   learned_scores = {}
   for line in tweet_file:
      tweet = json.loads(line).get('text','')
      tweet = map(lambda x:x.lower(), tweet.split())
      sentiment = 0.
      for word in tweet:
         sentiment += scores.get(word,0)
      for word in tweet:
         learned_scores[word] = learned_scores.get(word,0) + sentiment

   for i in learned_scores:
      print i, learned_scores[i]



if __name__ == '__main__':
   main()
