import read
import collections
df=read.load_data()
final_string=""
for index, row in df.iterrows():
    final_string+=str(row["headline"])
    
final_string=final_string.lower()
words = final_string.split(" ")
hundred_words=collections.Counter(words).most_common(100)
print(hundred_words)