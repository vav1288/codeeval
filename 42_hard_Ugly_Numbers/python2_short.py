import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        N = len(test.strip())

        results = [{} for i in range(N)]
        for i in reversed(range(N)):
            dI = results[i]
            dI[int(test[i:])] = 1
            for j in range(i+1, N):
                dJ = results[j]
                ddI = int(test[i:j])
                for k in dJ:
                    for key in (ddI+k, ddI-k):
                        dI[key] = dI.get(key, 0) + dJ[k]

        print sum(dI[k] for k in dI if k%2==0 or k%3==0 or k%5==0 or k%7==0)
