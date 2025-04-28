K, M = map(int, input().split())
lists = []
for _ in range(K):
    parts = list(map(int, input().split()))
    n_i = parts[0]
    elements = parts[1:]
    squares = [(x * x) % M for x in elements]
    unique_squares = list(set(squares))  
    lists.append(unique_squares)


dp = [False] * M
for s in lists[0]:
    dp[s] = True

for i in range(1, K):
    temp_dp = [False] * M
    current_squares = lists[i]
    for r in range(M):
        if dp[r]:
            for s in current_squares:
                new_r = (r + s) % M
                temp_dp[new_r] = True
    dp = temp_dp

max_remainder = 0
for r in range(M):
    if dp[r]:
        max_remainder = max(max_remainder, r)

print(max_remainder)