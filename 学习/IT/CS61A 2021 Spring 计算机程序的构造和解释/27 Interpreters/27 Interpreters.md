# 27 Interpreters

## Scheme Read
```python
# tokenize_line(["define x", " (+ y 3))", "(define y 42)"])
# [['(', 'define', 'x'], ['(', '+', 'y', 3, ')', ')'], ['(', 'define', 'y', 42, ')']]
b = Buffer(tokenize_line(["define x", " (+ y 3))", "(define y 42)"]))
# b.pop_first() # '('
# b.pop_first() # 'define'
scheme_read(b) # Pair('define', Pair('x', Pair(Pair('+', Pair('y', Pair(3, nil))), nil)))
scheme_read(b) # Pair('define', Pair('y', Pair(42, nil)))
```

## Scheme Apply
内置函数
用户函数

### Scheme的apply与eval
```scheme
(define L '(1 2 3))
(apply + L) ; 6
(eval (list '+ 1 2)) ; 3
(eval '(+ 1 2)) ; 3
```

### evaluation of symbols

 ==================

### static and dynamic scoping
python 静态作用域/词法作用域

```scheme
; 动态作用域
(define f (x)
    (g)
)
(define g ()
    (* x 2)
)
(let ((x 3))
    (g) ; 6
    (f 2) ; 4
    (g) ; 6
)
```

### Special Form
```scheme
quote
lambda
define
if
begin
cond
and
or
```

### lambda, function
参数，body 表达式， 父级环境

### 递归
尾递归优化

### Crucial Observation
tail-call 尾调用优化，尾上下文
```scheme
(define (first x) (some-stuff) (second (+ x 1)) (other-stuff))
; 调用second, 可以直接调用third(本地环境 y=2[x+1])
(define (second y) (third y))
; 调用third，可以直接调用(* z 2)(本地环境 z=2)
(define (third z) (* z 2))
; 最终first() 直接计算(* (+ x 1) 2)
```

### Tail-Call Optimization of Tail Recursions
```scheme
(define (adder so-far n)
    ; Return SO-FAR + 1 + 2 + 3 + ... + N
    (if (<= n 0) so-far (adder (+ so-far n) (- n 1)))
)
(adder 0 2000)
; adder 0 2000
; adder 2000 1999
; ...
; 一直替换，一直迭代。
```
注：实际scheme并不是这样做的。

调试：所有调用记录都丢失了。