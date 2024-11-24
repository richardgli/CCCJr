from collections import Counter

shelf = input()
c = Counter(shelf)
numL = c["L"]
numM = c["M"]
numS = c["S"]

cLM = Counter(shelf[:numL])
cMS = Counter(shelf[numL:numL + numM])

swaps = cLM["M"] + cLM["S"] + cMS["L"] + cMS["S"] - (min(cLM["M"], cMS["L"]))
print(swaps)
