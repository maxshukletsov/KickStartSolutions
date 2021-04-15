def solve():
    N, B = map(int, input().split())
    A = [int(i) for i in input().split()]
    house = 0
    score = 0
    for i in range(N):
        house += min(A)
        if house <= B:
            score+=1
        else:
            break
        A.remove(min(A))
    return(score)

T = int(input())
for case in range(0, T):
    print(f'Case #{case+1}: {solve()}')
