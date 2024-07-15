words = ['apple','banana','banana','apple','watermelon','melon']
print(word_freq)
word_freq = [words.count(w) for w in words]
frequencies=set(zip(words, word_freq))
print(frequencies)
# words_count=Counter(words)
# print(words_count)
print(set(words))