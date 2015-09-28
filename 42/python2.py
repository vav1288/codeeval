import sys
from collections import Counter

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        N = len(test.strip())

        results = [Counter() for i in range(N)]
        for i in reversed(range(N)):
            dI = results[i]
            dI[int(test[i:])] +=1
            for j in range(i+1, N):
                dJ = results[j]
                ddI = int(test[i:j])
                for k in dJ:
                    dI[ddI+k] += dJ[k]
                    dI[ddI-k] += dJ[k]

        res = 0
        for k in results[0]:
            if k % 2 == 0 or k % 3 == 0 or k % 5 == 0 or k % 7 == 0:
                res += results[0][k] 
        print res
