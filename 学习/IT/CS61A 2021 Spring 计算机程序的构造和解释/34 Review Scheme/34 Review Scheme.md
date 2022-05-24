# 34 Review Scheme

```scheme
;#1 list tail
(define (list-tail lst k)
    (if (= k 0) lst (list-tail (cdr lst) (- k 1)))
)

(list '(a b c d) 0) ;(a b c d)
(list '(a b c d) 1) ;(b c d)...

;#2 list element by index
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

![array tree](https://file.nyatori.com/images/8aadd817821599e826b681cae4c1c8fd.png)
array tree(数组树)

scheme表示该树：
```scheme
;嵌套link list
(define (arr-index arr) (car arr))
(define (arr-value arr) (car (cdr arr)))
(define (arr-left arr) (car (cdr (cdr arr))))
(define (arr-right arr (car (cdr (cdr (cdr arr))))))
(define (arr-make index value left right) (list index value left right))
(define arr-empty nil)

; (eq? arr arr-empty) 用arr-empty是抽象，因此不用nil。
; θ(lg N)
; 树递归，树递归一般是指数递增(多次调用)
; 但是这里是尾递归，因为条件关系，每次也只调用一次（而不是多次调用）
(define (get arr k) 
    (cond ((eq? arr arr-empty) (error "bad index"))
          ((= (arr-index arr) k) (arr-value arr))
          ((> (arr-index arr) k) (get (arr-left arr) k))
          (#t (get (arr-right arr) k))
    )
)
```

## Building an Array Tree
取中间节点，作为树的根节点，两边是两边的子树。
=> 递归问题。

![](https://file.nyatori.com/images/dd0ad15822eac04f2ec45da6fbae1786.png)

```scheme
(define (list-to-array lst)
    (defien (partial-list-to-array L m start)
        (cond ((= m 0) arr-empty)
              (#t 
                (arr-make 
                    (+ start (quotient m 2))
                    (list-ref L (quotient m 2))
                    (partial-list-to-array L (quotient m 2) start)
                    (partial-list-to-array 
                        (list-tail L (+ 1 (quotient m 2)))
                        (- m (quotient m 2) 1)
                        (+ (quotient m 2) 1 start)
                    )
                )
              )
        )
    )
    (partial-list-to-array lst (length lst) 0)
)
```