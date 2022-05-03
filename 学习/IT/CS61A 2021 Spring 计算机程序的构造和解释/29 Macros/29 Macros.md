# 29 Macros 宏

设置一个名称，将名称部分替换为指定的值。

### Quasiquote
```scheme
(list 'a 'b (+ 2 3 'd)) ; (a b 5 d)
`(a b ,(+ 2 3) d)

(define values (list (+ 2 3) (- 2 1)))
(append '(a b) values '(d)) ; (a b 5 1 d)
`(a b ,@values d)
```

### Example
```scheme
(define x 3)
(unless (list? x) (displayln x))
; instead of (if (not (list? x)) (displayln x))

(define-macro (unless cond body) `(if (not ,cond) ,body))


; 2
(define L '(1 2 3 4 5))
(for-list x (* x x) L) ; (1 4 9 16 25) Like [ x*x for x in L]
(define-macro (for-list var expr lst) `(map (lambda (,var) ,expr) ,lst))
; 上面的表达式for-list被替换为
; (map (lambda (x) (* x x)) L) <= eval()执行返回结果


;3
(for-range x 1 5 (* x x)) ; (1 4 8 16 25) Like [ x*x for x in range(1, 6) ]
(define-macro (for-range control-var low high body)
    ; 这里保存了low，保证只计算一次   low碰巧有副作用的函数就不好了(?)
    `(let (($low$ ,low))
        (define ($loop$ $so-far$ ,control-var)
            (if (< ,control-var $low) $so-far$
                ($loop$ (cons ,body $so-far$) (- ,control-var 1))
            )
        )
        ($loop$ '() ,high)
    )
)


; 4
(for (x (list 1 2 3 4 5)) (* x x)) ; for-list
(for (x 1 5) (* x x)) ; for-range

(define-macro (for list-spec body)
    (let ((control-var (car list-sec))
            (opnds (cdr list-spec)))
        ; 条件编译
        (if (= (length opnds) 1)
            `(for-list ,control-var ,body ,(car opnds))
            `(for-range ,control-var ,(car opnds ,(car (cdr opnds)) ,body)
        )
    )
)
```

### Name Clashes
```scheme
(define $low$ 15)
(for-range x 1 5 (* $low$ x)) ; 与全局的$low$变量冲突。 期望(15 30 45 60 75)。实际(1 2 3 4 5)

; some lisp dialects supply a builtin function gensym. generates new symbols that are guaranteed（保证） to differ from all other symbols.
(let ((low-name (gensym))))
```