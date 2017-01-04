happy = input("Enter a text string to word count: ")

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print("The word frequency of your text string is: ")
print(counts)
