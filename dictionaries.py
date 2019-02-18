empty_dict = {}
empty_dict2 = dict()
grades = { "Joel" : 80, "Tim" : 95 }
joels_grade = grades["Joel"]
try:
kates_grade = grades["Kate"]
except KeyError:
print "no grade for Kate!"
joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades
joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
tweet_keys= tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items() 
"user" in tweet_keys
"user" in tweet
word_counts = {}
for word in document:
if word in word_counts:
word_counts[word] += 1
else:
word_counts[word] = 1

word_counts = {}
for word in document:
try:
word_counts[word] += 1
except KeyError:
word_counts[word] = 1

word_counts = {}
for word in document:
previous_count = word_counts.get(word, 0)
word_counts[word] = previous_count + 1

from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict["Joel"]["City"] = "Seattle" 

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1

from collections import Counter
c = Counter([0, 1, 2, 0])
# c is (basically) { 0 : 2, 1 : 1, 2 : 1 }

word_counts = Counter(document)

for word, count in word_counts.most_common(10):

print word, count