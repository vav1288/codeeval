import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        N_str, data = test.split(';')
        N = int(N_str)
        numbers = [int(x) for x in data.split()]
        
        if len(numbers) < N:
            print(0)
            continue
        
        current_sum = sum(numbers[:N])
        best_sum = max(0, current_sum)

        for i in range(N, len(numbers)):
            current_sum += numbers[i] - numbers[i-N]
            if current_sum > best_sum:
                best_sum = current_sum
                
        print(best_sum)
        
