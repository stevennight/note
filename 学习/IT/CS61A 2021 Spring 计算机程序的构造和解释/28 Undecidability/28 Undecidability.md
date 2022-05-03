# 28 Undecidability

## The Halting Problem 停止问题
程序会无限循环吗？是否有程序可以分析到？

```scheme
(define (halts? defn x) ...)
```

Alan Turing: 解决停止问题是不可能的

Alan Turing: 图灵测试

### Partial Solutions
有时可以解决：
1. 运行上百次是否终止，是怎是。否则不确定。
2. 更复杂的程序有时可以让你知道是否进入了循环甚至什么时候进入循环。
3. 但对于一些输入，无论什么分析函数，都会得到错误答案或放弃或进入死循环。

### 用矛盾证明不可能 biting your tail
```scheme
;; Return a true value iff DEFN is a Scheme definition that defines a
;; one-argument function that eventually halts given the input X.
(define (halts? defn x) alleged definition of halts?)
(define halts?-bogus-program
(quote (define (halts?-bogus x)
(define (halts? defn x) alleged definition of halts?)
(define (loop) (loop))
(if (halts? x x) (loop) #t))))
(halts? halts?-bogus-program halts?-bogus-program) ; (*)
```

### Consequences 结论
不能判断两个程序是否在计算相同的东西（转换为停止问题）

没法写出完美的杀毒软件，无法判断一个程序是否做他应该做的。

哥德尔不完全性定理，与数学某些断言的不可判定性有关。

罗素悖论


证明

可以编写一个程序来检查给定的证明的正确性

Incompleteness Theorem

Completeness

可以通过选择正确的模型来选择命题是否为真。

Nonstandard Model


在分析程序时能做什么、不能做什么有实际的影响。

> 数学课，后续可以重新看 看懵了。