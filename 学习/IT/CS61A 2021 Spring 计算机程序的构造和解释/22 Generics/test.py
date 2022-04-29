from cgi import test


def sum_custom(items, init):
    total = init
    for item in items:
        total += item
    return total

print(sum_custom(["a", "b"], ""))

class Test:
    def test(self, ll):
        ll[0] = "test"

t = Test()
ll = [1,2,3]
t.test(ll)
print(ll)