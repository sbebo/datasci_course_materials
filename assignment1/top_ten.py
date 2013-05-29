import sys, json

def main():
   tweet_file = open(sys.argv[1])
   
   occurrences = {}
   for line in tweet_file:
      tweet = json.loads(line)
      if 'entities' not in tweet:
         continue
      hashtags = tweet['entities']['hashtags']
      for tag in hashtags:
         occurrences[tag['text']] = occurrences.get(tag['text'],0) + 1 

   sorted_hashtags = sorted((v,k) for k,v in occurrences.items())[-10:]
   for x,y in sorted_hashtags:
      print y,float(x)


if __name__ == '__main__':
   main()
