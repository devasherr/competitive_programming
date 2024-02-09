from collections import defaultdict

def isSubset( a1, a2, n, m):
    counta1 = defaultdict(int)
    counta2 = defaultdict(int)
    
    for i in range(n):
        counta1[a1[i]] = counta1[a1[i]] + 1
    for i in range(m):
        counta2[a2[i]] = counta2[a2[i]] + 1
    # a2 count must be lower than a1
    for key in counta2:
        if counta2[key] > counta1[key]:
            return "No"
    return "Yes"
