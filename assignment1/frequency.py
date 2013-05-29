import sys, json

def main():
   tweet_file = open(sys.argv[1])
   
   occurrences = {}
   tot_occurrences = 0
   for line in tweet_file:
      tweet = json.loads(line).get('text','')
      tweet = map(lambda x:x.lower(), tweet.split())
      for word in tweet:
         occurrences[word] = occurrences.get(word,0) + 1 
         tot_occurrences += 1

   for i in occurrences:
      print i, float(occurrences[i])/tot_occurrences


if __name__ == '__main__':
   main()
