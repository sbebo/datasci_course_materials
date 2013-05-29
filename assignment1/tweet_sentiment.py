import sys,json

def main():
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   scores = {} # initialize an empty dictionary
   for line in sent_file:
      term, score  = line.split("\t")
      scores[term] = int(score)
   
   for line in tweet_file:
      tweet = json.loads(line).get('text','')
      sentiment = 0.
      for word in tweet.split():
         sentiment += scores.get(word.lower(),0)
      print sentiment


if __name__ == '__main__':
   main()
