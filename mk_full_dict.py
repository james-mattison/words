import json

with open("dict.json") as _o:
    js = json.load(_o)


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

d = {}

i = 0
for item in js:
    if list(item.keys())[0].upper()[:1]in alpha:
        alpha.replace(list(item.keys())[0].upper()[:1], "")
    for char in alpha:
        d[alpha[i]] = item
    i += 1

print(len(d.keys()))

total_words = 0

for i, (key, val) in enumerate(d.items()):
    file = "dictionaries/{}.json".format(key)
    with open(file, "w") as _o:
        json.dump(val, _o, indent = 4)
        print(key, end = "", flush = True)

print("Checking first word words...")
for char in alpha:
    with open("dictionaries/" + char + ".json", "r") as _o:
        p = json.load(_o)
        keys = list(p.keys())
        print(f"| {char} {len(keys)} VALID")
        total_words += len(keys)

print(f"Processed a total of {total_words} words.")
