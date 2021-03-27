import collections

file = open('txt_dump.txt', encoding="utf8")  # File containing text to analyze

a = file.read()

# File containing any words to exclude from analysis i.e. mr, mrs.
stopwords = set(line.strip() for line in open('txt_blacklist.txt'))
stopwords = stopwords.union(
    set(['mr', 'mrs', 'one', 'two', 'said', 'the', 'a', 'and', 'to', 'of']))  # Hardcoded a few constants that I want to exclude always.

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

# How many keywords to search for in txt_dump.txt.
num_print = int(input("Number of words to find: "))

print("\nAnalysis Complete.\n\nThe {} most common words found:\n".format(num_print))

word_counter = collections.Counter(wordcount)

for word, count in word_counter.most_common(num_print):
    print(word.upper(), "-", count)


file.close()
