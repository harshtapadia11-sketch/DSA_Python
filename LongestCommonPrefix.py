strs = ["plane","plate","prowne"]
prefix = strs[0]

for word in strs[1:]:

    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)