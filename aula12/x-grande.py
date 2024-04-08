spc_btw = 8 * 2
spc_bfr = 0

for i in range(8):
    print(" " * spc_bfr, end="")
    print("*", end="")
    print(" " * spc_btw, end="")
    print("*")
    spc_btw -= 2
    spc_bfr += 1

print(" " * spc_bfr, end="")
print("**")

for i in range(8):
    spc_btw += 2
    spc_bfr -= 1
    print(" " * spc_bfr, end="")
    print("*", end="")
    print(" " * spc_btw, end="")
    print("*")

