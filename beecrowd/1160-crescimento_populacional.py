T = int(input())

for _ in range(T):
    PA, PB, G1, G2 = map(float, input().split())
    PA, PB = int(PA), int(PB)
    anos = 0

    while PA <= PB:
        anos += 1
        PA = int(PA * (1 + G1/100))
        PB = int(PB * (1 + G2/100))

        if anos > 100:
            print("Mais de 1 seculo.")
            break

    if anos <= 100:
        print(f"{anos} anos.")