def remove_boxes(boxes):
    def dp(l, r, k):
        if l > r:
            return 0
        if memo[l][r][k] != 0:
            return memo[l][r][k]
        
        
        while l < r and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1
        
        memo[l][r][k] = dp(l, r - 1, 0) + (k + 1) * (k + 1)
        
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                memo[l][r][k] = max(memo[l][r][k], dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
        
        return memo[l][r][k]

    n = len(boxes)
    memo = [[[0] * n for _ in range(n)] for _ in range(n)]
    return dp(0, n - 1, 0)

print(remove_boxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))  
print(remove_boxes([1, 1, 1]))  
print(remove_boxes([1]))  
