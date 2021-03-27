import collections

file = open('txt_dump.txt', encoding="utf8")

a = file.read()

stopwords = set(line.strip() for line in open('txt_blacklist.txt'))
stopwords = stopwords.union(
    set(['mr', 'mrs', 'one', 'two', 'said', 'the', 'a', 'and', 'to', 'of']))

wordcount = {}

for word in a.lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("*", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

num_print = int(input("Number of words to find: "))

print("\nAnalysis Complete.\n\nThe {} most common words found:\n".format(num_print))

word_counter = collections.Counter(wordcount)

for word, count in word_counter.most_common(num_print):
    print(word.upper(), "-", count)


file.close()
