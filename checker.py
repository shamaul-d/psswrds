def passmin(s):
    h = [x for x in s]
    num = [chr(a) for a in range(48,58)]
    cap = [chr(b) for b in range(97,123)]
    low = [chr(c) for c in range(65,91)]
    ansi = [d for d in h if d in num]
    ansc = [e for e in h if e in cap]
    ansl = [f for f in h if f in low]
    return (len(ansi) != 0 and len(ansc) != 0 and len(ansl) != 0)

print passmin("asdfghjkl")
print passmin("asdf4ik")
print passmin("asdfgQWERT789")
print passmin("a1L")

def pstrength(s):
    h = [x for x in s]
    num = [chr(a) for a in range(48,58)]
    cap = [chr(b) for b in range(97,123)]
    low = [chr(c) for c in range(65,91)]
    misc = [chr(d) for d in range(33,48)]
    misc2 = [chr(e) for e in range(58,65)]
    ansi = [f for f in h if f in num]
    ansc = [g for g in h if g in cap]
    ansl = [i for i in h if i in low]
    ansm = [j for j in h if i in misc or i in misc2]
    i = 0
    length = len(h) / 2
    if (len(ansi) != 0):
        i = 1
    c = 0
    if (len(ansc) != 0):
        c = 1
    l = 0
    if (len(ansl) != 0):
        l = 1
    lets = c + l
    if (c == 1 and l == 1):
        lets = 3
    m = 0
    if (len(ansm) != 0):
        m = 3
    ans = length + i + lets + m
    if (ans > 10):
        ans = 10
    return ans


print pstrength("asdfghjkl")
print pstrength("asdfGHJKL")
print pstrength("asdf4ik")
print pstrength("asdfgQWERT789!*")
print pstrength("a1L")
print pstrength("a1L!!")


