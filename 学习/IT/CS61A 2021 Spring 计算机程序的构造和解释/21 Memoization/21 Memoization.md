# 21 Memoization 记忆化

N\*\*3 N cube<br />
N\*\*2 N square

## Complexity
```python
for x in range(N):
    if L[x] < 0: # θ(N) 最坏情况
        c += 1   # θ(N) 最坏情况

for x in range(N):
    if L[x] < 0: # θ(N) 最坏情况
        c += 1   # θ(1) 最坏情况
        break

# f() => θ(N ** 3)  <- 2*N + 6*N**2 + 24*N**3 ×  
# θ不关心常数因子，只要高阶
for x in range(2*N):
    f(x, x, x)
    for y in range(3*N):
        f(x, y, y)
        for z in range(4*N):
            f(x, y, z)

# f() θ(N ** 2) => <- 0+1+2+...(N-1) = N(N-1)/2 ∈ θ(N ** 2)
for x in range(N):
    for y in range(x):
        f(x, y)

# f() θ(N)
# 比较 θ(N ** 2) <- N**2 + N - 1
z = 0
for x in range(N):
    for y in range(N):
        while z < N:
            f(x, y, z)
            z += 1
```

## 避免冗余计算
### Memorization, Dynamic Programming
```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# 迭代法  保存树中需要的信息避免重复计算(a, b => fib(n-2) fib(n-1))
def fib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for k in range(2, n+1):
        a, b = b, a+b
    return b

def count_change(amount, coins = (50, 25, 10, 5, 1)):
    if (amount == 0):
        return 1
    elif len(coins) == 0 or amount < 0:
        return 0
    else：
    return count_change(amount-coins[0], coins) + \
        count_change(amount, coins[1:])

# Memoizing
# memo table
def count_change(amount, coins = (50, 25, 10, 5, 1)):
    memo_table = {}
    # 优化memo_table，使用二维list。
    # memo_table = [ [-1] * (len(coins) + 1) for i in range(amount + 1) ]
    def count_change(amount, coins):
        key = (amount, coins)
        if key not in memo_table:
            memo_table[key] = full_count_change(amount, coins)
        return memo_table[key]
    
    def full_count_change(amount, coins):
        # 与原有代码一样。   
    return count_change(amount, coins)

# 此处还有一个使用@trace的版本。
# 因为memo_table的顺序。

# 预处理memo_table
# Dynamic Programing 动态规划
def count_change(amount, coins = (50, 25, 10, 5, 1)):
    memo_table = [ [-1] * (len(coins) + 1) for i in range(amount + 1) ]

    def count_change(amount, coins):
        if amount  < 0: return 0
        else: return memo_table[amount][len(coins)]
    
    def full_count_change(amount, coins):
        # 与原有代码一样。   
    
    # 先填充memo_table
    # 避免count_change中的一些检查计算。
    for a in range(0, amount + 1):
        memo_table[a][0] = full_count_change(a, ())
    for k in range(1, len(coins) + 1):
        for a in range(0, amount + 1):
            memo_table[a][k] = full_count_change(a, coins[-k:])
    return count_change(amount, coins)