import read
import collections

df=read.load_data()
domain_string=""
empty_string=" "
for index, row in df.iterrows():
    domain_string=domain_string+str(row["url"])+empty_string
    
words = domain_string.split(" ")
new_words=[]
## Remove nan
for value in words:
    if value=='nan':
        pass
    else:
        new_words.append(value)
        
hundred_domains=collections.Counter(new_words).most_common(100)
print(hundred_domains)