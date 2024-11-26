for m in range(2, 20):
    prime = True
    for j in range(2, m):
        if m % j == 0:
            prime = False

    if prime:
        print(m)