s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
y = 2 in s
z = 3 in s
stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list
stopwords_set = set(stopwords_list)
"zip" in stopwords_set
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)
