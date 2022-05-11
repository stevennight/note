# 31 Regular Expressions 正则表达式

声明式编程 (声明式匹配文本)

## Pattern Matching 模式匹配
声明要找的东西，让库区弄清楚如何找到它。

## Regular Expression 正则表达式
匹配特定字符的模式
```python
import re
re.search('aardvark', S)
re.fullmatch('[-+]?[0-7]+', S)

# Raw Strings 反斜杠转义字符串不会被转义。\s, \d就是实际看到的。
# 通常正则使用，避免反斜杠问题
re.match(r'\s*[-+]?\d+'. S)

"\n" # '\n'
r"\n" # '\\n'
```

```re
\
()
[] [ab,()] [a-zA-Z0-9] [-+0-9] [^a-z]
{}
+
*
?
|
$
^
.
\d 任何数字
\s 任何空格字符：space, tab, 换行, 回车, "\f", "\v"
\S 任何字符不包括空格
\w 单独的字母、数字和_下划线
\W 不匹配任何\w
```

## Combining Patterns
```re
P1P2 ab[.,]
P* [a-z]* 匹配0个或多个
P+ \d+ 匹配1个或多个
P? [-+]? 可选的，匹配P或者没有任何东西
P1|P2 \d+|Inf 匹配任何P1或P2的东西
(P)
^ 匹配字符串开头
$ 字符串结尾
\b 匹配单词的开头或结尾
\B 非\b
```
\* <- kleene star

### Python中使用
```python
# 返回match object
# fullmatch 整个字符串符合正则
matches = re.fullmatch(r'-?\d+', '123')
bool(matches) # True 可转为True/False

x = 'The Mill on the Floss'
# 开头匹配，比如这里的这里的The可以匹配，Mill不能匹配
re.match(r'The', x)
re.fullmatch(r'The.*Floss\.', x)
# 不一定是开头匹配，Mill用match不可以匹配到，但search就可以
re.search(r'Mill', x)

x = "There were 12 pence in a shilling and 20 shillings in a pound."
mat = re.search(r'(\d+).*(\d+)', x)
mat.group(0) # 12 pence in a shilling and 20
mat.groups() # ('12', '20')


for mat in re.finditer(r"(-?\d+)(/(\d+))?", x):
    # ...

re.sub(r'\s+', '-', "Replace my whitespace with\ndashes")
re.sub(r'(\S+)<(\S+)', r'\2>\1', "I think that x<10 and y<0")
re.sub(r'\d+', lambda x: str(int(x.group()) * 2), "1, 2, 3, 4, 5")
```

### Resolving Ambiguity 解决歧义
```python
re.match(r'wind|window', 'window') # wind
re.match(r'window|wind', 'window') # window
re.match(r'(wind|window)(.*)shade', 'window shade') # ('wind', 'ow ')
re.match(r'(window|wind)(.*)shade', 'window shade') # ('window', ' ')
re.match(r'(x*)(.*)', 'xxx') # ('xxx', '') * 贪婪匹配 greedy matching
re.match(r'(x+)(.*)', 'xxx') # ('xxx', '')
re.match(r'(x?)(.*)', 'xxx') # ('x', 'xx')
re.match(r'(.*)/(.+)', '12/10/2020') # ('12/10', '2020')
re.match(r'(.*)(\d*)', 'I have 5 dollars') # ('I have 5 dollars', '')
re.match(r'(.*?)(\d*)', 'I have 5 dollars') # ('I have ', '5') # lazy operators *? *+ ??
re.match(r'(.*?)(\d*)', 'I have 5 dollars') # ('', '')
```