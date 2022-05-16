# 34 Review Scheme

```scheme
;#1
(define (list-tail lst k)
    (if (= k 0) lst (list-tail (cdr lst) (- k 1)))
)

(list '(a b c d) 0) ;(a b c d)
(list '(a b c d) 1) ;(b c d)...

;#2
; link-list, θ(n)
(define (list-ref lst k)
    (car (list-tail lst k))
)

(list-ref '(a b c d) 0) ;a
(list-ref '(a b c d) 3) ;d
```

## list as tree
binary saarch tree(二叉查找树)

推荐的数据结构

![](https://file.nyatori.com/images/30951ced8db4f2959ffe4e07da42b9c6.png)

scheme表示该树：
```scheme
;嵌套link list
```