import sys,json

def main():
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])
   states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
   }
   scores = {} # initialize an empty dictionary
   for line in sent_file:
      term, score  = line.split("\t")
      scores[term] = int(score)

   happiness = {}
   for line in tweet_file:
      tweet = json.loads(line)
      if tweet.get('lang','') != 'en':
         continue
      
      text = tweet.get('text','')
      sentiment = 0.
      for word in text.split():
         sentiment += scores.get(word.lower(),0)

      place = tweet.get('place',None)
      user = tweet.get('user',None)
      if place is not None:
         location = place["full_name"]
      elif user is not None:
         location =  user.get("location","")
      else:
         continue

      if len(location) == 0:
         continue
      state = location.split()[-1].upper()
      if len(state) == 2 and state in states:
         happiness[state] = happiness.get(state,0) + sentiment
   
   print sorted([(v,k) for k,v in happiness.items()])[-1][1]


if __name__ == '__main__':
   main()
