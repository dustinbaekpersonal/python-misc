import pdb

s = "ohvhjdml"

l, max_len = 0, 0
res = ""

for i, sub in enumerate(s):
    while sub in res:
        l += 1
        res = res[l:]
        l=0
        print('in while loop')
    res += sub
    max_len = max(max_len, len(res))
    print(i, sub, res, end="\n\n")


