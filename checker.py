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
    return 1
