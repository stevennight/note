# 25 Scheme Examples

```scheme
; 非尾递归
(define (count predicate L)
    (cond ((null? L) 0) ;((eqv? L '()) 0)
          ((predicate (car L)) (+ 1 (count predicate (cdr L)))) ; 此处非尾递归
          (else (count predicate (cdr L)))
    )
)

; 尾递归 添加一个计数的值作为传参，不需要保留之前递归计算的其他东西。
(define (count sum predicate L)
    (define (count1 L s) 
        (cond ((null? L) 0)
          ((predicate (car L)) (count1 (cdr L) (+ 1 s))) ; 此处非尾递归
          (else (count1 (cdr L) s))
        )
    )
    (count1 L 0)
)


; map
(define (map fn L)
    (if (null? L) '()
        (cons (fn (car L)) (map fn (cdr L)))
    )
)
; 尾递归
(define (map fn L)
    (define (loop list-so-far L)
        (if (null? L) list-so-far
            ; append 创建一个新列表，耗时 n**2 program。
            (loop (append list-so-far (list (fn (car L)))) (cdr L))
        )
    )

    (loop '() L)
)
; 优化
(define (map fn L)
    (define (loop list-so-far L)
        (if (null? L) list-so-far
            ; 往list-so-far开头放一个元素 cons函数运行时间不变(?)
            (loop (cons (fn (car L)) list-so-far) (cdr L))
        )
    )

    (reverse (loop '() L))
)

(define (reverse L)
    (define (reverse1 so-far L)
        (if (null? L) so-far
            (reverse1 (cons (car L) so-far) (cdr L))
        )
    )
)
```

> Tree Recursions 创建新树 label-doubling 实验
