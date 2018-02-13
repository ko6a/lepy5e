

def test_func(l):
    if not l:
        return [l]
    ll = "x"
    for x in test_func(ll):
        print l


l = [1, 2, 3]
test_func(l)