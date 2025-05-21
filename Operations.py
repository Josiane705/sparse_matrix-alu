from Sparse import SM

# Read matrix from file
def read(f):
    with open(f, 'r') as x:
        l = [i.strip() for i in x if i.strip()]
    r = int(l[0].split('=')[1])
    c = int(l[1].split('=')[1])
    m = SM(r, c)
    for line in l[2:]:
        a, b, v = map(int, line[1:-1].split(','))
        m.set(a, b, v)
    return m

# Write matrix to file
def save(m, f):
    with open(f, 'w') as x:
        x.write(f"rows={m.r}\n")
        x.write(f"cols={m.c}\n")
        for (i, j), v in m.items():
            x.write(f"({i},{j},{v})\n")


