value = input()
x = value.split()
a = x[0]
b = x[1]
c = x[2]

if a < b and a < c:
    print(a)
    if b < c:
        print(f"{b}\n{c}")
    else:
        print(f"{c}\n{b}")
elif b < a and b < c:
    print(b)
    if a < c:
        print(f"{a}\n{c}")
    else:
        print(f"{c}\n{a}")
elif c < a and c < b:
    print(c)
    if a < b:
        print(f"{a}\n{b}")
    else:
        print(f"{b}\n{a}")
print(f"\n{a}\n{b}\n{c}")