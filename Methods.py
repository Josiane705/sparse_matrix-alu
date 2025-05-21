
from Sparse import SM

def check(a, b, op):
    if op in ('add', 'sub'):
        if a.r != b.r or a.c != b.c:
            raise ValueError("Matrix sizes don't match")
    elif op == 'mul':
        if a.c != b.r:
            raise ValueError("Columns of A must match rows of B")

# Add two sparse matrices
def add(a, b):
    check(a, b, 'add')
    z = SM(a.r, a.c)
    for (i, j), v in a.items():
        z.set(i, j, v)
    for (i, j), v in b.items():
        z.set(i, j, z.get(i, j) + v)
    return z

# Subtract two sparse matrices
def sub(a, b):
    check(a, b, 'sub')
    z = SM(a.r, a.c)
    for (i, j), v in a.items():
        z.set(i, j, v)
    for (i, j), v in b.items():
        z.set(i, j, z.get(i, j) - v)
    return z

# Multiply two sparse matrices
def mul(a, b):
    check(a, b, 'mul')
    z = SM(a.r, b.c)
    for (i, k), v in a.items():
        for j in range(b.c):
            if b.get(k, j) != 0:
                z.set(i, j, z.get(i, j) + v * b.get(k, j))
    return z
