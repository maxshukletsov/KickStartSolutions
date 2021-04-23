def solve():
    N = int(input())
    S = input()
    score = 1
    text = '1 '
    for i in range(1, N):
    	if ord(S[i]) > ord(S[i-1]):
    		score +=1
    	else:
    		score = 1
    	text += f'{score} '
    return text

T = int(input())
for case in range(0, T):
    print(f'Case #{case+1}: {solve()}')