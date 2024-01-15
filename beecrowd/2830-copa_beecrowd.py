mestreKung = int(input()) - 1
mestreLu = int(input()) - 1

if mestreLu // 2 == mestreKung // 2:
    print("oitavas")
elif mestreLu // 4 == mestreKung // 4:
    print("quartas")
elif mestreLu // 8 == mestreKung // 8:
    print("semifinal")
else:
    print("final")