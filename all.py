n = 5
for i in range(1, n+1):
    print('*' * i)



n = 5
for i in range(n, 0, -1):
    print('*' * i)


n = 5
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))


n = 5
for i in range(n, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))


n = 5

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

for i in range(n-1, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))


n = 5
for i in range(1, n+1):
    if i == 1 or i == n:
        print('*' * i)
    else:
        print('*' + ' ' * (i-2) + '*')


n = 5
for i in range(1, n+1):
    print(' '.join(str(x) for x in range(1, i+1)))


n = 5
for i in range(n, 0, -1):
    print(' '.join(str(x) for x in range(1, i+1)))


n = 5
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
    print()


n = 5
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()


n = 5
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i + '*' * (i-1))


n = 5
for i in range(1, n+1):
    print(str(i) * i)



n = 5
for i in range(1, n+1):
    if i == 1 or i == n:
        print(' ' * (n-i) + '*' * (2*i-1))
    else:
        print(' ' * (n-i) + '*' + ' ' * (2*i-3) + '*')


n = 5
for i in range(1, n+1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)
for i in range(n-1, 0, -1):
    print('*' * i + ' ' * (2*(n-i)) + '*' * i)



n = 5
ch = 65
for i in range(1, n+1):
    print(chr(ch) * i)
    ch += 1


n = 5
ch = 65
for i in range(n, 0, -1):
    print(chr(ch) * i)
    ch += 1


n = 5
num = 1
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
    num += 1



n = 5
for i in range(1, n+1):
    print('*' * i)
for i in range(n-1, 0, -1):
    print('*' * i)



n = 5

for i in range(1, n+1):
    if i == 1:
        print(' ' * (n-i) + '*')
    else:
        print(' ' * (n-i) + '*' + ' ' * (2*i-3) + '*')

for i in range(n-1, 0, -1):
    if i == 1:
        print(' ' * (n-i) + '*')
    else:
        print(' ' * (n-i) + '*' + ' ' * (2*i-3) + '*')



n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print('*', end="")
        else:
            print(" ", end="")
    print()


n = 5
for i in range(n):
    print('* ' * n)



n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end="")
        else:
            print(" ", end="")
    print()


n = 5
for i in range(n, 0, -1):
    if i == 1 or i == n:
        print('*' * (2*i-1))
    else:
        print(' ' * (n-i) + '*' + ' ' * (2*i-3) + '*')


n = 5
for i in range(1, n+1):
    print(str(i) + ' ' * (n-i) + '*' * i)

