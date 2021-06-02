import json
from collections import Counter

with open('nouns.json','r') as f:
    nouns = json.load(f)


counts = Counter(nouns)

print(counts.most_common(20))




