# 24 Scheme

scheme是lisp的方言。

## 数据类型
原子
- numbers
- symbols
- booleans: #t, #f
- empty list:()
- procedures(function)

非原子：
- pairs

### Pairs
```scheme
(V) (V.())
(V1 V2 V3) (V1.(V2.(V3.())))
(V1 V2 V3.V4) (V1.(V2.(V3.V4)))
```

表达式（特殊的对）
![](https://file.nyatori.com/images/1e0cbceba328305fd08f327246478c0d.png)

表达式和程序都是lisp数据结构，scheme程序就是scheme数据。

python语法 -> 翻译成语法树<br />
scheme语法(语法树)

### Programs
```scheme
(> 3 2) ; 3 > 2 ==> #t
(- (/ (* (+ 3 7 10) (- 1000 8)) 992) 17) ;(((3+7+10)*(1000-8))/992) - 17 ==> 3 猎鲨记
(pair? (list 1 2)) ; #t


; 特殊form
(+ 1 2) ; 3 表达式，结果3
; (quote E) 特殊form，不对E求值
(quote (+ 1 2)) ; list (+ 1 2)
'(+ 1 2) ; list (+ 1 2)

(if (> x y) x y) ; 特殊form，只对一个求值
(and (integer? x) (> x y) (< x z))
(or (not (integer? x)) (> x y) (< x z))
(lambda (x y) (/ (* x x) y))
(define pi 3.14..) ; 定义symbol(变量) 定义到当前环境
(define (f x) (* x x))


(cond ((< x 1) 'small)
      ((< x 3) 'medium)
      ((< x 5) 'large)
      (#t      'big))


;环境、定义
(define pi 3.14..) ; 定义symbol(变量) 定义到当前环境


; Numbers
(- 1000 7)
(/ 3 2)
(quotient 3 2) ; 向0取整
(> 7 2)
(integer? 5)


; list pair
(cons 1 2) ; (1 . 2)
(cons 'a (cons 'b '())) ; Like Link("a", Link("b", Link.empty)) (a b)
(define L '(a, b, c))
(car L) ; like L.first
(cdr L) ; like L.rest
(car (cdr L)) ; like L.rest.first
(cdr (cdr (cdr L)) ; ()
(list (+ 1 2) 'a 4) ; (3 a 4)


; 等价比较
(= 1 (-2 1)) ; #t
(eqv? 1 2) ; #f 作用于numbers, empty list, booleans, symbols
(define L '(1 2 3))
(eqv? L '(1 2 3)) ; #f 相当于python的is
(eq? L '(1 2 3)) ; #f 相当于python的is 可能无法作用于numbers
(equal? '((1 2) 3 (4))) (list (list 1 2) 3 (list 4)) ; #t
(eqv? '((1 2) 3 (4))) (list (list 1 2) 3 (list 4)) ; #f 比较对象


; Let
(define x 17)
(let ((x 5)
      (y (+ x 2)))
    (+ x y))
((lambda (x y) (+ x y) 5 (+ x 2))) ; 等价上面的写法，输出24


; 循环 尾递归 Loops and Tail Recursion
; 尾递归，会被底层转换为迭代 但是!python等其他高级语言没有这个转换 依然使用栈进行递归处理
(define (sumsq n)
  (define (sumsq1 s n)
    (if (<= n 0) s
        (sumsq1 (+ s (* n n))
                (- n 1))))
  (sumsq1 0 n))
```