lin = int(input("Quantas linhas? "))
spc = lin

for l in range(1, lin*2, 2):
    spc-=1
    print(" " * spc, end="")
    print("*" * l)

print(f'{" "*(lin-2)}| |')
print(f'{" "*(lin-2)}| |')
print(f'{" "*(lin-2)}| |')