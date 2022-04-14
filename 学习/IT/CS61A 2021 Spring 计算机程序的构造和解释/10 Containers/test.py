def pair(a, b):
    """返回一对非负整数（A, B） 2和3是质数，利用质数性质。"""
    return 2**a * 3**b

def left(p):
    return multiplicty(2, p)
def right(p):
    return multiplicty(3, p)
def multiplicty(factor, n):
    """假设factor, n是整数，factor > 1。返回n可以被factor整除的次数。"""
    # 实现
    # 待运行看看对不对。
    if n % factor != 0:
        return 0
    return 1 + multiplicty(factor, n / factor)