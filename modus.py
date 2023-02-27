from collections import Counter
data = [0, 2, 2, 1, 3, 2, 0]
no = len(data)
val = Counter(data)
nilaimodus = dict(val)
modus = [i for i, v in nilaimodus.items() if v == max(list(val.values()))]  
if len(modus) == no:
    nilaiModus = "tidak memiliki modus"
else:
    nilaimodus = "memiliki modus: " + ', '.join(map(str, modus))
print(nilaimodus)
