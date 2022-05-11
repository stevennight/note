# 32 BNF(Backus-Naur Form)

## 描述语言句法 BNF
Algol 60 引入

Backus-Naur Form：巴科斯诺尔范式

```BNF
# 描述字典的句法、字典的构造函数
dict_display       ::= "{" [key_list | dict_comprehension] "}"
key_list           ::= key_datum ("," key_datum)* [","]
key_datum          ::= expression ":" expression
                   |   "**" or_expr
dict_comprehension ::= expression ":" expression comp_for
```

python package Lark

algol 60 引入的"::="，python文档也用这种格式。
Lark包使用的是":"。

## BNF vs Regular Expression
文本中模式(patterns)的声明式语言

BNF 比 正则表达式 更强大。<br />
比如：包含任意深度匹配括号【正则 ×】

正则表达式描述的语言称为regular / type 3 languages. 【正则语言】
BNF 描述 context-free / type 2 languages. 【上下文无关语言】

type 0 languages, church's thesis丘奇理论，可以描述任何算法描述的集合。

## 基础BNF
```BNF
# 一个symbol代表一个字符串集合（sets of strings）
symbol0: symbol1 symbol2 ... symbol n (n ≥ 0)
```
Nonterminal symbols 非终结符：其它变量名（小写）。symbol0永远是非终结符。<br />
Terminal symbols 终结符：带引号的字符串，正则表达式，定义的大写名称

``` BNF
# or
number: octal_number | decimal_number | hexadecimal_number
```

## 定义Terminal(终结符)
```BNF
NUMBER: /\d+(\.\d+)/
FRACTION: NUMBER "/" NUMBER
```

解释空格、注释，让语法变得混乱。
几乎所有BNF解析器生成器都会忽略这些。
`%ignore /\s+/`

## 例子
```Lark
// 默认情况下，"start"定义所有的匹配字符串
start: sentence
sentence: noun_phrase verb
noun: NOUN
noun_pharse: article noun
article:: | ARTICLE
verb: VERB

NOUN: "horse" | "dog" | "hamster"
ARTICLE: "a" | "the"
VERB: "stands" | "walks" | "jumps"
%ignore /\s+/

// the grammar will match(术语 accept)
// the horse jumps
// a dog walks
```

## Repeated Patterns
```Lark
numbers: numbers "," INTEGER | INTEGER
INTEGER: /-?\d+/
```

## Nested Recursions
正则表达式无法描述

```Lark
// 匹配 () (()) ((())) ...
nest: "(" ")" | "(" nest ")"
```

## Extended BNF(EBNF)
| 符号 | 解释 | 原生BNF |
| -- | -- | -- |
| item* | 0或多个 | items: \| items item |
| item+ | 1或多个 | items: item \| items item |
| [ item ] | 可选项 | opt_item:  \| item |
| item? | 同上 | 同上 |

```BNF
name: /\w+/
number: /\d+/
list: ( name  | number )+
numbered_list: ( name [ ":" number ] )+
comma_separated_list: [ name ("," name)* ]
```

## Caculator
```BNF
start: calc_expr
// ? 只有一个子树，在语法树上省略，具体参见语法树
?calc_expr: NUMBER | calc_op
calc_op: "(" OPERATOR calc_expr* ")"
OPERATOR: "+" | "-" | "*" | "/"
%ignore /\s+/
// Lark库
$import common.Number
```

## Syntax Tree

Calculator Tree:

![计算器的语法树](https://file.nyatori.com/images/39e6073e822656e82345040b3cff2661.png)

1. 规则 -> 非终结符 -> 树的节点(node)，子节点是token或者树（规则）
1. 叶子节点没有子节点并且是终结符（token）
1. Lark默认会移除 字符串，保留命名的token(NUMBER)以及正则定义的token
1. 规则以?开头并且只有一个子节点的会被移除（calc_expr）
1. abstract syntax tree

## Evaluation
```python
from Lark import Transformer
class Eval(Transformer):
    def start(self, args):
        return args[0]
    def calc_op(self, args):
        op = args[0]
        if op == '+':
            return sum(args[1:])
        elif op == '-':
            # ...
    def NUMBER(self, num):
        return float(num)

evaluator = Eval()
print(evaluator.transform(tree))
```

## Ambiguity 歧义
与正则表达式类似

```BNF
?start: expr
?expr: NUMBER | expr OPERATOR expr
OPERATOR: "+" | "-" | "*" | "/"
```

`3+7*2`的树：

![](https://file.nyatori.com/images/05897b0b540a80fafba6b18980111c3e.png)

消除歧义：
```BNF
// 经典
?start: expr
?expr: ?add_expr
?add_expr: mul_expr | add_expr ADDOP mul_expr
?mul_expr: NUMBER | mul_expr MULOP NUMBER
ADDOP: "+" | "-"
MULOP: "*" | "/"
```

![](https://file.nyatori.com/images/2487f0f7c3a812f78ee1d65c832db89c.png)