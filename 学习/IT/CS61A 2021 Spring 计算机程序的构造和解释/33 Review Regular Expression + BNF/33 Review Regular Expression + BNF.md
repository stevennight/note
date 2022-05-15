# 33 Review Regular Expression + BNF

## RegEx

[正则表达式解析、说明工具](https://regexr.com/)

用到哪里？
- java, perl, js etc
- ides
- sql
- spreadsheet
- html

html例子：
```html
<input name="zip" type="text" pattern="\d\d\d\d\d">
<input name="zip" type="text" pattern="\d{5}">
<input name="zip" type="text" pattern="\d{5,}">
<input name="zip" type="text" pattern="\d{0,5}">
```

```javascript
/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2.,}$/g
// 单词边界
/\bGME\b/g
```

## BNF

> 可以在code.cs61a.org尝试

BNF，描述语言语法的语法，通常用于编程语言。

用到哪里？
- 语言规范：python, CSS, SaSS, XML
- 文件格式：Google's robots.txt
- 协议：Apache Kafka
- 解析以及编译器
- 文本生成

相比编写技能，更多是阅读技能【阅读文档】

``` bnf
start: calc_expr
?calc_expr: NUMBER | calc_op
calc_op: "(" OPERATOR calc_expr* ")"
OPERATOR: "+" | "-" | "*" | "/"

%ignore /\s+/
%import common.NUMBER
```
0xDEADBEEF => JAVA标记JAVA文件的内容

注意歧义