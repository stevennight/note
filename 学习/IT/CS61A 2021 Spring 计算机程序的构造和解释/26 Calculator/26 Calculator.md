# 26 Calculator

Machine Language: 让机器理解，由硬件执行

High-level Language：由程序执行

High-level Language -> 程序编译器compiler/解释器Interpreter -> 其他语言，通常是Machine Language

## metalinguistic abstraction
定义一种新语言，metalinguistic abstraction 元语言抽象

- erlang 为并发程序编写语言
- mediawiki mark-up language（标记语言） 写网页的语言

## parsing
text 【词法分析Lexical Analysis】-> tokens 【语法分析Syntactic Analysis】-> expression

```
# text
(+ 1
    (- 23)
    (* 4 5.6))

# token
'(', '+', 1
'(', '-', 23, ')'
'(', '*', 4, 5.6, ')', ')'

# expression 抽象语法树
Pair('+', Pair(1, ...))
#printed as 
(+ 1 (- 23) (* 4 5.6))
```

语法分析识别表达式层级结构，可能是嵌套的。
每次调用scheme_read消耗一个表达式的输入token。
输出翻译的对（pair）。
一个递归过程。
见到'('就会开始递归，直到遇到')'。

## Scheme-Syntax Calculator

Pair
```python
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
```

Calculator Syntax

![](https://file.nyatori.com/images/0f70a0f8b4ab902944596177e9054b12.png)


Calculator Semantics

![](https://file.nyatori.com/images/2922bf0e59a199bbad8d5bad08f73a3d.png)

## Evaluation
```python
def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return calc_apply(exp.first, arguments)
    else
        raise TypeError

def calc_apply(operator, args):
    if operator == '+':
        return reduce(add, args, 0)
        # ...
    else:
        raise TypeError
```

## Interactive Interpreters
### Read-Eval-Print Loop
1. Print a prompt 
2. Read text input from the user 
3. 解析文本为表达式（Pair）
4. Evaluate the expression 
5. If any errors occur, report those errors, otherwise 
6. Print the value of the expression and repeat

可参考压缩包内代码