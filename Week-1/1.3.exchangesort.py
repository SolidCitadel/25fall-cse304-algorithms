from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    for i in range(n - 1):
        for j in range(i + 1, n):
            if S[j] < S[i]:
                S[i], S[j] = S[j], S[i]