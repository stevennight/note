# 20 Complexity and Orders of Growth 复杂度与增长的阶

## 复杂度
解决问题的 时间复杂度，空间复杂度

程序的复杂度？算法/问题复杂度？

### A Direct Approach 直接的方法
```python
from timeit  import repeat
repeat('fib(10)', globals=globals(), number=5)
# [0.00029..., 0.00027..., 0.00027...]
```
```shell
python -m timeit --setup='from fib import fib' 'fib(10)'
```
好：得到真实时间。

坏：结果仅限已测试的数据。结果仅限于指定程序、平台、负载，以及其他因素。没有给予算法或者解决问题的复杂度。

通过推断
> fib(5) 2.04 usec<br />
> fib(10) 22.5 usec<br />
> fib(15) 256 usec<br />
> fib(20) 2.75 msec<br />
> fib(25) 30.6 msec<br />
> fib(30) 345 msec<br />

↑ 1.5t<sup>1.6</sup> usec, t >= 10

### 最好，最坏，平均

```python
# L的长度，abs(x-y)<=delta导致的循环次数变化，平台，机器；迭代器、abs()、减法耗时等因素。
def near(L, x, delta):
    for y in L:
        if abs(x-y) <= delta:
            return True
    return False
```

### 推测什么？
不考虑时间
考虑程序执行了多少操作

固定消耗：程序的启动、返回等时间。

> 最小固定消耗 + M(L) * 最小循环消耗 <=
> C<sub>near</sub>(L)
> <= 最大固定消耗 + M(L) * 最大循环消耗

最坏 => M(L) = len(L)，
最好 => M(L) = 0/1

> 最小固定消耗 <=
> C<sub>near</sub>(L)
> <= 最大固定消耗 + len(L) * 最大循环消耗

> **精确的时间  =>  函数的增长趋势**

忽略有限集（小值），没有指示性。大小趋于无穷，消耗时间发生的变化。

f(n)<br />
θ(g(n)) 绝对值与g(n)成正比的函数集合<br />
|f(n)| 与 |g(n)| 成比例。

f(n) ∈ θ(g(n)), n足够大时，有K<sub>1</sub>|g(n)| ≤ |f(n)| ≤ K<sub>2</sub>|g(n)|， 0 < K<sub>1</sub> < K<sub>2</sub>。<br />
\* K<sub>1</sub> K<sub>2</sub>越接近越好，但可能界限会很宽。
\* 大O，上界限以下的函数。大Ω，下界限以上的函数。θ满足上界限以及下界限。

![函数f(x)与g(x)](https://file.nyatori.com/images/6128a7661b66bab936e7c043c00e9040.png)

如图代表了 f(n) ∈ θ(g(n))， x > 1。

### Near Function
最坏情况下，M(L) = len(L) = N。最坏情况在以下范围内：
> 最小固定消耗 + N * 最小循环消耗 ≤
> C<sub>near</sub><sup>wc</sup>(N)
> ≤ 最大固定消耗 + N * 最大循环消耗

> C<sub>near</sub><sup>wc</sup>(N) ∈ θ(N)

忽略固定消耗↓ 一个近似值
> p * N ≤
> C<sub>near</sub><sup>wc</sup>(N)
> ≤ q * N

### Typical θ Estimates 典型θ预估
\* lg = log<sub>2</sub>
```python
# 常量 θ(1)
x += L[c]
# 对数 θ(lg N)
while N > 0:
    x, N = x + L[N], N // 2
# 线性 θ(N)
for c in range(N):
    x += L[c]
# θ(N ** 2) 简单排序
for c in range(N):
    for d in range(N):
        x += L[c][d]
# 指数 θ(2 ** N) 密码算法破译
def longMax(A, L, U): # define N = U - L; L <= U
    if L == U: return A[L]
    else return max(longMax(A, L + 1, U),
                    longMax(A, L, U - 1))
# θ(N lg N) 排序常见(eg 快速排序) cs61b
def sort(L): # define N = len(L)
    M = len(L) // 2
    if M == 0: return L # Assume merge takes θ(N)
    else: return merge(sort(L[:M]), sort(L[M:]))
```

## Efficiency and Complexity 效率 复杂度
效率 与 理论上最佳执行时间相比

理论最优：算法的下界 lower bounds ->
问题的近似复杂度没有可能少于θ(f(n))，难以证明。



P = NP P ≠ NP