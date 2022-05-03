# 30 Declarative Programming 声明式编程

声明式编程，又叫Programming Paradigm 编程范式

之前都是命令式编程，告诉电脑应该如何完成任务
（能确切指定如何做某事的任何类型的编程）

prolog

(fact Conclusion Hypothesis1 Hypothesis2)

Prolog程序由这样的断言组成。

### example
Scheme风格Prolog：
``` scheme
(load math.logic)
# (fact) 数据
(fact (parent george paul))
(fact (ancestor ?X ?Y) (parent ?X ?Y))
(query (ancestor martin ann))
(query (ancestor martin ?x))
(query (ancestor ?x ?y))
; + 0, * 1很容易造成无限循环。
```

↑关系，非函数
```scheme
(abs -3 3) ; 3是-3的绝对值
(add x y z) ; z是x与y相加

(? (eval (+ 1 2) 3))
```

```scheme
; 第一个操作符是谓词 true/false函数。操作数是谓词的数据、不代表程序调用，是字面量。
; 除了逻辑变量，表示为以?开头的符号。
(ordered (0 1 2))
(fact CONCLUSION HYPOTHESIS ...) ; 可以多个假设

; operational and declarative meanings
(fact (eats ?P ?F) (hungry ?P) (has ?P ?F) (likes ?P ?F))
; declarative 声明式 meaning:
; P饿了，P有F，P喜欢F，那P吃了F  将程序视为系统要找到解决方案的问题的【逻辑规范】
; operational 操作层面 meaning:
; 证明P吃F，因为P饿了，P有F以及P喜欢F  将规范视为寻找解决方案【运行程序】
```

closed universe assumption 封闭宇宙假设<br />
如果你找不到证明你的断言的证据 那假设为假。

