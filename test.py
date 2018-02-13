#!/usr/bin/python

def permute_test(seq):
    res = []
    for i in range(len(seq)):
        rest = seq[:i] + seq[i+1:] # Delete current node
        for x in permute1(rest): # Permute the others
            res.append(seq[i:i+1] + x) # Add node at front
    return res

a = 0

def permute1(seq):
    global a 
    a = a + 1

    print
    print "#################"
    print a
    print "FUNC"

    if not seq:

        print "if begin"
        print "NOT SEQ"
        print "seq:", seq
        print "if end"

        return [seq] # Empty sequence
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:] # Delete current node

            print "CYCLE 1 BEGIN"
            print "seq[:i]", seq[:i]
            print "seq[i+1:]", seq[i+1:]
            print "rest:", rest

            for x in permute1(rest): # Permute the others
                res.append(seq[i:i+1] + x) # Add node at front

                print "CYCLE 2 START"
                print "x:", x
                print "seq:", seq
                print "i:", i
                print "seq[i:i+1]", seq[i:i+1]
            print "CYCLE 2 END"
            print
        print "CYCLE 1 END"
        print

        return res

def permute2(seq):
    if not seq: # Shuffle any sequence: generator
        yield seq # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:] # Delete current node
            for x in permute2(rest): # Permute the others
                yield seq[i:i+1] + x

def scramble(seq):
    l = []
    for i in range(len(seq)): # Generator function
        yield seq[i:] + seq[:i] # Yield one item per iteration
        # print seq[i:]
        # print seq[:i]
        # print "cycle"
        # l.append(seq[i:] + seq[:i])
    # return l

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

def tester(func, items, trace=True):
    for args in scramble(items): # Use generator (or: scramble2(items))
        if trace: print(args)
        print(sorted(func(*args)))


# print list(scramble('abc'))

l = permute1('ab') # Permutations larger: N!
print 
print "###############"
print l

# print permute_test('abc')

# list(permute2('abc')) # Generate all combinations
# G = permute2('abc') # Iterate (iter() not needed)
# next(G)
# next(G)
