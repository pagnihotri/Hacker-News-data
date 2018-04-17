import read
import collections
from dateutil.parser import parse 

df=read.load_data()
time_string=""
empty_string=" "
hour_val=""
for index, row in df.iterrows():
    time_string=parse(str(row["submission_time"]))
    hour_val=hour_val+str(time_string.hour)+empty_string
    
words = hour_val.split(" ")
hundred_hour=collections.Counter(words).most_common(100)
print(hundred_hour)