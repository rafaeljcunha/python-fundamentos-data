
while True:
    sentence = input()

    if sentence == '*':
        break

    words = sentence.split()
    first_letter = words[0][0].lower()

    is_tautogram = all(word[0].lower() == first_letter for word in words)

    if is_tautogram:
        print('Y')
    else:
        print('N')
