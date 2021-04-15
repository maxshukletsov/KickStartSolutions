T = int(input())
def a():
    N, K = map(int, input().split())
    S = str(input())
    score = 0
    for i in range(N//2):
            score+= int(S[i] != S[-1-i])
    return(score-K)
    
for case in range(0, T):
    print(f'Case #{case}: {abs(a())}')
