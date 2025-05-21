from Operations import read, save
from Methods import add, sub, mul

print("Choose:")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
op = input("Enter 1 / 2 / 3: ")

f1 = input("First file: ")
f2 = input("Second file: ")
out = input("Save to: ")

try:
    m1 = read(f1)
    m2 = read(f2)

    if op == '1':
        res = add(m1, m2)
    elif op == '2':
        res = sub(m1, m2)
    elif op == '3':
        res = mul(m1, m2)
    else:
        print("Wrong choice.")
        exit()

    save(res, out)
    print("Done! Saved to", out)
except Exception as e:
    print("Error:", e)
